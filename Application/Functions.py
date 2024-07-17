import json
import os
import pickle
from pathlib import Path
import Functions as functions

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from feature_engine.discretisation import DecisionTreeDiscretiser

from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import mutual_info_classif
import lightgbm as lgb
import xgboost as xgb
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, roc_curve, auc, confusion_matrix, accuracy_score, precision_score, \
    recall_score, f1_score, adjusted_rand_score, r2_score, silhouette_score, davies_bouldin_score, \
    calinski_harabasz_score, classification_report
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

import pandas as pd
import joblib
from ctgan import CTGAN
from sklearn.model_selection import ParameterGrid
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import random
import Constantes as const


# Functions

# Conversion del dataFrame a tipo numeric
def convert_to_numeric(column):
    if column.dtype in ['object', 'category']:
        # Verificar si hay letras en todos los registros
        contains_letters = any(isinstance(val, str) and any(c.isalpha() for c in val) for val in column)
        if not contains_letters:
            return pd.to_numeric(column, errors='coerce')
    return column


def discretizar_df_arboles_1(df, max_depth=40, n_bins=18, rango_discretizacion=(-np.inf, np.inf)):
    df_discretizado = pd.DataFrame()

    # Iterar sobre todas las columnas del dataframe original
    for columna in df.columns:
        if df[
            columna].dtype.kind in 'biufc' or columna.name == 'Tumor type':  # (CHULO) Comprueba si el tipo de datos de la columna es numérico ('b' para booleano, 'i' para entero, 'u' para sin signo, 'f' para flotante o 'c' para complejo)
            # Si la columna es numérica, realizar la discretización
            dt = DecisionTreeRegressor(max_depth=max_depth)
            dt.fit(df[columna].values.reshape(-1, 1), df[columna])
            puntos_corte = dt.tree_.threshold[
                dt.tree_.threshold != -2]  # Extrae los puntos de corte del árbol de decisión para la columna numérica específica, ignorando aquellos puntos de corte asociados con nodos hoja (-2)
            puntos_corte = np.sort(puntos_corte)
            puntos_corte = np.concatenate(([rango_discretizacion[0]], puntos_corte, [rango_discretizacion[1]]))
            df_discretizado[f'{columna}'] = pd.cut(df[columna], bins=puntos_corte, labels=range(len(puntos_corte) - 1))
        else:
            # Si la columna no es numérica, simplemente copiarla al dataframe resultante
            df_discretizado[columna] = df[columna]

    return df_discretizado.apply(convert_to_numeric)


# Discretizar dataFrame y mostrar correlación respecto a la variable objetivo
def discretizar_df_arboles(df, imprimir="SI", max_depth=15, rango_discretizacion=(-np.inf, np.inf)):
    df_discretizado = pd.DataFrame()

    # Iterar sobre todas las columnas del dataframe original
    for columna in df.select_dtypes(include=['number']).columns:
        if df[
            columna].dtype.kind in 'biufc' or columna.name != 'Tumor type':  # (CHULO) Comprueba si el tipo de datos de la columna es numérico ('b' para booleano, 'i' para entero, 'u' para sin signo, 'f' para flotante o 'c' para complejo)
            # Si la columna es numérica, realizar la discretización
            dt = DecisionTreeRegressor(max_depth=max_depth)
            dt.fit(df[columna].values.reshape(-1, 1), df[columna])
            puntos_corte = dt.tree_.threshold[
                dt.tree_.threshold != -2]  # Extrae los puntos de corte del árbol de decisión para la columna numérica específica, ignorando aquellos puntos de corte asociados con nodos hoja (-2)
            puntos_corte = np.sort(puntos_corte)
            puntos_corte = np.concatenate(([rango_discretizacion[0]], puntos_corte, [rango_discretizacion[1]]))
            # print(f"\t Columna : {columna} \n Puntos de Corte : \n {puntos_corte}")
            df_discretizado[f'{columna}'] = pd.cut(df[columna], bins=puntos_corte, labels=range(len(puntos_corte) - 1))
        else:
            # Si la columna no es numérica, simplemente copiarla al dataframe resultante
            df_discretizado[columna] = df[columna]

    # Calcular el coeficiente de correlación entre las variables numéricas discretas y la variable objetivo binaria
    correlaciones_discretas = df_discretizado.corrwith(df_discretizado['Tumor type'])

    # Ordenar las correlaciones de mayor a menor
    correlaciones_discretas_ordenadas = correlaciones_discretas.abs().sort_values(ascending=False)

    # Obtener las top 20 variables numéricas discretas con las correlaciones más altas
    top_20_correlaciones_discretas = correlaciones_discretas_ordenadas.nlargest(20)

    if imprimir == "SI":
        # Imprimir las top 20 correlaciones
        print(top_20_correlaciones_discretas)

    return df_discretizado


def escalado_dataFrame(df):
    if df.empty:
        raise ValueError("El DataFrame está vacío, no se puede realizar el escalado.")

    # Crear un objeto StandardScaler
    scaler = StandardScaler()

    # Normalizar df_imputacion_iterativa
    df_normalized = df.select_dtypes(include=['number']).copy()  # Crear una copia del DataFrame original

    if not df_normalized.empty:
        df_normalized[df_normalized.columns] = scaler.fit_transform(df_normalized)
    else:
        print("Esto está vacío")
    return df_normalized


def calcular_ganancia_informacion(df_features, target, imprimir='SI'):
    # Extraer las características de interés del DataFrame
    X_interest = df_features.values

    # Extraer la variable objetivo del DataFrame principal
    y = target.values

    # Calcular la Ganancia de Información utilizando Mutual Information
    information_gain = mutual_info_classif(X_interest, y, discrete_features=False, random_state=42, n_neighbors=7)

    # Crear un DataFrame para visualizar los resultados
    ig_results = pd.DataFrame({'Feature': df_features.columns, 'Information Gain': information_gain})

    # Ordenar los resultados por Ganancia de Información en orden descendente
    ig_results_sorted = ig_results.sort_values(by='Information Gain', ascending=False)

    if imprimir == "SI":
        print(ig_results_sorted)


# División del conjunto de datos en entrenamiento, validacion y test


def split_data(X, y, train_size=0.6, val_size=0.2, test_size=0.2, random_state=None):
    """
    Divide un conjunto de datos en entrenamiento, validación y test.

    Args:
        X: Matriz de características.
        y: Vector de etiquetas.
        train_size: Porcentaje de datos para entrenamiento (por defecto: 0.6).
        val_size: Porcentaje de datos para validación (por defecto: 0.2).
        test_size: Porcentaje de datos para test (por defecto: 0.2).
        random_state: Semilla para la aleatorización (por defecto: None).

    Returns:
        Tuple: (X_train, X_val, X_test, y_train, y_val, y_test).
    """
    assert train_size + val_size + test_size == 1.0, "La suma de train_size, val_size y test_size debe ser igual a 1.0"

    # Dividir los datos en entrenamiento y test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state,
                                                        shuffle=True)

    # Calcular porcentaje respecto al tamaño original
    val_size_relative = val_size / (1.0 - test_size)

    # Dividir los datos de entrenamiento en entrenamiento y validación
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size_relative,
                                                      random_state=random_state, shuffle=True)

    return X_train, X_val, X_test, y_train, y_val, y_test


def mostrar_cross_validation(model, X_train, y_train):
    cv_scores = cross_val_score(
        estimator=model,
        X=X_train,
        y=y_train,
        scoring='neg_root_mean_squared_error',
        cv=5
    )
    print("Cross validation : ")
    print(f"Métricas validación cruzada: {cv_scores}")
    print(f"Média métricas de validación cruzada: {cv_scores.mean()}")
    print("")


def mostrar_score(X_train, y_train, model):
    score = round(model.score(X_train, y_train), 3) * 100
    print(f"Tanto por ciento de acierto : {score} %")
    print("")


def mostrar_estadisticas(y_val, y_pred):
    mse = round(mean_squared_error(y_val, y_pred), 3)
    accuracy = round(accuracy_score(y_val, y_pred), 3)
    precision = round(precision_score(y_val, y_pred), 3)
    recall = round(recall_score(y_val, y_pred), 3)
    f1 = round(f1_score(y_val, y_pred), 3)
    conf_matrix = confusion_matrix(y_val, y_pred)

    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)
    print("Error cuadrático medio en el conjunto de validación:", mse)
    print("Matriz de Confusión :\n", conf_matrix)
    print("")


def mostrar_curva_ROC(y_val, y_pred):
    fpr, tpr, _ = roc_curve(y_val, y_pred)

    # Calcular el área bajo la curva ROC (AUC)
    roc_auc = auc(fpr, tpr)

    # Plotear la curva ROC
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='Curva ROC (AUC = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Tasa de Falsos Positivos')
    plt.ylabel('Tasa de Verdaderos Positivos')
    plt.title('Curva ROC')
    plt.legend(loc="lower right")
    plt.show()


def evaluate_model(model, X, y, set_name):
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    print(f"Metrics for {set_name} set:")
    print(f"Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1-Score: {f1:.4f}")


# Función para mostrar métricas y añadirlas a un DataFrame
def mostrar_estadisticas_guardar_tabla(y_val, y_pred, set_name, model_name, print_roc='NO'):
    '''
    Ejemplo de uso :

    # Fase de entrenamiento
    results_df = mostrar_estadisticas_guardar_tabla(y_train, kmeans.predict(X_train_prep), "Training", results_df, model_name)

    # Fase de validación
    results_df = mostrar_estadisticas_guardar_tabla(y_val, kmeans.predict(X_val_prep), "Validation", results_df, model_name)

    # Fase de prueba
    results_df = mostrar_estadisticas_guardar_tabla(y_test, kmeans.predict(X_test_prep), "Test", results_df, model_name)

    # Importante: Al final de todos los modelos (fuera del método): Guardar los resultados en un archivo Excel
    results_df.to_excel('model_results.xlsx', index=False)

    '''
    global tabla_results_df
    accuracy = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred, average='weighted')
    recall = recall_score(y_val, y_pred, average='weighted')
    f1 = f1_score(y_val, y_pred, average='weighted')
    rand_index = adjusted_rand_score(y_val, y_pred)
    conf_matrix = confusion_matrix(y_val, y_pred)
    r2 = r2_score(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)
    fpr, tpr, _ = roc_curve(y_val, y_pred)
    # Calcular el área bajo la curva ROC (AUC)
    roc_auc = auc(fpr, tpr)

    if conf_matrix.shape == (2, 2):  # Asegúrate de que es una matriz de confusión 2x2
        tn, fp, fn, tp = conf_matrix.ravel()
    else:
        tn = fp = fn = tp = None  # Si no es una matriz 2x2, asigna valores None

    global_score = calcular_puntuacion_global(accuracy, precision, recall, f1, rand_index, r2, mse, tn, fp, fn, tp,
                                              roc_auc)

    # Imprimir todas las métricas
    print(f"Metrics for {set_name} set :")
    print(f" - Accuracy: {accuracy:.4f}")
    print(f" - Precision: {precision:.4f}")
    print(f" - Recall: {recall:.4f}")
    print(f" - F1-Score: {f1:.4f}")
    print(f" - Adjusted Rand Index: {rand_index:.4f}")
    print(f" - Mean Squared Error: {mse:.4f}")
    print(f" - R-squared: {r2:.4f}")
    print(f" - Área bajo la curva : {roc_auc:.3f}")
    print(f" - Confusion Matrix: \n{conf_matrix}")
    # if tn is not None and fp is not None and fn is not None and tp is not None:
    #   print(f"\tTN: {tn}\n\tFP: {fp}\n\tFN: {fn}\n\tTP: {tp}")
    print(f" - Global Score : {global_score}")
    print(f"")

    new_row = pd.DataFrame({
        'Model': [model_name],
        'Set': [set_name],
        'Accuracy': [accuracy],
        'Precision': [precision],
        'Recall': [recall],
        'F1-Score': [f1],
        'Adjusted Rand Index': [rand_index],
        'Mean Squared Error': [mse],
        'R-squared': [r2],
        'AUC-ROC': [roc_auc],
        'TN': [tn],
        'FP': [fp],
        'FN': [fn],
        'TP': [tp],
        'Global Score': [global_score]
    })

    if (print_roc == 'SI'):
        plot_ROC(fpr, tpr, roc_auc)

    tabla_results_df = pd.concat([tabla_results_df, new_row], ignore_index=True)

    return tabla_results_df

def mostrar_estadisticas_log(y_val, y_pred, set_name, mostrarEstadisticas=True) :
    global tabla_results_df
    accuracy = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred, average='weighted')
    recall = recall_score(y_val, y_pred, average='weighted')
    f1 = f1_score(y_val, y_pred, average='weighted')
    rand_index = adjusted_rand_score(y_val, y_pred)
    conf_matrix = confusion_matrix(y_val, y_pred)
    r2 = r2_score(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)
    fpr, tpr, _ = roc_curve(y_val, y_pred)
    # Calcular el área bajo la curva ROC (AUC)
    roc_auc = auc(fpr, tpr)

    if conf_matrix.shape == (2, 2):  # Asegúrate de que es una matriz de confusión 2x2
        tn, fp, fn, tp = conf_matrix.ravel()
    else:
        tn = fp = fn = tp = None  # Si no es una matriz 2x2, asigna valores None

    global_score = calcular_puntuacion_global(accuracy, precision, recall, f1, rand_index, r2, mse, tn, fp, fn, tp,
                                              roc_auc)
    if mostrarEstadisticas:
        # Imprimir todas las métricas
        print(f"Metrics for {set_name} set :")
        print(f" - Accuracy: {accuracy:.4f}")
        print(f" - Precision: {precision:.4f}")
        print(f" - Recall: {recall:.4f}")
        print(f" - F1-Score: {f1:.4f}")
        print(f" - Adjusted Rand Index: {rand_index:.4f}")
        print(f" - Mean Squared Error: {mse:.4f}")
        print(f" - R-squared: {r2:.4f}")
        print(f" - Área bajo la curva : {roc_auc:.3f}")
        print(f" - Confusion Matrix: \n{conf_matrix}")
        # if tn is not None and fp is not None and fn is not None and tp is not None:
        #   print(f"\tTN: {tn}\n\tFP: {fp}\n\tFN: {fn}\n\tTP: {tp}")
        print(f" - Global Score : {global_score}")
        print(f"")

    return global_score

def plot_ROC(fpr, tpr, roc_auc):
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='Curva ROC (AUC = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Tasa de Falsos Positivos')
    plt.ylabel('Tasa de Verdaderos Positivos')
    plt.title('Curva ROC')
    plt.legend(loc="lower right")
    plt.show()


def calcular_puntuacion_global(accuracy, precision, recall, f1, rand_index, r2, mse, tn, fp, fn, tp, auc_roc):
    # Definir ponderaciones para cada métrica
    weights = {
        'accuracy': 0.12,
        'precision': 0.12,
        'recall': 0.12,
        'f1': 0.12,
        'rand_index': 0.1,
        'r2': 0.05,
        'mse': 0.05,
        'tpr': 0.1,
        'fpr': 0.1,
        'auc_roc': 0.12,
    }

    # Normalizar las métricas
    mse_norm = (1 - mse)  # Invertir MSE ya que menor es mejor
    r2_norm = (r2 + 1) / 2  # Normalizar R2 para que esté entre 0 y 1

    # TPR y FPR
    tpr = recall  # TPR es lo mismo que recall
    fpr = fp / (fp + tn) if (fp + tn) != 0 else 0  # Asegurar no división por cero

    # Invertir FPR ya que menor es mejor
    fpr_inverted = 1 - fpr

    # Calcular la puntuación global
    global_score = (accuracy * weights['accuracy'] +
                    precision * weights['precision'] +
                    recall * weights['recall'] +
                    f1 * weights['f1'] +
                    rand_index * weights['rand_index'] +
                    r2_norm * weights['r2'] +
                    mse_norm * weights['mse'] +
                    tpr * weights['tpr'] +
                    fpr_inverted * weights['fpr'] +
                    auc_roc * weights['auc_roc'])

    return round(global_score * 100, 2)


# Funciones para aprendizaje no supervisado
def optimal_cluster_number(X_train, X_val, model, max_clusters=10, method='elbow', plot_grafica='NO'):
    """
    Encuentra el número óptimo de clusters para un modelo de clustering utilizando el método del codo (Elbow Method)
    u otros métodos.
    """
    if method == 'elbow':
        distortions = []
        for i in range(1, max_clusters + 1):
            model.n_clusters = i
            model.fit(X_train)
            distortions.append(model.inertia_)
        if plot_grafica == 'SI':
            # Plotting the elbow curve
            plt.plot(range(1, len(distortions) + 1), distortions, marker='o')
            plt.xlabel('Número de clusters')
            plt.ylabel('Distorsión')
            plt.title('Método del codo para encontrar el número óptimo de clusters')
            plt.show()

        # Finding the optimal number of clusters based on the elbow point
        optimal_k = np.argmin(np.gradient(distortions)) + 1
        if optimal_k == 1:  # Ensure that the optimal number of clusters is greater than 1
            optimal_k = 2
        return optimal_k

    elif method == 'silhouette':
        silhouette_scores = []
        for i in range(2, max_clusters + 1):
            model.n_clusters = i
            model.fit(X_train)
            labels = model.predict(X_val)
            silhouette_scores.append(silhouette_score(X_val, labels))

        if plot_grafica == 'SI':
            # Plotting the silhouette scores
            plt.plot(range(2, len(silhouette_scores) + 2), silhouette_scores, marker='o')
            plt.xlabel('Número de clusters')
            plt.ylabel('Silhouette Score')
            plt.title('Silhouette Score para encontrar el número óptimo de clusters')
            plt.show()

        # Finding the optimal number of clusters based on silhouette score
        optimal_k = np.argmax(silhouette_scores) + 2
        return optimal_k

    else:
        raise ValueError("Método no válido. Métodos disponibles: 'elbow', 'silhouette', etc.")


# Función para motrar estadísticas para modelos de aprendizaje no supervisado
def mostrar_estadisticas_guardar_tabla_NS(X, labels, set_name, model_name):
    '''
    Ejemplo de uso :

    # Fase de entrenamiento
    results_df = mostrar_estadisticas_guardar_tabla(X_train, kmeans.predict(X_train), "Training", model_name, results_df)

    # Fase de validación
    results_df = mostrar_estadisticas_guardar_tabla(X_val, kmeans.predict(X_val), "Validation", model_name, results_df)

    # Fase de prueba
    results_df = mostrar_estadisticas_guardar_tabla(X_test, kmeans.predict(X_test), "Test", model_name, results_df)

    # Importante: Al final de todos los modelos (fuera del método): Guardar los resultados en un archivo Excel
    results_df.to_excel('model_results.xlsx', index=False)
    '''
    global tabla_results_NS_df
    silhouette_avg = silhouette_score(X, labels)
    db_score = davies_bouldin_score(X, labels)
    ch_score = calinski_harabasz_score(X, labels)

    global_score = calcular_puntuacion_global_NS(silhouette_avg, db_score, ch_score)

    # Imprimir todas las métricas
    print(f"Metrics for {set_name} set ({model_name}):")
    print(f" - Silhouette Score: {silhouette_avg:.4f}")
    print(f" - Davies-Bouldin Index: {db_score:.4f}")
    print(f" - Calinski-Harabasz Index: {ch_score:.4f}")
    print(f" - Global Score: {global_score:.4f}")
    print(f"")

    new_row = pd.DataFrame({
        'Model': [model_name],
        'Set': [set_name],
        'Silhouette Score': [silhouette_avg],
        'Davies-Bouldin Index': [db_score],
        'Calinski-Harabasz Index': [ch_score],
        'Global Score': [global_score]
    })

    tabla_results_NS_df = pd.concat([tabla_results_NS_df, new_row], ignore_index=True)

    return tabla_results_NS_df


def calcular_puntuacion_global_NS(silhouette_avg, db_score, ch_score):
    # Normalizando los valores para que estén en el rango de 0 a 100
    normalized_silhouette = (silhouette_avg + 1) * 50  # Ajustando el rango del Silhouette Score de -1 a 1 a 0 a 100
    normalized_davies_bouldin = (1 - db_score) * 50  # Ajustando el rango del Davies-Bouldin Index de 0 a 1 a 0 a 100

    # Calculando el puntaje global promediando los puntajes normalizados
    global_score = (normalized_silhouette + normalized_davies_bouldin + ch_score) / 3

    return global_score


def encontrar_numero_optimo_clusters(X_train, X_val, model, max_clusters=10, plot_grafica='NO'):
    wcss = []
    silhouette_scores = []
    davies_bouldin_scores = []
    calinski_harabasz_scores = []
    global_scores = []

    for i in range(2, max_clusters + 1):
        model.n_clusters = i
        model.fit(X_train)

        # Predecir las etiquetas para los datos de validación
        labels = model.predict(X_val)

        # Calcular las métricas
        silhouette = silhouette_score(X_val, labels)
        davies_bouldin = davies_bouldin_score(X_val, labels)
        calinski_harabasz = calinski_harabasz_score(X_val, labels)

        global_score = calcular_puntuacion_global_NS(silhouette, davies_bouldin, calinski_harabasz)

        wcss.append(model.inertia_)
        silhouette_scores.append(silhouette)
        davies_bouldin_scores.append(davies_bouldin)
        calinski_harabasz_scores.append(calinski_harabasz)
        global_scores.append(global_score)

    if plot_grafica == 'SI':
        # Plot para el método del codo
        plt.figure(figsize=(12, 8))
        plt.plot(range(2, max_clusters + 1), wcss, marker='o')
        plt.title('Método del Codo')
        plt.xlabel('Número de Clústeres')
        plt.ylabel('WCSS')
        plt.show()

        # Plot para las métricas de validación
        plt.figure(figsize=(12, 8))
        plt.plot(range(2, max_clusters + 1), silhouette_scores, marker='o', label='Silhouette Score')
        plt.plot(range(2, max_clusters + 1), davies_bouldin_scores, marker='o', label='Davies-Bouldin Index')
        plt.plot(range(2, max_clusters + 1), calinski_harabasz_scores, marker='o', label='Calinski-Harabasz Index')
        plt.plot(range(2, max_clusters + 1), global_scores, marker='o', label='Global Score')
        plt.title('Métricas de Validación para Diferentes Números de Clústeres')
        plt.xlabel('Número de Clústeres')
        plt.ylabel('Valor de la Métrica')
        plt.legend()
        plt.show()

    # Encontrar el número óptimo de clústeres basado en el puntaje global
    numero_optimo_clusters = range(2, max_clusters + 1)[np.argmax(global_scores)]
    return numero_optimo_clusters

def process_data(split = True, process_data = True, df_sample = None):
    # Carga de la URL de donde se encuentran los datos
    # (I) Introducir valor de nombreArchivo y variar la ruta en local donde se guardan los datos
    nombreArchivo = 'Tables_S1_to_S11'  # nombre del archivo del dataset
    url_datos = f'C:/Users/danie/OneDrive/Documentos/Master/Lusku/TFM/Proposiciones/Deteccion Cancer/Datos/{nombreArchivo}.xlsx'

    # Se procede a hacer una carga de los datos.
    df_original = pd.read_excel(url_datos, sheet_name='Table S6')

    # Crear una copia del DataFrame original para realizar los cambios
    df6 = df_original.copy()

    # Recorrer las columnas del DataFrame para eliminar las cadenas de texto : ['*', '**']
    for columna in df6.columns:
        if df6[columna].dtype == 'object':
            # Aplicar la sustitución para cada secuencia en secuencias_a_buscar
            for secuencia in ['*', '**']:
                df6[columna] = df6[columna].apply(
                    lambda x: x.replace(secuencia, '') if isinstance(x, str) and secuencia in x else x)

    df_prep = df6.apply(convert_to_numeric)

    # Relleno de nulos de la variable "AJCC Stage"
    df_prep["AJCC Stage"] = df_prep["AJCC Stage"].fillna("0")

    # Calcular la media solo para las columnas numéricas
    numeric_columns = df_prep.select_dtypes(include=['number'])
    mean_values = numeric_columns.mean()

    # Rellenar los valores nulos con la media correspondiente
    df = df_prep.copy()  # Copiar el DataFrame preprocesado para evitar modificarlo
    for col in mean_values.index:
        df[col].fillna(mean_values[col], inplace=True)

    # Binarización "Tumor Type" 0 -> NO CANCER; 1 -> SI CANCER + 'CancerSEEK Test Result'
    df['Tumor type'] = df['Tumor type'].apply(lambda x: 0 if str(x).strip().lower() == "normal" else 1).astype(int)
    # df['CancerSEEK Test Result'] = df['CancerSEEK Test Result'].apply(lambda x: 0 if str(x).strip().lower() == "negative" else 1).astype(int)

    # Conservar solo las columnas 'CA19-9 (U/ml)', 'CA-125 (U/ml)','HGF (pg/ml)','OPN (pg/ml)', 'Omega score', 'Prolactin (pg/ml)', 'CEA (pg/ml)', 'Myeloperoxidase (ng/ml)', 'TIMP-1 (pg/ml)'
    columnas_a_conservar = ['Tumor type', 'CA19-9 (U/ml)', 'CA-125 (U/ml)', 'HGF (pg/ml)', 'OPN (pg/ml)', 'Omega score',
                            'Prolactin (pg/ml)', 'CEA (pg/ml)', 'Myeloperoxidase (ng/ml)', 'TIMP-1 (pg/ml)']

    ## --- CHECKPOINT ----- Datos limpios

    # Columna objetivo
    Y_column = df['Tumor type'].copy()
    # Reducción del dataFrame
    df_reduced = df[columnas_a_conservar].copy()
    # Copia del dataFrame entero
    df_full = df.copy()

    ''' INICIO - Verificacion del information gain'''
    # Information Gain inicial
    df_discretizado = discretizar_df_arboles_1(df_reduced.drop(columns=['Tumor type']))
    df_reduced_discretizado_escalated = escalado_dataFrame(df_discretizado)
    calcular_ganancia_informacion(df_reduced_discretizado_escalated, Y_column, imprimir="NO")

    # Information Gain usando arboles de decision (acorde a : "..the cancer antigen markers are no longer the top predictive features. Instead, we observe the opposite trend for the purity and accuracy measurements..")
    df_discretizado_full = discretizar_df_arboles(df_full,
                                                  imprimir="NO")  # Columnas de este segundo enfoque guardadas en columnas_segundo_enfoque
    df_discretizado_reduced = discretizar_df_arboles(df_reduced, imprimir="NO")

    ''' FIN - Verificacion del information gain'''

    # Crear un DataFrame para almacenar los resultados en una tabla para luego poder compararlos - APRENDIZAJE SUPERVISADO
    tabla_results_df = pd.DataFrame(
        columns=['Model', 'Set', 'Accuracy', 'Precision', 'Recall', 'F1-Score', 'Adjusted Rand Index',
                 'Mean Squared Error', 'R-squared', 'AUC-ROC', 'TN', 'FP', 'FN', 'TP', 'Global Score'])

    # Crear un DataFrame para almacenar los resultados en una tabla para luego poder compararlos - APRENDIZAJE NO SUPERVISADO
    tabla_results_NS_df = pd.DataFrame(
        columns=['Model', 'Set', 'Silhouette Score', 'Davies-Bouldin Index', 'Calinski-Harabasz Index', 'Global Score'])

    ## --- CHECKPOINT ----- Datos discretizados + Information gain
    # TODO Una vez hechos los modelos, habrá que estudiar cómo influye el usar esta serie de variables en la predicción
    columnas_segundo_enfoque = ['Tumor type', 'OPN (pg/ml)', 'IL-6 (pg/ml)', 'IL-8 (pg/ml)', 'HGF (pg/ml)',
                                'Prolactin (pg/ml)', 'Omega score', 'GDF15 (ng/ml)', 'CYFRA 21-1 (pg/ml)',
                                'Myeloperoxidase (ng/ml)']
    df_reduced_segundo_enfoque = df[columnas_segundo_enfoque].copy()

    ''' Valores para X
    1. df : entero, limpio, sin normalizar ni discretizar
    2. df_reduced : reducido, limpio, sin normalizar ni discretizar
    3. df_reduced_discretizado_escalated --> Acorde a la Tabla 1
    4. df_discretizado_full.drop(columns=['Tumor type']) --> Acorde a la Figura S3 (usando todas las variables) discretizado con arbol de decisión
    5. df_discretizado_reduced.drop(columns=['Tumor type']) --> Acorde a la Figura S3; discretizado con arbol de decisión
    '''
    y = df_reduced_segundo_enfoque['Tumor type']
    X = df_reduced_segundo_enfoque.drop(columns='Tumor type')
    if process_data == True:
        if split == True :
            X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y, train_size=0.6, val_size=0.2, test_size=0.2,
                                                                        random_state=42)

            numeric_cols = X_train.select_dtypes(include=['float64', 'int']).columns.to_list()
            cat_cols = X_train.select_dtypes(include=['object', 'category']).columns.to_list()

            # Crear el discretizado
            numeric_pipeline = Pipeline(steps=[
                ('scale', StandardScaler()),
                ('discretize',
                 DecisionTreeDiscretiser(cv=5, scoring='accuracy', variables=numeric_cols, regression=False))
            ])

            # Crear el preprocesador
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numeric_pipeline, numeric_cols),
                    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)
                ],
                remainder='passthrough',
                verbose_feature_names_out=False
            ).set_output(transform="pandas")

            X_train_prep = preprocessor.fit_transform(X_train,y_train)
            X_val_prep = preprocessor.transform(X_val)
            X_test_prep = preprocessor.transform(X_test)

            if df_sample is not None and not df.empty:
                df_sample_prep = preprocessor.transform(df_sample)
                return df_sample_prep
            X_prep = np.vstack((X_train_prep, X_val_prep, X_test_prep))

            return X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test
        else :
            numeric_columns = df_reduced.select_dtypes(include=['number']).columns.to_list()
            categorical_columns = df_reduced.select_dtypes(include=['object', 'category']).columns.to_list()
            preprocessor = ColumnTransformer(
                [('scale', StandardScaler(), numeric_columns),
                 ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_columns)],
                remainder='passthrough',
                verbose_feature_names_out=False).set_output(transform="pandas")

            df_reduced = preprocessor.fit_transform(df_reduced)
            return df_reduced
    else :
            return df_reduced

def get_preprocessor(df) :
    numeric_features = const.Constantes.important_features

    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features)
        ],
        remainder='passthrough'
    )
    return preprocessor


def process_data_cancer_type(df):
    model_name = 'preprocessor.joblib'
    model_path = os.path.join(functions.get_path(), model_name)
    print(f"Model Path: {model_path}")  # Imprime la ruta del modelo para verificar

    try:
        preprocessor = functions.load_model('C:/Users/danie/OneDrive/Documentos/Master/Lusku/TFM/Repositorio compartido/kschool_master/Modelos supervisados entrenados/preprocessor.joblib')
        if preprocessor is None:
            raise ValueError(
                "El preprocesador no se pudo cargar correctamente. Verifica la ruta y el archivo del modelo.")
        return preprocessor.transform(df)
    except ImportError as e:
        print(f"Error al importar un módulo necesario para cargar el modelo: {e}")
        raise
    except Exception as e:
        print(f"Error al cargar o aplicar el preprocesador: {e}")
        raise


def preprocess_data(df) :
    numeric_columns = df.select_dtypes(include=['number']).columns.to_list()
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.to_list()

    preprocessor = ColumnTransformer(
        [('scale', StandardScaler(), numeric_columns),
         ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_columns)],
        remainder='passthrough',
        verbose_feature_names_out=False).set_output(transform="pandas")

    df_reduced = preprocessor.fit_transform(df)

def invert_preprocessor(data_prep):
    numeric_cols = data_prep.select_dtypes(include=['float64', 'int']).columns.to_list()
    cat_cols = data_prep.select_dtypes(include=['object', 'category']).columns.to_list()

    preprocessor = ColumnTransformer(
        [('scale', StandardScaler(), numeric_cols),
         ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols)],
        remainder='passthrough',
        verbose_feature_names_out=False
    ).set_output(transform="pandas")

    # Invertir la transformación para los datos numéricos
    scaler = preprocessor.named_transformers_['scale']
    numeric_data_transformed = data_prep[numeric_cols]
    original_numeric_data = scaler.inverse_transform(numeric_data_transformed)

    # Invertir la transformación para los datos categóricos
    onehot = preprocessor.named_transformers_['onehot']
    encoded_columns = onehot.get_feature_names_out(cat_cols)
    categorical_data_transformed = data_prep[encoded_columns]
    original_categorical_data = onehot.inverse_transform(categorical_data_transformed)

    # Combinar las columnas invertidas con las columnas restantes
    original_data = pd.DataFrame(original_numeric_data, columns=numeric_cols)
    for i, col in enumerate(cat_cols):
        original_data[col] = original_categorical_data[:, i]

    # Combinar las columnas originales si hay columnas que se pasaron sin transformar (remainder='passthrough')
    if preprocessor.remainder == 'passthrough':
        passthrough_cols = data_prep.columns.difference(numeric_cols + list(encoded_columns))
        passthrough_data = data_prep[passthrough_cols]
        original_data = pd.concat([original_data, passthrough_data.reset_index(drop=True)], axis=1)

    return original_data

def get_path() :
    # Construir el path para el modelo
    current_directory = os.path.dirname(__file__)  # Directorio actual del script Functions.py
    return os.path.join(os.path.dirname(current_directory), 'Modelos supervisados entrenados')
def load_model_with_pickle(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def load_model(model_path):
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

def check_limitis(value,min,max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value

class CTGANTrainer:
    def __init__(self, param_grid, model_path, pac=1):
        self.param_grid = param_grid
        self.model_path = model_path
        self.pac = pac

    def evaluate_ctgan(self, params, X):
        # Ajustar los parámetros de CTGAN
        params['pac'] = self.pac
        model = CTGAN(**params)
        model.fit(X)

        # Generar una muestra sintética
        synthetic_data = model.sample(len(X))

        return synthetic_data

    def grid_search(self, X):
        # Realizar la búsqueda de hiperparámetros
        best_score = -np.inf
        best_params = None

        for params in ParameterGrid(self.param_grid):
            synthetic_data = self.evaluate_ctgan(params, X)
            score = self.calculate_score(X, synthetic_data)
            if score > best_score:
                best_score = score
                best_params = params

        return best_params

    def calculate_score(self, real_data, synthetic_data):
        # Aquí puedes implementar la métrica de evaluación que desees
        # En este caso, se puede comparar alguna métrica entre los datos reales y sintéticos
        return 0  # Ejemplo simplificado, implementa tu métrica adecuada aquí

    def train_and_save(self, df):
        # Convertir numpy array de vuelta a DataFrame si es necesario
        if isinstance(df, np.ndarray):
            df = pd.DataFrame(df, columns=self.feature_names)

        # Ajustar el preprocesador si es necesario
        # Asumiendo que ya tienes preprocesado tu dataframe

        # Separar características (X)
        X = df

        # Buscar los mejores hiperparámetros
        best_params = self.grid_search(X)
        print(f"Best parameters found: {best_params}")

        # Entrenar el modelo CTGAN con los mejores hiperparámetros
        best_params['pac'] = self.pac  # Asegurar que 'pac' esté en los mejores parámetros
        model = CTGAN(**best_params)
        model.fit(X)

        # Guardar el modelo entrenado
        joblib.dump(model, self.model_path)

    def load_model(self):
        # Cargar el modelo entrenado
        return joblib.load(self.model_path)

    def generate_sample(self, model, num_samples=1):
        # Generar datos sintéticos
        return model.sample(num_samples)


class CTGAN2:
    def __init__(self, param_grid, model_path, pac=1):
        self.param_grid = param_grid
        self.model_path = model_path
        self.pac = pac
    def train(self):
        # Cargar datos de entrenamiento y prueba
        train_data = pd.read_excel(self.config.train_data_path)
        test_data = pd.read_excel(self.config.test_data_path)

        # Combinar datos de entrenamiento y prueba
        df_combined = pd.concat([train_data, test_data], axis=0)

        # Seleccionar características importantes
        X_real = df_combined[self.config.important_features]
        y_real = df_combined[self.config.target_column]

        # Identificar clases minoritarias
        class_counts = y_real.value_counts()
        minority_classes = class_counts[class_counts < class_counts.median()].index

        # Separar datos de clases minoritarias
        X_minority = X_real[y_real.isin(minority_classes)]
        y_minority = y_real[y_real.isin(minority_classes)]

        # Entrenar el modelo CTGAN solo con las clases minoritarias
        ctgan_params = self.params['CTGAN']
        model = CTGAN(**ctgan_params)
        model.fit(X_minority)

    def load_model(self):
        # Cargar el modelo entrenado
        return joblib.load(self.model_path)

    def generate_sample(self, model, num_samples=1):
        # Generar datos sintéticos
        return model.sample(num_samples)

