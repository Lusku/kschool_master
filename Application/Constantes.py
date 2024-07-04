import os

class Constantes:
    REGRESION_LINEAL = 'Regresión Lineal'
    REGRESION_LOGISTICA = 'Regresión Logística'
    ADABOOST = 'AdaBoost'
    RANDOM_FOREST = 'Random Forest'
    GRADIENT_BOOSTING = 'Gradient Boosting'
    KNN = 'KNN'
    VOTING_CLASSIFIER_1 = 'Voting Classifier 1'
    VOTING_CLASSIFIER_2 = 'Voting Classifier 2'

    rf_params = {
        'n_estimators': 100,
        'max_depth': 5
    }
    gb_params = {
        'n_estimators': 100,
        'learning_rate': 0.06,
        'max_depth': 3
    }

    lgb_params = {
        'n_estimators': 100,
        'learning_rate': 0.06,
        'num_leaves': 31
    }

    xgb_params = {
        'n_estimators': 100,
        'learning_rate': 0.06,
        'max_depth': 3
    }

    ctgan_params = {
        'epochs': 200,
        'batch_size': 500,
        'discriminator_steps': 1,
        'log_frequency': True,
        'verbose': True
    }

    important_features = [
        'sFas (pg/ml)',
        'sHER2/sEGFR2/sErbB2 (pg/ml)',
        'CA 15-3 (U/ml)',
        'CA19-9 (U/ml)',
        'CA-125 (U/ml)',
        'TIMP-2 (pg/ml)',
        'TGFa (pg/ml)',
        'Leptin (pg/ml)',
        'IL-8 (pg/ml)',
        'IL-6 (pg/ml)',
        'AFP (pg/ml)',
        'GDF15 (ng/ml)',
        'Prolactin (pg/ml)',
        'HGF (pg/ml)',
        'CD44 (ng/ml)',
        'Midkine (pg/ml)',
        'Thrombospondin-2 (pg/ml)',
        'TIMP-1 (pg/ml)',
        'HE4 (pg/ml)'
    ]

    param_grid = {
        'epochs': 200,
        'batch_size': 500,
        'discriminator_steps': 1,
        'verbose': [False]
    }
    current_directory = os.path.dirname(__file__)  # Directorio actual del script Functions.py
    desired_model_directory = os.path.join(os.path.dirname(current_directory), 'Modelo CTGAN')
    model_path = os.path.join(desired_model_directory, 'ctgan_model.pkl')

    desired_model_directory_2 = os.path.join(os.path.dirname(current_directory), 'Modelo CTGAN')
    model_path_2 = os.path.join(desired_model_directory, 'ctgan_model_2.pkl')
