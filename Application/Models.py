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
def RegressionLogistica():
    print("En proceso")