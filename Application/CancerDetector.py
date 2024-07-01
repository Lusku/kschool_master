from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import random
import pandas as pd
import Models as md
import Functions as fn

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación para detección de cáncer")

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
            'CA19-9 (U/ml)': tk.StringVar(),
            'CA-125 (U/ml)': tk.StringVar(),
            'HGF (pg/ml)': tk.StringVar(),
            'OPN (pg/ml)': tk.StringVar(),
            'Omega score': tk.StringVar(),
            'Prolactin (pg/ml)': tk.StringVar(),
            'CEA (pg/ml)': tk.StringVar(),
            'Myeloperoxidase (ng/ml)': tk.StringVar(),
            'TIMP-1 (pg/ml)': tk.StringVar()
            # Puedes añadir más variables según sea necesario
        }

        # Rangos comunes para cada variable en la primera pestaña
        self.ranges_cancer = {
            'CA19-9 (U/ml)': '14-12491',
            'CA-125 (U/ml)': '4-3600',
            'HGF (pg/ml)': '158-11432',
            'OPN (pg/ml)': '3218-433959',
            'Omega score': '0-333',
            'Prolactin (pg/ml)': '806-608432',
            'CEA (pg/ml)': '426-337245',
            'Myeloperoxidase (ng/ml)': '1-1001',
            'TIMP-1 (pg/ml)': '482-157461'
        }

        # Variables y sus valores predefinidos para la segunda pestaña
        self.variables_tipo_cancer = {
            'AFP (pg/ml)': tk.StringVar(),
            'Angiopoietin-2 (pg/ml)': tk.StringVar(),
            'AXL (pg/ml)': tk.StringVar(),
            'CA-125 (U/ml)': tk.StringVar(),
            'CA 15-3 (U/ml)': tk.StringVar(),
            'CA19-9 (U/ml)': tk.StringVar(),
            'CD44 (ng/ml)': tk.StringVar(),
            'CEA (pg/ml)': tk.StringVar(),
            'CYFRA 21-1 (pg/ml)': tk.StringVar(),
            'DKK1 (ng/ml)': tk.StringVar(),
            'Endoglin (pg/ml)': tk.StringVar(),
            'FGF2 (pg/ml)': tk.StringVar(),
            'Follistatin (pg/ml)': tk.StringVar(),
            'Galectin-3 (ng/ml)': tk.StringVar(),
            'G-CSF (pg/ml)': tk.StringVar(),
            'GDF15 (ng/ml)': tk.StringVar(),
            'HE4 (pg/ml)': tk.StringVar(),
            'HGF (pg/ml)': tk.StringVar(),
            'IL-6 (pg/ml)': tk.StringVar(),
            'IL-8 (pg/ml)': tk.StringVar(),
            'Kallikrein-6 (pg/ml)': tk.StringVar(),
            'Leptin (pg/ml)': tk.StringVar(),
            'Mesothelin (ng/ml)': tk.StringVar(),
            'Midkine (pg/ml)': tk.StringVar(),
            'Myeloperoxidase (ng/ml)': tk.StringVar(),
            'NSE (ng/ml)': tk.StringVar(),
            'OPG (ng/ml)': tk.StringVar(),
            'OPN (pg/ml)': tk.StringVar(),
            'PAR (pg/ml)': tk.StringVar(),
            'Prolactin (pg/ml)': tk.StringVar(),
            'sEGFR (pg/ml)': tk.StringVar(),
            'sFas (pg/ml)': tk.StringVar(),
            'SHBG (nM)': tk.StringVar(),
            'sHER2/sEGFR2/sErbB2 (pg/ml)': tk.StringVar(),
            'sPECAM-1 (pg/ml)': tk.StringVar(),
            'TGFa (pg/ml)': tk.StringVar(),
            'Thrombospondin-2 (pg/ml)': tk.StringVar(),
            'TIMP-1 (pg/ml)': tk.StringVar(),
            'TIMP-2 (pg/ml)': tk.StringVar(),
            'Omega score': tk.StringVar()
        }

        # Rangos comunes para cada variable en la segunda pestaña
        self.ranges_tipo_cancer = {
            'AFP (pg/ml)': '706-600608',
            'Angiopoietin-2 (pg/ml)': '38-30001',
            'AXL (pg/ml)': '109-12247',
            'CA-125 (U/ml)': '5-3600',
            'CA 15-3 (U/ml)': '1-1177',
            'CA19-9 (U/ml)': '14-12491',
            'CD44 (ng/ml)': '7-148',
            'CEA (pg/ml)': '426-337245',
            'CYFRA 21-1 (pg/ml)': '1816-1475727',
            'DKK1 (ng/ml)': '0.35-5.97',
            'Endoglin (pg/ml)': '79-16244',
            'FGF2 (pg/ml)': '80-735',
            'Follistatin (pg/ml)': '62-8126',
            'Galectin-3 (ng/ml)': '0.2-140',
            'G-CSF (pg/ml)': '29-12828',
            'GDF15 (ng/ml)': '0.04-24',
            'HE4 (pg/ml)': '3672-189498',
            'HGF (pg/ml)': '158-11433',
            'IL-6 (pg/ml)': '3-2818',
            'IL-8 (pg/ml)': '8-5290',
            'Kallikrein-6 (pg/ml)': '137-53357',
            'Leptin (pg/ml)': '727-449757',
            'Mesothelin (ng/ml)': '1-583',
            'Midkine (pg/ml)': '64-53955',
            'Myeloperoxidase (ng/ml)': '1-1001',
            'NSE (ng/ml)': '1-220',
            'OPG (ng/ml)': '0.09-4.2',
            'OPN (pg/ml)': '3218-433960',
            'PAR (pg/ml)': '663-49042',
            'Prolactin (pg/ml)': '806-608432',
            'sEGFR (pg/ml)': '198-8577',
            'sFas (pg/ml)': '193-61146',
            'SHBG (nM)': '2-479',
            'sHER2/sEGFR2/sErbB2 (pg/ml)': '306-150848',
            'sPECAM-1 (pg/ml)': '220-15318',
            'TGFa (pg/ml)': '15-12019',
            'Thrombospondin-2 (pg/ml)': '482-157461',
            'TIMP-1 (pg/ml)': '977-569513',
            'TIMP-2 (pg/ml)': '15026-105749',
            'Omega score': '0-333'
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
                                     command=lambda: self.generate_random_values(variables, ranges))
        generate_button.pack(pady=10)

        # Frame para las entradas de texto
        frame_inputs = ttk.Frame(tab, padding="10")
        frame_inputs.pack()

        # Añadir las etiquetas de encabezado
        header_labels = ["Variable", "Valor", "Rango común"]
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
            self.generate_random_values(variables, ranges)

            # Añadir etiqueta con el rango de valores común
            range_label = ttk.Label(frame_inputs, text=ranges[variable])
            range_label.grid(row=i, column=2, padx=12, pady=5, sticky="w")

        # Combobox para seleccionar el modelo de aprendizaje supervisado
        label_combox = ttk.Label(tab, text="Modelo a utilizar para la predicción:")
        label_combox.pack(pady=(10, 0))
        model_var = tk.StringVar()
        model_combobox = ttk.Combobox(tab, textvariable=model_var)
        model_combobox['values'] = (Constantes.REGRESION_LINEAL, Constantes.REGRESION_LOGISTICA,
                                    Constantes.ADABOOST, Constantes.RANDOM_FOREST, Constantes.GRADIENT_BOOSTING)
        model_combobox.current(0)  # Seleccionar el primer modelo por defecto
        model_combobox.pack(pady=10)

        # Botón para realizar los cálculos
        btn_calculate = ttk.Button(tab, text="Calcular", command=lambda: calculate_command(variables, model_var))
        btn_calculate.pack(pady=10)

    def calculate_cancer(self, variables, model_var):
        # Obtener los valores de las variables
        data = {variable: [float(var_value.get())] for variable, var_value in variables.items()}
        df = pd.DataFrame(data)

        # Procesa los datos base
        X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test = fn.process_data()

        # Seleccionar el modelo basado en la opción del combobox
        model_name = model_var.get()
        if model_name == Constantes.REGRESION_LINEAL:
            result, prob = md.RegressionLineal(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == Constantes.REGRESION_LOGISTICA:
            result, prob = md.RegresionLogistica(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == Constantes.ADABOOST:
            result, prob = md.AdaBoost(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == Constantes.RANDOM_FOREST:
            result, prob = md.RandomForest(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == Constantes.GRADIENT_BOOSTING:
            result, prob = md.GradientBoosting(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)

        # Mostrar el resultado en una ventana emergente
        result_message = f"Predicción: {'Tiene cáncer' if result == 1 else 'No tiene cáncer'}"
        result_message += f"\nCon una probabilidad estimada de : {round(prob, ndigits=2)}"
        tk.messagebox.showinfo("Resultado", result_message)

    def calculate_tipo_cancer(self, variables, model_var):
        # Obtener los valores de las variables
        data = {variable: [float(var_value.get())] for variable, var_value in variables.items()}
        df = pd.DataFrame(data)

        # Procesa los datos base
        X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test = fn.process_data_tipo_cancer()

        # Seleccionar el modelo basado en la opción del combobox
        model_name = model_var.get()
        if model_name == Constantes.REGRESION_LINEAL:
            result, prob = md.RegressionLineal(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == Constantes.REGRESION_LOGISTICA:
            result, prob = md.RegresionLogistica(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == Constantes.ADABOOST:
            result, prob = md.AdaBoost(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == Constantes.RANDOM_FOREST:
            result, prob = md.RandomForest(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == Constantes.GRADIENT_BOOSTING:
            result, prob = md.GradientBoosting(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)

        # Mostrar el resultado en una ventana emergente
        result_message = f"Predicción del tipo de cáncer: {result}"
        result_message += f"\nCon una probabilidad estimada de : {round(prob, ndigits=2)}"
        tk.messagebox.showinfo("Resultado", result_message)

    def generate_random_values(self, variables, ranges):
        for variable, var_value in variables.items():
            min_val, max_val = map(float, ranges[variable].split('-'))
            var_value.set(round(random.uniform(min_val, max_val),2))

    def show_info(self):
        info_message = "Aplicación para detección de cáncer\n\n"
        info_message += "Esta es una aplicación de prueba que utiliza diferentes modelos de aprendizaje supervisado para predecir la presencia de cáncer en función de varias biomarcas.\n\n"
        info_message += "Puede generar valores aleatorios para las biomarcas y seleccionar un modelo para realizar la predicción."

        tk.messagebox.showinfo("Información", info_message)


class Constantes:
    REGRESION_LINEAL = 'Regresión Lineal'
    REGRESION_LOGISTICA = 'Regresión Logística'
    ADABOOST = 'AdaBoost'
    RANDOM_FOREST = 'Random Forest'
    GRADIENT_BOOSTING = 'Gradient Boosting'


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()