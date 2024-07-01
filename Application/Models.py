import statistics

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import skew, kurtosis
from scipy.stats import shapiro
from scipy.stats import normaltest

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import mutual_info_classif

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, roc_curve, auc, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, adjusted_rand_score, r2_score, silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import Functions as fn

def RegressionLineal(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df):
    # Crear una instancia del modelo de regresión lineal
    model_LR = LinearRegression()
    model_name = "Regresion Lineal"

    # Definir un umbral
    umbral = 0.5

    # Cross validation
    fn.mostrar_cross_validation(model_LR, X_train_prep, y_train)

    # Entrenar el modelo usando los datos de entrenamiento preprocesados
    model_LR.fit(X_train_prep, y_train)
    y_train_pred = model_LR.predict(X_train_prep)
    y_train_pred_bin = np.where(y_train_pred > umbral, 1, 0)

    y_val_pred = model_LR.predict(X_val_prep)
    y_val_pred_bin = np.where(y_val_pred > umbral, 1, 0)

    # Predicciones
    y_test_pred = model_LR.predict(X_test_prep)
    y_test_pred_bin = np.where(y_test_pred > umbral, 1, 0)

    # Predecir con datos introducidos por el usuario
    y_prod = model_LR.predict(df)
    y_prod_bin = np.where(y_prod > umbral, 1, 0)

    gb_train = fn.mostrar_estadisticas_log(y_train, y_train_pred_bin, "Training")
    gb_val = fn.mostrar_estadisticas_log(y_val, y_val_pred_bin, "Validation")
    gb_test = fn.mostrar_estadisticas_log(y_test, y_test_pred_bin, "Test")

    return y_prod_bin, statistics.mean([gb_train, gb_val, gb_test])
def RegresionLogistica(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df):
    from sklearn.linear_model import LogisticRegression
    model_name = "Regresión Logística"
    print(model_name)
    # Crear una instancia del modelo de regresión logística
    model_LogR = LogisticRegression()

    # Entrenar el modelo usando los datos de entrenamiento preprocesados
    model_LogR.fit(X_train_prep, y_train)

    y_train_pred = model_LogR.predict(X_train_prep)
    y_val_pred = model_LogR.predict(X_val_prep)
    y_test_pred = model_LogR.predict(X_test_prep)

    gb_train = fn.mostrar_estadisticas_log(y_train, y_train_pred, "Training")
    gb_val = fn.mostrar_estadisticas_log(y_val, y_val_pred, "Validation")
    gb_test = fn.mostrar_estadisticas_log(y_test, y_test_pred, "Test")

    y_prod = model_LogR.predict(df)

    return y_prod, statistics.mean([gb_train, gb_val, gb_test])

def AdaBoost(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df):
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import GridSearchCV

    model_name = "AdaBoost"
    print(model_name)

    # Inicializar el clasificador débil (stump)
    base_estimator = DecisionTreeClassifier(max_depth=2)

    # Configurar la búsqueda de hiperparámetros
    param_grid = {
        'n_estimators': [50, 100, 200, 250, 300],
        'learning_rate': [0.01, 0.05, 0.07, 0.10, 0.5, 1.0]
    }

    # Inicializar el modelo AdaBoost
    ada = AdaBoostClassifier(estimator=base_estimator, n_estimators=50, learning_rate=1.0, random_state=42)

    grid_search = GridSearchCV(estimator=ada, param_grid=param_grid, cv=5, n_jobs=-1, scoring='accuracy')

    # Entrenar el modelo con búsqueda de hiperparámetros
    grid_search.fit(X_train_prep, y_train)

    # Obtener los mejores hiperparámetros
    best_params = grid_search.best_params_
    print(f"Mejores hiperparámetros: {best_params}")

    # Mejor modelo
    best_model = grid_search.best_estimator_

    # Cross validation
    # TODO mostrar_cross_validation(best_model, X_train_prep, y_train)

    # Entrenar el modelo usando los datos de entrenamiento preprocesados
    best_model.fit(X_train_prep, y_train)

    y_train_pred = best_model.predict(X_train_prep)
    y_val_pred = best_model.predict(X_val_prep)
    y_test_pred = best_model.predict(X_test_prep)

    gb_train = fn.mostrar_estadisticas_log(y_train, y_train_pred, "Training")
    gb_val = fn.mostrar_estadisticas_log(y_val, y_val_pred, "Validation")
    gb_test = fn.mostrar_estadisticas_log(y_test, y_test_pred, "Test")

    y_prod = best_model.predict(df)

    return y_prod, statistics.mean([gb_train, gb_val, gb_test])


def randomForest(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df):
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.ensemble import RandomForestClassifier
    model_name = "Random Forest"
    print(model_name)
    RF = RandomForestClassifier()

    rf_params = {
        "n_estimators": [100, 200, 300, 400, 500],
        "max_depth": [None, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        "max_features": [None, "sqrt", "log2"],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "bootstrap": [True, False]
    }

    random_search = RandomizedSearchCV(estimator=RF,
                                       param_distributions=rf_params,
                                       n_iter=100,
                                       cv=5,
                                       verbose=0,
                                       random_state=42,
                                       n_jobs=-1)

    random_search.fit(X_train_prep, y_train)

    print("Mejores parámetros encontrados:", random_search.best_params_)

    model_RF = random_search.best_estimator_

    model_RF.fit(X_train_prep, y_train)

    # Cross validation
    # TODO mostrar_cross_validation(model_RF, X_train_prep, y_train)

    y_train_pred = model_RF.predict(X_train_prep)
    y_val_pred = model_RF.predict(X_val_prep)
    y_test_pred = model_RF.predict(X_test_prep)

    gb_train = fn.mostrar_estadisticas_log(y_train, y_train_pred, "Training")
    gb_val = fn.mostrar_estadisticas_log(y_val, y_val_pred, "Validation")
    gb_test = fn.mostrar_estadisticas_log(y_test, y_test_pred, "Test")

    y_prod = model_RF.predict(df)

    return y_prod, statistics.mean([gb_train, gb_val, gb_test])

def gradientBoost(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df):
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.model_selection import GridSearchCV

    model_name = "Gradient Boosting"
    print(model_name)

    # Configurar la búsqueda de hiperparámetros
    param_grid = {
        'n_estimators': [50, 100, 200, 250, 300],
        'learning_rate': [0.01, 0.05, 0.07, 0.10, 0.5, 1.0],
        'max_depth': [3, 4, 5],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    # Inicializar el modelo AdaBoost
    GradBoost = GradientBoostingClassifier(n_estimators=50, learning_rate=1.0, random_state=42)

    grid_search = GridSearchCV(estimator=GradBoost, param_grid=param_grid, cv=5, n_jobs=-1, scoring='accuracy')

    # Entrenar el modelo con búsqueda de hiperparámetros
    grid_search.fit(X_train_prep, y_train)

    # Obtener los mejores hiperparámetros
    best_params = grid_search.best_params_
    print(f"Mejores hiperparámetros: {best_params}")

    # Mejor modelo
    best_model = grid_search.best_estimator_

    # Cross validation
    # TODO mostrar_cross_validation(best_model, X_train_prep, y_train)

    # Entrenar el modelo usando los datos de entrenamiento preprocesados
    best_model.fit(X_train_prep, y_train)

    y_train_pred = best_model.predict(X_train_prep)
    y_val_pred = best_model.predict(X_val_prep)
    y_test_pred = best_model.predict(X_test_prep)

    gb_train = fn.mostrar_estadisticas_log(y_train, y_train_pred, "Training")
    gb_val = fn.mostrar_estadisticas_log(y_val, y_val_pred, "Validation")
    gb_test = fn.mostrar_estadisticas_log(y_test, y_test_pred, "Test")

    y_prod = best_model.predict(df)

    return y_prod, statistics.mean([gb_train, gb_val, gb_test])