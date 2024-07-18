import os
from tkinter import messagebox
from tkinter import ttk

import joblib
from PIL import Image, ImageTk
import tkinter as tk
import random
import pandas as pd
import Models as md
import Functions as fn
import Constantes as const

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación para detección de cáncer")

        trainer = fn.CTGANTrainer(const.Constantes.param_grid, const.Constantes.model_path, pac=1)
        trainer2 = fn.CTGAN2(const.Constantes.param_grid, const.Constantes.model_path_2, pac=1)
        self.ctgan_model = trainer.load_model()
        self.ctgan_model_2 = trainer2.load_model()

        # Crear el Notebook para las pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Crear el marco para la primera pestaña
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Predicción de cáncer")

        # Crear el marco para la segunda pestaña
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Predicción del tipo de cáncer")

        # Crear el marco superior para el botón de información
        top_frame = ttk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        # Cargar la imagen del icono de información y redimensionarla
        original_image = Image.open("info_icon.png")
        resized_image = original_image.resize((30, 30), Image.LANCZOS)
        self.info_icon = ImageTk.PhotoImage(resized_image)

        # Crear el botón de información y colocarlo en la esquina superior derecha
        info_button = ttk.Button(top_frame, image=self.info_icon, compound='center', command=self.show_info)
        info_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Variables y sus valores predefinidos para la primera pestaña
        self.variables_cancer = {
            'OPN (pg/ml)': tk.StringVar(),
            'IL-6 (pg/ml)': tk.StringVar(),
            'IL-8 (pg/ml)': tk.StringVar(),
            'HGF (pg/ml)': tk.StringVar(),
            'Prolactin (pg/ml)': tk.StringVar(),
            'Omega score': tk.StringVar(),
            'GDF15 (ng/ml)': tk.StringVar(),
            'CYFRA 21-1 (pg/ml)': tk.StringVar(),
            'Myeloperoxidase (ng/ml)': tk.StringVar()
        }

        self.ranges_cancer = {
            'OPN (pg/ml)': '3218-433960',
            'IL-6 (pg/ml)': '3-2818',
            'IL-8 (pg/ml)': '8-5290',
            'HGF (pg/ml)': '158-11433',
            'Prolactin (pg/ml)': '806-608432',
            'Omega score': '0-333',
            'GDF15 (ng/ml)': '0.04-24',
            'CYFRA 21-1 (pg/ml)': '1816-1475727',
            'Myeloperoxidase (ng/ml)': '1-1001'
        }

        # Variables y sus valores predefinidos para la segunda pestaña
        self.variables_tipo_cancer = {
            'sFas (pg/ml)': tk.StringVar(),
            'sHER2/sEGFR2/sErbB2 (pg/ml)': tk.StringVar(),
            'CA 15-3 (U/ml)': tk.StringVar(),
            'CA19-9 (U/ml)': tk.StringVar(),
            'CA-125 (U/ml)': tk.StringVar(),
            'TIMP-2 (pg/ml)': tk.StringVar(),
            'TGFa (pg/ml)': tk.StringVar(),
            'Leptin (pg/ml)': tk.StringVar(),
            'IL-8 (pg/ml)': tk.StringVar(),
            'IL-6 (pg/ml)': tk.StringVar(),
            'AFP (pg/ml)': tk.StringVar(),
            'GDF15 (ng/ml)': tk.StringVar(),
            'Prolactin (pg/ml)': tk.StringVar(),
            'HGF (pg/ml)': tk.StringVar(),
            'CD44 (ng/ml)': tk.StringVar(),
            'Midkine (pg/ml)': tk.StringVar(),
            'Thrombospondin-2 (pg/ml)': tk.StringVar(),
            'TIMP-1 (pg/ml)': tk.StringVar(),
            'HE4 (pg/ml)': tk.StringVar()
        }

        # Rangos comunes para cada variable en la segunda pestaña
        self.ranges_tipo_cancer = {
            'sFas (pg/ml)': '193-61146',
            'sHER2/sEGFR2/sErbB2 (pg/ml)': '306-150848',
            'CA 15-3 (U/ml)': '1-1177',
            'CA19-9 (U/ml)': '14-12491',
            'CA-125 (U/ml)': '5-3600',
            'TIMP-2 (pg/ml)': '15026-105749',
            'TGFa (pg/ml)': '15-12019',
            'Leptin (pg/ml)': '727-449757',
            'IL-8 (pg/ml)': '8-5290',
            'IL-6 (pg/ml)': '3-2818',
            'AFP (pg/ml)': '706-600608',
            'GDF15 (ng/ml)': '0.04-24',
            'Prolactin (pg/ml)': '806-608432',
            'HGF (pg/ml)': '158-11433',
            'CD44 (ng/ml)': '7-148',
            'Midkine (pg/ml)': '64-53955',
            'Thrombospondin-2 (pg/ml)': '482-157461',
            'TIMP-1 (pg/ml)': '977-569513',
            'HE4 (pg/ml)': '3672-189498'
        }

        # Añadir soporte de scroll a las pestañas
        self.add_scroll_support(self.tab1, self.variables_cancer, self.ranges_cancer, "Predicción de cáncer", self.calculate_cancer)
        self.add_scroll_support(self.tab2, self.variables_tipo_cancer, self.ranges_tipo_cancer, "Predicción del tipo de cáncer", self.calculate_tipo_cancer)

    def add_scroll_support(self, tab, variables, ranges, title, calculate_command):
        # Crear un canvas para permitir scroll
        canvas = tk.Canvas(tab)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Añadir el canvas y el scrollbar a la pestaña
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Crear el contenido de la pestaña dentro del frame scrollable
        self.setup_tab(scrollable_frame, variables, ranges, title, calculate_command)

    def setup_tab(self, tab, variables, ranges, title, calculate_command):
        # Create the random button
        generate_button = ttk.Button(tab, text="Generar valores aleatorios",
                                     command=lambda: self.generate_random_values(variables, ranges, title))
        generate_button.pack(pady=10)

        # Frame para las entradas de texto
        frame_inputs = ttk.Frame(tab, padding="10")
        frame_inputs.pack()

        # Añadir las etiquetas de encabezado
        header_labels = ["Variable", "Valor", "Mínimo - Máximo"]
        for j, text in enumerate(header_labels):
            label = ttk.Label(frame_inputs, text=text, font=("Arial", 10, "bold"))
            label.grid(row=0, column=j, padx=5, pady=5, sticky="w")

        # Crear etiquetas y entradas para cada variable
        for i, (variable, var_value) in enumerate(variables.items(), start=1):
            label = ttk.Label(frame_inputs, text=variable)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = ttk.Entry(frame_inputs, textvariable=var_value)
            entry.grid(row=i, column=1, padx=5, pady=5)

            # Generar valor aleatorio para cada variable
            # var_value.set(random.randint(1, 100))  # Ejemplo: números aleatorios del 1 al 100

            self.generate_random_values(variables, ranges, title)

            # Añadir etiqueta con el rango de valores común
            range_label = ttk.Label(frame_inputs, text=ranges[variable])
            range_label.grid(row=i, column=2, padx=12, pady=5, sticky="w")

        # Combobox para seleccionar el modelo de aprendizaje supervisado
        label_combox = ttk.Label(tab, text="Modelo a utilizar para la predicción:")
        label_combox.pack(pady=(10, 0))
        model_var = tk.StringVar()
        model_combobox = ttk.Combobox(tab, textvariable=model_var)
        if title == 'Predicción de cáncer':
            model_combobox['values'] = (const.Constantes.REGRESION_LINEAL, const.Constantes.REGRESION_LOGISTICA,
                                        const.Constantes.RANDOM_FOREST, const.Constantes.KNN, const.Constantes.GRADIENT_BOOSTING,
                                        const.Constantes.ADABOOST, const.Constantes.VOTING_CLASSIFIER_1)
        else:
            model_combobox['values'] = (const.Constantes.VOTING_CLASSIFIER_2,)
        model_combobox.current(0)  # Seleccionar el primer modelo por defecto
        model_combobox.pack(pady=10)

        # Botón para realizar los cálculos
        btn_calculate = ttk.Button(tab, text="Calcular", command=lambda: calculate_command(variables, model_var))
        btn_calculate.pack(pady=10)



    def calculate_cancer(self, variables, model_var):
        # Obtener los valores de las variables
        data = {variable: [float(var_value.get())] for variable, var_value in variables.items()}
        df = pd.DataFrame(data)
        # df_prep = fn.process_data(split = True, process_data = True, df_sample = df)
        df_prep = fn.process_data_1(df)
        # Seleccionar el modelo basado en la opción del combobox
        model_name = model_var.get()
        if model_name == const.Constantes.REGRESION_LINEAL:
            result, prob = md.RegressionLineal(df_prep)
        elif model_name == const.Constantes.REGRESION_LOGISTICA:
            result, prob = md.RegressionLogistica(df_prep)
        elif model_name == const.Constantes.RANDOM_FOREST:
            result, prob = md.RandomForest(df_prep)
        elif model_name == const.Constantes.KNN:
            result, prob = md.KNN(df_prep)
        elif model_name == const.Constantes.ADABOOST:
            result, prob = md.AdaBoost(df_prep)
        elif model_name == const.Constantes.GRADIENT_BOOSTING:
            result, prob = md.GradientBoosting(df_prep)
        elif model_name == const.Constantes.VOTING_CLASSIFIER_1:
            result, prob = md.VotingClassifier_1(df_prep)
        else:
            result, prob = None, None
        result_message = ""
        if prob is not None and not df.empty:
            # Mostrar el resultado en una ventana emergente
            result_message = f"Tiene una probabilidad estimada del : {round(float(prob)*100, ndigits=2)}% de tener cáncer."

        result_message += f"\nPredicción: {'Tiene cáncer' if result == 1 else 'No tiene cáncer'}"
        tk.messagebox.showinfo("Resultado", result_message)

    def calculate_tipo_cancer(self, variables, model_var):
        # Obtener los valores de las variables
        data = {variable: [float(var_value.get())] for variable, var_value in variables.items()}
        df = pd.DataFrame(data)

        # Procesa los datos base
        df_prep = fn.process_data_cancer_type(df)

        # Seleccionar el modelo basado en la opción del combobox
        model_name = model_var.get()
        result, prob = md.VotingClassifier_2(df_prep)
        if model_name == const.Constantes.VOTING_CLASSIFIER_2:
            result, prob = md.VotingClassifier_2(df_prep)
            fn.get_path()
        label_encoder = joblib.load(os.path.join(fn.get_path(), 'Tumor type_label_encoder.joblib'))
        result = label_encoder.inverse_transform(result)
        # Mostrar el resultado en una ventana emergente
        result_message = f"Predicción del tipo de cáncer: {result[0]}"
        tk.messagebox.showinfo("Resultado", result_message)

    def generate_random_values(self, variables, ranges, title):
        if title == 'Predicción de cáncer':
            if self.ctgan_model is not None:
                synthetic_sample = self.ctgan_model.sample(1).iloc[0]
                for variable, var_value in variables.items():
                    if variable in synthetic_sample:
                        min_val, max_val = map(float, ranges[variable].split('-'))
                        var_value.set(fn.check_limitis(round(synthetic_sample[variable], 2), min_val, max_val))

            else:
                for variable, var_value in variables.items():
                    min_val, max_val = map(float, ranges[variable].split('-'))
                    var_value.set(round(random.uniform(min_val, max_val), 2))
        else:
            if self.ctgan_model_2 is not None:
                synthetic_sample = self.ctgan_model_2.sample(1).iloc[0]
                for variable, var_value in variables.items():
                    if variable in synthetic_sample:
                        min_val, max_val = map(float, ranges[variable].split('-'))
                        var_value.set(fn.check_limitis(round(synthetic_sample[variable], 2), min_val, max_val))
            else:
                for variable, var_value in variables.items():
                    min_val, max_val = map(float, ranges[variable].split('-'))
                    var_value.set(round(random.uniform(min_val, max_val), 2))

    def show_info(self):
        info_message = "Aplicación para detección de cáncer\n\n"
        info_message += "Esta aplicación de prueba utiliza diferentes modelos de aprendizaje supervisado para predecir la presencia de cáncer en función de varias biomarcas.\n\n"
        info_message += "Puede escogerse entre diferentes modelos de aprendizaje supervisado para realizar la predicción. Se encuentran ordenados de menor a mayor efectividad\n\n"
        info_message += ("Se puede permutar a la pestaña 'Predicción del tipo de cancer' para realizar la predecir que tipo de cáncer se tiene en función de los parámetros introducidos.\n"
                         "El modelo que predice el tipo de cáncer se trata de un conglomerado de modelos de aprendizaje supervisado combinados mediante la técnica de vosting classifier.\n\n")
        info_message += ("Los modelos de aprendizaje supervisado utilizados en el 'Vooting Classifier 2' son:\n")
        info_message += ("\t - Random Forest\n")
        info_message += ("\t - Gradient Boosting\n")
        info_message += ("\t - Light GBM\n")
        info_message += ("\t - XGBoost\n")
        info_message += ("Existe la posibilidad de generar valores aleatorios para las biomarcadores siguiendo un modelo de generación de datos sintéticos CTGAN que está entrenado para crear una muestra de datos siguiendo una distribución"
                         "pareja a los datos utilizados durante el estudio\n\n")
        info_message += ("Tras presionar el botón 'Calcular' se muestra en una ventana emergente  la probabilidad de tener cáncer, que variará según el modelo escogido, y "
                         "la predicción del modelo.\n\n")

        tk.messagebox.showinfo("Información", info_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)

    # Cargar el modelo CTGAN entrenado
    trainer = fn.CTGANTrainer(const.Constantes.param_grid, const.Constantes.model_path, pac=1)
    trainer2 = fn.CTGAN2(const.Constantes.param_grid, const.Constantes.model_path_2, pac=1)

    # Asignar el modelo a la instancia de MyApp
    app.ctgan_model = trainer.load_model()
    app.ctgan_model_2 = trainer2.load_model()
    root.mainloop()
