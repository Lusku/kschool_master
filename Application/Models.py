import os
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
import pickle
import joblib


def RegressionLineal(df):
    """
    Load a pre-trained Linear Regression model and use it to make predictions on the provided DataFrame.

    Parameters:
    df (pd.DataFrame): The input data on which predictions are to be made.

    Returns:
    tuple: A tuple containing:
        - y_pred (np.ndarray): The predicted values.
        - prob (np.ndarray or None): The predicted probabilities if the model supports it, otherwise None.
    """
    model_name = 'regresionLineal_e2_1.joblib'
    model_path = os.path.join(fn.get_path(), model_name)

    # Load the model with joblib
    model = fn.load_model(model_path)

    print(model)
    if model is None:
        return None, None

    # Make predictions with the loaded model
    try:
        y_pred = model.predict(df)
        if hasattr(model, 'predict_proba'):
            prob = model.predict_proba(df)[:, 1]
        elif hasattr(model, 'decision_function'):
            prob = model.decision_function(df)
            prob = 1 / (1 + np.exp(-prob))  # Convertir las puntuaciones de decisión a probabilidades
        else:
            prob = None
    except AttributeError as e:
        print(f"Error al hacer predicción: {e}")
        return None, None

    return y_pred, prob


def RegressionLogistica(df):
    """
    Load a pre-trained Logistic Regression model and use it to make predictions on the provided DataFrame.

    Parameters:
    df (pd.DataFrame): The input data on which predictions are to be made.

    Returns:
    tuple: A tuple containing:
        - y_pred (np.ndarray): The predicted values.
        - prob (np.ndarray or None): The predicted probabilities if the model supports it, otherwise None.
    """
    model_name = 'regresionLogistica_e2_2.joblib'
    model_path = os.path.join(fn.get_path(), model_name)

    # Cargar el modelo con joblib
    model = fn.load_model(model_path)

    print(model)
    if model is None:
        return None, None

    # Realizar predicción con el modelo cargado
    try:
        y_pred = model.predict(df)
        prob = model.predict_proba(df)[:, 1] if hasattr(model, 'predict_proba') else None
    except AttributeError as e:
        print(f"Error al hacer predicción: {e}")
        return None, None

    return y_pred, prob


def RandomForest(df):
    """
    Load a pre-trained Random Forest model and use it to make predictions on the provided DataFrame.

    Parameters:
    df (pd.DataFrame): The input data on which predictions are to be made.

    Returns:
    tuple: A tuple containing:
        - y_pred (np.ndarray): The predicted values.
        - prob (np.ndarray or None): The predicted probabilities if the model supports it, otherwise None.
    """
    model_name = 'randomForest_e2_2.joblib'
    model_path = os.path.join(fn.get_path(), model_name)

    # Load the model with joblib
    model = fn.load_model(model_path)

    print(model)
    if model is None:
        return None, None

    # Make predictions with the loaded model
    try:
        y_pred = model.predict(df)
        prob = model.predict_proba(df)[:, 1] if hasattr(model, 'predict_proba') else None
    except AttributeError as e:
        print(f"Error al hacer predicción: {e}")
        return None, None

    return y_pred, prob


def KNN(df):
    """
    Load a pre-trained K-Nearest Neighbors (KNN) model and use it to make predictions on the provided DataFrame.

    Parameters:
    df (pd.DataFrame): The input data on which predictions are to be made.

    Returns:
    tuple: A tuple containing:
        - y_pred (np.ndarray): The predicted values.
        - prob (np.ndarray or None): The predicted probabilities if the model supports it, otherwise None.
    """
    model_name = 'knn_e2_2.joblib'
    model_path = os.path.join(fn.get_path(), model_name)

    # Load the model with joblib
    model = fn.load_model(model_path)

    print(model)
    if model is None:
        return None, None

    # Make predictions with the loaded model
    try:
        y_pred = model.predict(df)
        prob = model.predict_proba(df)[:, 1] if hasattr(model, 'predict_proba') else None
    except AttributeError as e:
        print(f"Error al hacer predicción: {e}")
        return None, None

    return y_pred, prob

def AdaBoost(df):
    """
    Load pre-trained AdaBoost models and use them to make predictions on the provided DataFrame.

    Parameters:
    df (pd.DataFrame): The input data on which predictions are to be made.

    Returns:
    tuple: A tuple containing:
        - y_pred (np.ndarray): The predicted values.
        - prob (np.ndarray or None): The predicted probabilities if the model supports it, otherwise None.
    """
    model_name = 'adaBoost_e2_2.joblib'
    model_path = os.path.join(fn.get_path(), model_name)

    # Load the first AdaBoost model with joblib
    model_adaboost = fn.load_model(model_path)

    print(model_adaboost)
    if model_adaboost is None:
        return None, None

    # Make predictions with the loaded model
    try:
        y_pred = model_adaboost.predict(df)
        prob = model_adaboost.predict_proba(df)[:, 1] if hasattr(model_adaboost, 'predict_proba') else None
    except AttributeError as e:
        print(f"Error al hacer predicción: {e}")
        return None, None

    return y_pred, prob

def GradientBoosting(df):
    model_name = 'gradientBoosting_e2_2.joblib'
    model_path = os.path.join(fn.get_path(), model_name)

    # Cargar el modelo con joblib
    model = fn.load_model(model_path)

    print(model)
    if model is None:
        return None, None

    # Realizar predicción con el modelo cargado
    try:
        y_pred = model.predict(df)
        prob = model.predict_proba(df)[:, 1] if hasattr(model, 'predict_proba') else None
    except AttributeError as e:
        print(f"Error al hacer predicción: {e}")
        return None, None

    return y_pred, prob


def VotingClassifier_1(df):
    model_name = 'voting_clf_e2_1.joblib'
    model_path = os.path.join(fn.get_path(), model_name)

    # Cargar el modelo con joblib
    model = fn.load_model(model_path)

    print(model)
    if model is None:
        return None, None

    # Realizar predicción con el modelo cargado
    try:
        y_pred = model.predict(df)
        prob = model.predict_proba(df)[:, 1] if hasattr(model, 'predict_proba') else None
    except AttributeError as e:
        print(f"Error al hacer predicción: {e}")
        return None, None

    return y_pred, prob


def VotingClassifier_2(df):
    model_name = 'voting_clf.joblib'
    model_path = os.path.join(fn.get_path(), model_name)

    # Cargar el modelo con joblib
    model = fn.load_model(model_path)

    if model is None:
        return None, None

    # Realizar predicción con el modelo cargado
    try:
        y_pred = model.predict(df)
        prob = model.predict_proba(df)[:, 1] if hasattr(model, 'predict_proba') else None
    except AttributeError as e:
        print(f"Error al hacer predicción: {e}")
        return None, None

    return y_pred, prob