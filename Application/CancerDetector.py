import tkinter as tk
from tkinter import ttk, messagebox
import random
import Functions as fn
import Models as md
import pandas as pd
import numpy as np

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación para detección de cáncer")
        
        # Variables y sus valores predefinidos
        self.variables = {
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
        
        # Frame para las entradas de texto
        frame_inputs = ttk.Frame(self.root, padding="10")
        frame_inputs.pack()
        
        # Crear etiquetas y entradas para cada variable
        for i, (variable, var_value) in enumerate(self.variables.items()):
            label = ttk.Label(frame_inputs, text=variable)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            
            entry = ttk.Entry(frame_inputs, textvariable=var_value)
            entry.grid(row=i, column=1, padx=5, pady=5)
            
            # Generar valor aleatorio para cada variable
            var_value.set(random.randint(1, 100))  # Ejemplo: números aleatorios del 1 al 100

        # Combobox para seleccionar el modelo de aprendizaje supervisado
        label_combox = ttk.Label(self.root, text="Modelo a utilizar para la predicción:")
        label_combox.pack(pady=(10, 0))
        self.model_var = tk.StringVar()
        self.model_combobox = ttk.Combobox(self.root, textvariable=self.model_var)
        self.model_combobox['values'] = ('Regresión Lineal', 'Árbol de Decisión', 'Máquina de Soporte Vectorial')
        self.model_combobox.current(0)  # Seleccionar el primer modelo por defecto
        self.model_combobox.pack(pady=10)

        # Botón para realizar los cálculos
        btn_calculate = ttk.Button(self.root, text="Calcular", command=self.calculate)
        btn_calculate.pack(pady=10)


    def calculate(self):
        # Obtener los valores de las variables
        data = {variable: [float(var_value.get())] for variable, var_value in self.variables.items()}
        df = pd.DataFrame(data)

        # Procesa los datos base
        X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test = fn.process_data()

        # Seleccionar el modelo basado en la opción del combobox
        model_name = self.model_var.get()
        if model_name == 'Regresión Lineal':
            result, prob = md.RegressionLineal(X_train_prep, X_val_prep, X_test_prep, y_train, y_val, y_test, df)
        elif model_name == 'Árbol de Decisión':
            print("En proceso")
        elif model_name == 'Máquina de Soporte Vectorial':
            print("En proceso")

        # Mostrar el resultado en una ventana emergente
        result_message = f"Predicción: {'Tiene cáncer' if result == 1 else 'No tiene cáncer'}"
        result_message += f"\nCon una probabilidad de : {prob}"
        tk.messagebox.showinfo("Resultado", result_message)
        


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()