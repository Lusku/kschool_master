# <u>**Conclusiones, Dificultades y Caminos Abiertos**</u>

## 1. Conclusiones de los resultados del proyecto


Nuestro proyecto se basa en la premisa de simular y mejorar el estudio existente "[Early Cancer Detection from Multianalyte Blood Test Results](https://www.cell.com/iscience/fulltext/S2589-0042(19)30132-4?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS2589004219301324%3Fshowall%3Dtrue)". Elegimos este tema debido a la fascinante intersección entre la salud y las ciencias de datos. Al profundizar en el proyecto, se hizo evidente que representa un punto de inflexión significativo en la integración de la ciencia de datos con el análisis de ADN y ARN presentes en la sangre.

En nuestra búsqueda por expandir y consolidar nuestros conocimientos, hemos utilizado recursos tecnológicos propios y hemos avanzado gradualmente en nuestro aprendizaje. Este crecimiento, impulsado por la formación recibida, ha sido crucial para abordar las diversas dificultades que encontramos a lo largo del proyecto. Enfrentamos desafíos que nos llevaron a hacer pausas debido a limitaciones en conocimientos, recursos y tiempo. A pesar de estas dificultades, el proyecto presenta un amplio margen para mejoras y adiciones significativas, las cuales sólo pueden realizarse en un entorno de investigación adecuado.

---

Como parte de nuestras conclusiones y recordatorio del trabajo realizado, analizaremos en términos generales los resultados obtenidos tanto en el notebook 1 como en el notebook 2. Comenzaremos con la primera parte del proyecto, enfocándonos en las curvas AUC-ROC, detalladas a continuación:


### 1.1. MODELO PREDICCIÓN, notebook 1: Comparación de los resultados actuales con los resultados del proyecto [Early Cancer Detection from Multianalyte Blood Test Results](https://www.cell.com/iscience/fulltext/S2589-0042(19)30132-4?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS2589004219301324%3Fshowall%3Dtrue)

![fx1 lrg](fx1_lrg.png)
 **Curva AUC ROC, Wong et all.**
 
*Fig. 1*

Análisis CURVA AUC ROC, Modelo 1.
1. **Modelos Evaluados**:
- CancerA1DE (AUC=0.99)
- CancerA2DE (AUC=0.99)
- CancerSEEK (AUC=0.93)
- DeepLearning1 (AUC=0.90)
- DeepLearning2 (AUC=0.90)
- DeepLearning3 (AUC=0.90)
- J48 (AUC=0.92)
- NaiveBayes (AUC=0.89)

2. **Rendimiento General**:
- Los modelos CancerA1DE y CancerA2DE tienen un desempeño sobresaliente con un AUC de 0.99.
- CancerSEEK también muestra un rendimiento fuerte con un AUC de 0.93.
- Los modelos de aprendizaje profundo (DeepLearning1, DeepLearning2, y DeepLearning3) tienen un AUC de 0.90, lo que indica un rendimiento bastante bueno pero no tan excelente como los primeros dos.
- El modelo J48 tiene un buen rendimiento con un AUC de 0.92.
- NaiveBayes tiene el menor AUC entre estos modelos con 0.89, aunque sigue siendo un valor relativamente alto.

3. **Curva ROC**:
- La curva ROC está bien separada del eje diagonal (línea de azar), especialmente para los modelos con AUC altos.
- Los modelos con AUC de 0.99 tienen curvas muy cercanas al eje de la izquierda y al tope, indicando una alta tasa de verdaderos positivos y una baja tasa de falsos positivos.


![Enfoque 1 notebook 1](Enfoque%201%20notebook%201.png)
**Curva AUC ROC, Enfoque 1, Notebook 1**

*Fig. 2*

Análisis CURVA AUC ROC, Modelo 2
1. **Modelos Evaluados**:
- Regresión Logística (AUC=0.96)
- Árbol de Decisión (AUC=0.93)
- KNN (AUC=0.96)
- SVM (AUC=0.96)
- Naive Bayes - Gaussiano (AUC=0.96)
- Naive Bayes - Bernoulli (AUC=0.96)
- AdaBoost (AUC=0.95)
- Gradient Boosting (AUC=0.96)
- Regresión Polinomial (AUC=0.96)

2. **Rendimiento General**:
- La mayoría de los modelos tienen un AUC de 0.96, lo que sugiere un rendimiento excelente y uniforme en varios enfoques.
- El Árbol de Decisión tiene un AUC más bajo de 0.93, y AdaBoost tiene un AUC de 0.95.
- Los valores de AUC altos indican que estos modelos tienen una buena capacidad para distinguir entre las clases.

3. **Curva ROC**:
- Similar a la primera imagen, las curvas ROC están bien separadas del eje diagonal.
- Las curvas de los modelos con AUC de 0.96 son casi idénticas y están muy cerca del eje de la izquierda y al tope, indicando un rendimiento muy alto en términos de tasa de verdaderos positivos y baja tasa de falsos positivos.


![Enfoque 2 notebook 1](Enfoque%202%20notebook%201.png)
**Curva AUC ROC, Enfoque 2, Notebook 1**

*Fig. 3*

Análisis CURVA AUC ROC, Modelo 3
1. **Modelos Evaluados**:
- Regresión Logística (AUC=0.99)
- Árbol de Decisión (AUC=0.95)
- KNN (AUC=0.99)
- SVM (AUC=0.99)
- Naive Bayes - Gaussiano (AUC=0.99)
- Naive Bayes - Bernoulli (AUC=0.98)
- AdaBoost (AUC=0.98)
- Gradient Boosting (AUC=0.99)
- Regresión Polinomial (AUC=0.99)

2. **Rendimiento General**:
- La mayoría de los modelos tienen un AUC de 0.99, indicando un rendimiento excepcional.
- El Árbol de Decisión tiene un AUC de 0.95.
- AdaBoost y Naive Bayes - Bernoulli tienen un AUC de 0.98.

3. **Curva ROC**:
- Las curvas ROC están bien separadas del eje diagonal.
- Los modelos con AUC de 0.99 tienen curvas cercanas al eje de la izquierda y la parte superior, indicando un rendimiento muy alto.

#### 1.1.1. Comparación General de los tres modelos

 **COMPARACIÓN DE LOS ANÁLISIS**

1. **Modelos Evaluados y Rendimiento General**

- **Modelo 1**:
  - **Modelos Evaluados**: CancerA1DE y CancerA2DE destacan con un AUC de 0.99, seguidos por CancerSEEK (0.93), y varios modelos de aprendizaje profundo (0.90). J48 tiene un AUC de 0.92 y NaiveBayes (0.89).
  - **Rendimiento General**: Los modelos CancerA1DE y CancerA2DE muestran un rendimiento sobresaliente, seguidos de CancerSEEK y los modelos de aprendizaje profundo. NaiveBayes presenta el AUC más bajo pero aún alto en comparación con otros modelos.

- **Modelo 2**:
  - **Modelos Evaluados**: Regresión Logística, KNN, SVM, Naive Bayes (Gaussiano y Bernoulli), Gradient Boosting, y Regresión Polinomial tienen un AUC de 0.96, mientras que el Árbol de Decisión y AdaBoost tienen AUCs de 0.93 y 0.95 respectivamente.
  - **Rendimiento General**: La mayoría de los modelos tienen un rendimiento excelente con un AUC de 0.96. El Árbol de Decisión y AdaBoost tienen un rendimiento ligeramente inferior pero siguen siendo efectivos.

- **Modelo 3**:
  - **Modelos Evaluados**: La mayoría de los modelos, incluyendo Regresión Logística, KNN, SVM, Naive Bayes (Gaussiano), y Gradient Boosting tienen un AUC de 0.99, mientras que el Árbol de Decisión (0.95), AdaBoost y Naive Bayes - Bernoulli (0.98) presentan valores ligeramente menores.
  - **Rendimiento General**: La mayoría de los modelos tienen un rendimiento excepcional con un AUC de 0.99. Solo algunos modelos como el Árbol de Decisión y algunos modelos de boosting tienen AUCs inferiores.

 **CURVA ROC**

- **Modelo 1**:
  - **Curvas ROC**: Las curvas ROC para los modelos con AUC de 0.99 están muy cerca del eje izquierdo y la parte superior, lo que indica una alta tasa de verdaderos positivos y una baja tasa de falsos positivos. Los modelos con AUC más bajos muestran curvas menos cercanas al eje superior.

- **Modelo 2**:
  - **Curvas ROC**: Similar al Texto 1, las curvas ROC para los modelos con AUC de 0.96 están bien separadas del eje diagonal y se acercan al eje izquierdo y la parte superior, indicando un rendimiento alto. Las diferencias entre las curvas de los modelos son mínimas, dado que muchos tienen el mismo AUC.

- **Modelo 3**:
  - **Curvas ROC**: Las curvas ROC de los modelos con AUC de 0.99 están bien separadas del eje diagonal, muy cerca del eje izquierdo y la parte superior, reflejando un rendimiento muy alto. Las curvas para los modelos con AUC ligeramente inferiores también están bien posicionadas pero no tan cerca del ideal como los modelos con 0.99.

**RESUMEN COMPARATIVO**

- **Modelo y Rendimiento**: En el modelo 1, los modelos CancerA1DE y CancerA2DE destacan con el mejor rendimiento, mientras que en los Modelos 2 y 3, la mayoría de los modelos muestran un rendimiento sobresaliente con AUCs altos, aunque el modelo 3 destaca por la prevalencia de modelos con AUC de 0.99. El modelo 2 presenta una distribución más variada de AUCs entre los modelos.

- **Curvas ROC**: En todos los modelos, las curvas ROC muestran una separación clara del eje diagonal, indicando una buena capacidad de los modelos para distinguir entre las clases. En general, los modelos con AUC más altos tienen curvas que se acercan más al ideal, pero las diferencias son menores cuando el AUC es alto (0.96 o superior).

Esta comparación muestra que, en general, los modelos con AUC más altos ofrecen un rendimiento muy bueno, y la capacidad de distinguir entre clases mejora conforme el AUC se aproxima a 1. Las curvas ROC corroboran estos hallazgos al mostrar una separación efectiva de las clases en todos los análisis.


### 1.2. MODELO CLASIFICACIÓN, notebook 2: Comparación de los resultados actuales con los resultados del proyecto [Early Cancer Detection from Multianalyte Blood Test Results](https://www.cell.com/iscience/fulltext/S2589-0042(19)30132-4?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS2589004219301324%3Fshowall%3Dtrue)


![Cancerseek AUC ROC notebook 2](Cancerseek%20AUC%20ROC%20notebook%202.png)
**Curva AUC ROC, Modelo 1**

*Fig. 4*
1. **Modelos evaluados**:
* Breast - Colorectum
* Breast - Upper GI
* Breast - Liver
* Breast - Lung
* Breast - Ovary
* Breast - Pancreas
* Colorectum - Upper GI
* Colorectum - Liver
* Colorectum - Lung
* Colorectum - Ovary
* Colorectum - Pancreas
* Upper GI - Liver
* Upper Gl - Lung
* Upper Gl - Ovary
* Upper Gl - Pancreas
* Liver - Lung
* Liver - Ovary
* Liver - Pancreas
* Lung - Ovary
* Lung - Pancreas
* Ovary - Pancreas

2. **Rendimiento General**:

- CancerSEEK muestra una polarización notable en su rendimiento, agrupándose en dos extremos. Esto sugiere que el modelo de Random Forest utilizado por CancerSEEK podría estar sesgado hacia ciertas diferenciaciones específicas de tipos de cáncer. 
- Aunque el modelo obtiene buenos resultados en cánceres colorrectal y de ovario, su desempeño se ve comprometido en otros tipos de cáncer. 
- Se observa que la mayoría de los métodos no logran localizar eficazmente el cáncer de hígado, lo que puede atribuirse a la limitada disponibilidad de datos para este tipo específico.

3. **Curva ROC**:

- La curva ROC del análisis revela una variabilidad significativa en el rendimiento de CancerSEEK según el tipo de cáncer. 
- Los altos valores de AUC para los cánceres colorrectal y de ovario indican un buen rendimiento en estos casos. 
- Los valores bajos de AUC para otros tipos de cáncer, especialmente el cáncer de hígado, destacan las limitaciones del modelo debido a la insuficiencia de datos. Esta polarización en la curva ROC subraya la necesidad de mejorar el modelo o de equilibrar el conjunto de datos para obtener un rendimiento más consistente en todos los tipos de cáncer.


 **Modelos evaluados**:

![Probabilidad total](Probabilidad%20total%20AUC%20ROC%20notebook%202.png)
**Curva AUC ROC, Modelo 2**

*Fig. 5*

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matriz de Modelos de Predicción</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 16px;
            text-align: left;
        }
        th, td {
            padding: 12px;
            border: 1px solid #ddd;
        }
        th {
            background-color:#f9f7fa;
        }
        tr:nth-child(even) {
            background-color:#2d6875;
        }
        caption {
            font-size: 18px;
            margin: 10px 0;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <table>
        <caption>Tabla de Predicción de Modelos de Cáncer</caption>
        <thead>
            <tr>
                <th>Modelo / Predicción</th>
                <th>Breast</th>
                <th>Colorectum</th>
                <th>Esophagus</th>
                <th>Liver</th>
                <th>Lung</th>
                <th>Ovary</th>
                <th>Pancreas</th>
                <th>Stomach</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Breast</strong></td>
                <td>Predicted_Proba_Breast</td>
                <td>Predicted_Proba_Colorectum</td>
                <td>Predicted_Proba_Esophagus</td>
                <td>Predicted_Proba_Liver</td>
                <td>Predicted_Proba_Lung</td>
                <td>Predicted_Proba_Ovary</td>
                <td>Predicted_Proba_Pancreas</td>
                <td>Predicted_Proba_Stomach</td>
            </tr>
            <tr>
                <td><strong>Colorectum</strong></td>
                <td>Predicted_Proba_Breast</td>
                <td>Predicted_Proba_Colorectum</td>
                <td>Predicted_Proba_Esophagus</td>
                <td>Predicted_Proba_Liver</td>
                <td>Predicted_Proba_Lung</td>
                <td>Predicted_Proba_Ovary</td>
                <td>Predicted_Proba_Pancreas</td>
                <td>Predicted_Proba_Stomach</td>
            </tr>
            <tr>
                <td><strong>Esophagus</strong></td>
                <td>Predicted_Proba_Breast</td>
                <td>Predicted_Proba_Colorectum</td>
                <td>Predicted_Proba_Esophagus</td>
                <td>Predicted_Proba_Liver</td>
                <td>Predicted_Proba_Lung</td>
                <td>Predicted_Proba_Ovary</td>
                <td>Predicted_Proba_Pancreas</td>
                <td>Predicted_Proba_Stomach</td>
            </tr>
            <tr>
                <td><strong>Liver</strong></td>
                <td>Predicted_Proba_Breast</td>
                <td>Predicted_Proba_Colorectum</td>
                <td>Predicted_Proba_Esophagus</td>
                <td>Predicted_Proba_Liver</td>
                <td>Predicted_Proba_Lung</td>
                <td>Predicted_Proba_Ovary</td>
                <td>Predicted_Proba_Pancreas</td>
                <td>Predicted_Proba_Stomach</td>
            </tr>
            <tr>
                <td><strong>Lung</strong></td>
                <td>Predicted_Proba_Breast</td>
                <td>Predicted_Proba_Colorectum</td>
                <td>Predicted_Proba_Esophagus</td>
                <td>Predicted_Proba_Liver</td>
                <td>Predicted_Proba_Lung</td>
                <td>Predicted_Proba_Ovary</td>
                <td>Predicted_Proba_Pancreas</td>
                <td>Predicted_Proba_Stomach</td>
            </tr>
            <tr>
                <td><strong>Ovary</strong></td>
                <td>Predicted_Proba_Breast</td>
                <td>Predicted_Proba_Colorectum</td>
                <td>Predicted_Proba_Esophagus</td>
                <td>Predicted_Proba_Liver</td>
                <td>Predicted_Proba_Lung</td>
                <td>Predicted_Proba_Ovary</td>
                <td>Predicted_Proba_Pancreas</td>
                <td>Predicted_Proba_Stomach</td>
            </tr>
            <tr>
                <td><strong>Pancreas</strong></td>
                <td>Predicted_Proba_Breast</td>
                <td>Predicted_Proba_Colorectum</td>
                <td>Predicted_Proba_Esophagus</td>
                <td>Predicted_Proba_Liver</td>
                <td>Predicted_Proba_Lung</td>
                <td>Predicted_Proba_Ovary</td>
                <td>Predicted_Proba_Pancreas</td>
                <td>Predicted_Proba_Stomach</td>
            </tr>
            <tr>
                <td><strong>Stomach</strong></td>
                <td>Predicted_Proba_Breast</td>
                <td>Predicted_Proba_Colorectum</td>
                <td>Predicted_Proba_Esophagus</td>
                <td>Predicted_Proba_Liver</td>
                <td>Predicted_Proba_Lung</td>
                <td>Predicted_Proba_Ovary</td>
                <td>Predicted_Proba_Pancreas</td>
                <td>Predicted_Proba_Stomach</td>
            </tr>
        </tbody>
    </table>
</body>
</html>


2. **Rendimiento General**:

El modelo presenta un desempeño general sólido con una precisión total de 0.77, destacándose en la clasificación de tumores de **Ovary** y **Esophagus**, que obtienen altos valores en precisión, recall y f1-score. Sin embargo, muestra debilidades notables en **Lung** y **Liver**, con puntuaciones de 0.00 y 0.14 en f1-score, respectivamente, indicando un pobre desempeño en la identificación de estos tipos. La **Breast** y **Colorectum** tienen un rendimiento equilibrado, pero aún hay margen para mejorar la precisión y el recall en clases menos representadas. En general, el modelo tiene una precisión y recall promedio de 0.69 y 0.63, respectivamente, sugiriendo que, aunque tiene buenos resultados en algunas categorías, la precisión general es variable entre diferentes tipos de tumores.

3. **Curva ROC**:

El análisis de los resultados muestra un desempeño sobresaliente del modelo en la mayoría de las clases, con todas las AUC superiores a 0.90. Las clases **Ovary** y **Breast** destacan con AUCs perfectos de 1.00 y 0.99 respectivamente, indicando una excelente capacidad de discriminación. Las clases **Colorectum** y **Esophagus** también muestran AUCs altas (0.96 y 0.95), lo que refleja un buen rendimiento en la identificación de estos tumores. Sin embargo, **Lung** y **Stomach** tienen AUCs ligeramente menores (0.92), sugiriendo que el modelo tiene un desempeño marginalmente inferior en estas clases.

![Cancerseek AUC ROC SMOTE Y CTGANSnotebook 2](Cancerseek%20AUC%20ROC%20SMOTE%20Y%20CTGANSnotebook%202.png)
**Curva AUC ROC, Modelo 3**

*Fig. 6*
1. **Modelos evaluados**
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matriz de Confusión</title>
    <style>
        table {
            width: 60%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
        }
        caption {
            font-size: 1.5em;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <table>
        <caption>Matriz de Confusión</caption>
        <thead>
            <tr>
                <th></th>
                <th>Pred 0</th>
                <th>Pred 1</th>
                <th>Pred 2</th>
                <th>Pred 3</th>
                <th>Pred 4</th>
                <th>Pred 5</th>
                <th>Pred 6</th>
                <th>Pred 7</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>True 0</th>
                <td>32</td>
                <td>4</td>
                <td>0</td>
                <td>1</td>
                <td>4</td>
                <td>0</td>
                <td>1</td>
                <td>0</td>
            </tr>
            <tr>
                <th>True 1</th>
                <td>4</td>
                <td>56</td>
                <td>3</td>
                <td>1</td>
                <td>6</td>
                <td>1</td>
                <td>2</td>
                <td>4</td>
            </tr>
            <tr>
                <th>True 2</th>
                <td>2</td>
                <td>3</td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>1</td>
            </tr>
            <tr>
                <th>True 3</th>
                <td>2</td>
                <td>0</td>
                <td>0</td>
                <td>6</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>1</td>
            </tr>
            <tr>
                <th>True 4</th>
                <td>4</td>
                <td>3</td>
                <td>1</td>
                <td>2</td>
                <td>11</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
            </tr>
            <tr>
                <th>True 5</th>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>10</td>
                <td>0</td>
                <td>0</td>
            </tr>
            <tr>
                <th>True 6</th>
                <td>1</td>
                <td>1</td>
                <td>0</td>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td>16</td>
                <td>0</td>
            </tr>
            <tr>
                <th>True 7</th>
                <td>2</td>
                <td>4</td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>1</td>
                <td>3</td>
            </tr>
        </tbody>
    </table>
</body>
</html>



2. **Rendimiento General**

El análisis de la matriz de confusión muestra que el modelo tiene un rendimiento desigual entre diferentes clases. La clase 1 tiene el mejor desempeño con 56 verdaderos positivos y solo algunas confusiones menores, mientras que la clase 6 también muestra buenos resultados con 16 verdaderos positivos y mínimas confusiones. Sin embargo, las clases 2, 3 y 4 tienen problemas de clasificación, con múltiples errores de predicción y pocos verdaderos positivos. En general, el modelo parece tener una precisión aceptable en la mayoría de las clases, pero presenta dificultades significativas con algunas, lo que sugiere la necesidad de ajustes o mejoras adicionales.

3. **Curva ROC**

El análisis de los resultados de AUC-ROC muestra un desempeño sólido del modelo en la mayoría de las clases. La clase 5 tiene la puntuación más alta con un AUC de 0.994, indicando una excelente capacidad para distinguir entre esa clase y las demás. La clase 6 también muestra un AUC muy alto de 0.982, reflejando un buen rendimiento en la clasificación de esa categoría. Las clases 0, 1, 3 y 4 también tienen valores altos, superiores a 0.90, mientras que la clase 2 y la clase 7, con AUCs de 0.834 y 0.878 respectivamente, presentan un rendimiento algo inferior. El AUC promedio macro de 0.918 sugiere que, en general, el modelo ofrece un buen equilibrio en la capacidad de discriminación entre todas las clases.

#### 1.2.1. Comparación General de los tres modelos

- **Modelos y AUC**:
  - El análisis de la matriz de confusión muestra que el modelo actual tiene un rendimiento variado entre las clases, con la clase 5 destacándose con un AUC de 0.994 y la clase 2 mostrando un rendimiento inferior con un AUC de 0.834. Este modelo presenta un buen desempeño general, aunque con áreas que requieren mejoras.
  - En comparación con CancerSEEK, que exhibe un rendimiento polarizado con buenos resultados en ciertos tipos de cáncer pero deficiencias en otros, el modelo actual logra un rendimiento alto en la mayoría de las clases, aunque presenta debilidades en algunas categorías específicas.
  - CancerSEEK tiene una polarización notable en su rendimiento entre diferentes tipos de cáncer, con buenos resultados en cánceres colorrectal y de ovario pero bajo rendimiento en tipos como el cáncer de hígado, indicando una posible limitación en la cobertura de datos.

- **Uniformidad y Diversidad**:
  - El modelo actual muestra alta uniformidad con un AUC promedio macro de 0.918, sugiriendo un equilibrio general en el rendimiento entre las clases. Sin embargo, hay una notable diversidad, especialmente con las clases 2 y 7, que presentan puntuaciones más bajas.
  - CancerSEEK muestra una mayor variabilidad en el rendimiento, con polarización que indica una falta de uniformidad, probablemente relacionada con la disponibilidad desigual de datos para los diferentes tipos de cáncer.
  - En contraste, los resultados del análisis de probabilidades predichas muestran que el modelo es más consistente en su capacidad de identificación para clases como **Liver** y **Lung**, mientras que muestra confusión en clases como **Ovary** y **Pancreas**.

- **Top Performers**:
  - El modelo actual identifica de manera sobresaliente las clases 5 y 6, con AUCs superiores a 0.98, indicando un excelente rendimiento en la clasificación de estas categorías. También muestra un buen desempeño en **Breast** y **Colorectum**.
  - CancerSEEK, aunque efectivo en algunos cánceres, tiene problemas significativos en tipos menos representados como el cáncer de hígado, reflejando una capacidad sesgada hacia ciertos tipos de cáncer.
  - En el análisis de probabilidades, **Liver** y **Lung** tienen las probabilidades predichas más altas, lo que sugiere un buen desempeño en estas categorías, mientras que **Pancreas** y **Ovary** presentan dificultades en diferenciación clara.

- **Rendimiento Inferior**:
  - El modelo actual muestra un rendimiento más bajo en las clases 2 y 7, con AUCs de 0.834 y 0.878, sugiriendo áreas de mejora necesarias para estas categorías.
  - CancerSEEK también enfrenta problemas en tipos de cáncer menos representados, como el cáncer de hígado, indicando limitaciones relacionadas con datos insuficientes para algunas clases.
  - El análisis de probabilidades predichas revela que **Esophagus** y **Stomach** tienen distribuciones de probabilidades que se extienden a otras categorías, sugiriendo que el modelo podría estar confuso o tener una menor capacidad discriminativa en estas áreas.

- **Interpretación y Conclusiones**:
  - El modelo actual muestra un desempeño sólido en general con áreas para mejorar en las clases con menor AUC, indicando una capacidad aceptable para diferenciar entre la mayoría de las clases. Ajustar el modelo podría ser beneficioso para mejorar el rendimiento en las categorías con puntuaciones más bajas.
  - CancerSEEK presenta un buen rendimiento en ciertos cánceres pero revela una polarización en su capacidad de clasificación, lo que subraya la necesidad de equilibrar el conjunto de datos o ajustar el modelo para mejorar la uniformidad en el rendimiento.
  - El análisis de probabilidades predichas confirma que el modelo es efectivo en identificar ciertos tipos de cáncer como **Liver** y **Lung**, pero presenta oportunidades para mejorar la precisión en la clasificación de clases con distribuciones más dispersas. Revisar y ajustar el enfoque de predicción podría mejorar la diferenciación entre clases menos claramente separadas.

## 2. Conclusiones generales

1. **Muestra de Datos**: Es crucial aumentar la muestra de datos para mejorar la robustez y la confiabilidad de los modelos. La recolección de más datos reales sería ideal, aunque los datos sintéticos pueden ser un complemento útil.

2. **Optimización de Modelos**: Continuar ajustando los hiperparámetros y explorando nuevas arquitecturas de modelos podría mejorar los resultados. Agregar más modelos al Voting Classifier también podría aumentar la precisión de las predicciones.

3. **Aplicación Práctica**: La aplicación desarrollada, 'CancerDetector.py', es una herramienta útil para poner a prueba los modelos entrenados. Permite a los usuarios experimentar con diferentes modelos y ver cómo los distintos biomarcadores afectan las predicciones.

4. **Enfoque en la Calidad**: Dado que los datos son de alta calidad pero en pequeña cantidad, es importante mantener un enfoque en la calidad de los datos recolectados en el futuro. Datos más diversos y en mayor cantidad permitirán entrenar modelos más generales y menos propensos al sobreajuste.

5. **Relevancia de los Biomarcadores**: Los biomarcadores seleccionados han demostrado ser efectivos en la predicción del cáncer. Sin embargo, es fundamental seguir investigando y validando estos biomarcadores en estudios futuros para confirmar su relevancia y descubrir nuevos marcadores que puedan mejorar aún más las predicciones.


## 3. Dificultades

Durante el desarrollo del proyecto para la detección temprana de cáncer a partir de pruebas de sangre multianalíticas, se han identificado diversas dificultades significativas que pueden afectar el éxito y la implementación del proyecto. A continuación se detallan estos desafíos:

* **Falta de Datos Reales** 

La escasez de datos auténticos y diversos es un obstáculo importante. Sin una cantidad suficiente de datos representativos, es difícil evaluar el desempeño de los modelos en escenarios reales. La falta de datos puede afectar la precisión de las predicciones y limitar la capacidad de los modelos para generalizar a nuevos datos. Además, la ausencia de datos específicos de diferentes poblaciones puede impedir que el modelo sea equitativo y aplicable a diversas subpoblaciones.

* **Dependencia del Entorno de Desarrollo**

La dependencia del entorno de desarrollo, como una máquina virtual (VM), crea problemas de portabilidad y escalabilidad. Los modelos entrenados deben cargarse en el mismo entorno en el que fueron desarrollados, lo que puede dificultar su implementación en diferentes plataformas o contextos operativos. Esta dependencia también puede limitar la flexibilidad en la gestión y mantenimiento de los modelos.

* **Predicciones Incorrectas Iniciales**

Las predicciones incorrectas iniciales, como la detección de cáncer en todos los casos, se deben a la falta de preprocesamiento adecuado de los datos de entrada. Sin un preprocesamiento consistente, las discrepancias entre los datos de entrada y los datos de entrenamiento pueden llevar a resultados incorrectos. Este problema subraya la necesidad de un pipeline de preprocesamiento robusto que garantice que los datos sean compatibles con el modelo.

* **Limitaciones de Recursos Computacionales**

El entrenamiento de modelos complejos requiere una cantidad significativa de recursos computacionales, incluyendo tiempo de procesamiento, memoria y almacenamiento. Las limitaciones en estos recursos pueden ralentizar el desarrollo e implementación de los modelos, aumentando los costos y afectando la eficiencia general del proyecto. Esto puede ser un desafío, especialmente si no se dispone de infraestructura avanzada, como clústeres de computación o servicios en la nube.

* **Complejidad en la Interpretación de Resultados**

Los modelos complejos, como las redes neuronales profundas, a menudo se consideran "caja negra", lo que dificulta su interpretación y justificación. En aplicaciones médicas, la transparencia es crucial para que los resultados sean comprensibles y justificables para los profesionales de la salud. La falta de interpretabilidad puede generar desconfianza en los resultados y limitar la adopción de los modelos.

* **Gestión de la Calidad de los Datos**

La calidad de los datos de entrada es esencial para el desarrollo de modelos fiables. Datos incompletos, ruidosos o sesgados pueden llevar a resultados incorrectos y a modelos poco fiables. La limpieza de datos, la imputación de valores nulos, la normalización y estandarización, y la eliminación de valores atípicos son procesos críticos que requieren atención meticulosa para asegurar la precisión del modelo.

* **Evolución de los Datos y el Modelo**

Los datos y las condiciones pueden cambiar con el tiempo debido a diversos factores, como nuevas tecnologías de diagnóstico o tratamientos, y cambios en la población estudiada. Estos cambios pueden afectar la precisión y relevancia de los modelos entrenados. Es necesario implementar estrategias de mantenimiento y actualización continua para garantizar que los modelos sigan siendo precisos y útiles.

* **Consideraciones Éticas y de Privacidad**

El manejo de datos sensibles, especialmente en el contexto de la salud, requiere cumplir con normativas de privacidad y ética, como el GDPR en Europa y la HIPAA en Estados Unidos. Estas regulaciones pueden complicar el acceso a ciertos conjuntos de datos y limitar el análisis completo sin comprometer la privacidad de los pacientes. Es fundamental abordar estas consideraciones éticas para garantizar el uso responsable de los datos.

* **Integración con Sistemas Existentes**

Integrar modelos en sistemas y flujos de trabajo existentes puede ser desafiante. Los problemas pueden incluir incompatibilidades de formato de datos y limitaciones en el rendimiento de los sistemas actuales. La integración exitosa requiere una planificación cuidadosa y posiblemente la adaptación de sistemas para garantizar que los modelos se implementen de manera eficiente.

* **Evaluación y Validación del Modelo**

Garantizar que el modelo generalice bien a nuevos datos y no esté sobreajustado a los datos de entrenamiento es un desafío constante. Técnicas robustas de validación, como la validación cruzada y el uso de conjuntos de datos de prueba independientes, son necesarias para garantizar la fiabilidad del modelo. También es crucial realizar un monitoreo continuo del rendimiento para identificar y corregir cualquier disminución en su precisión o efectividad.

* **Desafíos en la Recolección de Datos**

La recolección de datos puede enfrentar desafíos relacionados con la heterogeneidad de las fuentes de datos, la calidad variable de los datos recolectados y las dificultades en el acceso a datos específicos. La coordinación con diferentes instituciones para obtener datos de calidad y asegurar la consistencia en la recolección es fundamental para obtener un conjunto de datos robusto y representativo.

* **Desafíos en la Explicación y Comunicación de Resultados**

Comunicar los resultados del modelo a las partes interesadas, incluyendo profesionales médicos y pacientes, puede ser complicado. La necesidad de traducir resultados técnicos en información comprensible para audiencias no técnicas es un desafío importante. Además, garantizar que las recomendaciones del modelo se alineen con las prácticas clínicas y los protocolos existentes requiere una colaboración efectiva con expertos en el dominio médico.

* **Desafíos en la Adaptación a Nuevas Variantes del Cáncer**

La detección temprana de cáncer puede complicarse con la aparición de nuevas variantes o subtipos de cáncer. Los modelos pueden necesitar ajustes y reentrenamiento para abordar eficazmente estas nuevas variantes, lo que requiere un enfoque dinámico y flexible en el desarrollo del modelo.

* **Desafíos en la Implementación en Entornos Clínicos**

La implementación de modelos en entornos clínicos puede enfrentar desafíos relacionados con la interoperabilidad con sistemas de información médica existentes, la aceptación por parte de los profesionales de la salud y la integración en los flujos de trabajo clínicos. Es necesario un enfoque colaborativo para garantizar que el modelo se adapte bien a las prácticas clínicas y aporte valor a los procesos de diagnóstico y tratamiento.


## 4. Caminos Abiertos
**4.1. Calidad y Cantidad de Datos**

**Ampliación:**
- **Diversificación de la Muestra:** Ampliar la muestra de datos no solo en cantidad, sino también en diversidad, incluyendo datos de diferentes cohortes, etnias, y condiciones clínicas. Esto puede proporcionar una visión más completa y generalizable.
- **Data Augmentation:** Considerar técnicas de augmentación de datos específicas para biomarcadores, como la generación de variaciones en los datos existentes, para simular diferentes condiciones sin necesidad de recolectar datos adicionales.

**Nuevos Puntos:**
- **Integración de Datos Genómicos y Clínicos:** Incorporar datos genómicos, clínicos y de imágenes médicas para una visión más holística, mejorando la calidad de los modelos predictivos.
- **Actualización Continua de Datos:** Implementar un sistema para la recolección continua de datos, permitiendo la actualización y refinamiento de modelos en tiempo real.

**4.2. Generación de Datos Sintéticos**

**Ampliación:**
- **Evaluación de Diferentes Técnicas de Generación:** Comparar CTGAN con otras técnicas de generación de datos sintéticos, como los Modelos Generativos Adversariales (GANs) o los Modelos Variacionales, para evaluar cuál ofrece una mejor replicación de los datos originales.

**Nuevos Puntos:**
- **Validación de Datos Sintéticos:** Implementar métodos de validación cruzada para asegurar que los datos sintéticos generados mantengan la integridad y la distribución de las relaciones entre variables.
- **Ensayo de Aplicación en Modelos:** Aplicar los datos sintéticos en diferentes etapas del proceso de modelado (pre-entrenamiento, fine-tuning) para evaluar su impacto en el rendimiento del modelo.

**4.3. Procesamiento de Datos**

**Ampliación:**
- **Imputación Avanzada:** Explorar técnicas avanzadas como la imputación basada en redes neuronales, métodos bayesianos, o imputación múltiple para mejorar el manejo de datos faltantes.

**Nuevos Puntos:**
- **Transformaciones de Datos:** Implementar transformaciones de datos como escalado, normalización, y técnicas de reducción de dimensionalidad (p.ej., PCA) para optimizar la calidad de los datos antes de su procesamiento.

**4.4. Replicación de Modelos de Referencia**

**Ampliación:**
- **Documentación Detallada:** Asegurarse de que toda la documentación del modelo de referencia esté completa para facilitar la replicación, incluyendo los parámetros exactos y el entorno de ejecución.

**Nuevos Puntos:**
- **Colaboración con los Creadores Originales:** Establecer colaboraciones con los autores de los modelos originales para obtener insights adicionales y asistencia en la replicación.

**4.5. Tendencia al Sobreajuste**

**Ampliación:**
- **Uso de Validación Cruzada Estratificada:** Implementar técnicas de validación cruzada estratificada para evaluar la robustez del modelo en diferentes subconjuntos de datos.
- **Modelos de Ensamble:** Continuar explorando modelos de ensamble, como Random Forests y Gradient Boosting, para combinar fortalezas de diversos modelos y reducir el riesgo de sobreajuste.

**Nuevos Puntos:**
- **Optimización de Hiperparámetros:** Utilizar técnicas de optimización automatizada como Grid Search y Random Search para ajustar hiperparámetros de manera más efectiva.
- **Regularización Avanzada:** Implementar técnicas avanzadas de regularización, como Dropout en redes neuronales, para combatir el sobreajuste.

**4.6. Ampliación y Refinamiento de Modelos**

**Ampliación:**
- **Exploración de Modelos Alternativos:** Evaluar nuevos modelos emergentes como Transformers y otros enfoques de aprendizaje profundo que podrían ofrecer mejoras en la predicción.

**Nuevos Puntos:**
- **Desarrollo de Modelos Personalizados:** Crear modelos personalizados adaptados específicamente a las características de los datos y el problema en cuestión, en lugar de depender únicamente de modelos preexistentes.

**4.7. Evaluación de Modelos No Supervisados**

**Ampliación:**
- **Análisis de Clustering Avanzado:** Realizar un análisis más profundo utilizando técnicas de clustering avanzadas (p.ej., clustering jerárquico, t-SNE) para identificar patrones ocultos en los datos.

**Nuevos Puntos:**
- **Integración con Modelos Supervisados:** Combinar resultados de modelos no supervisados con modelos supervisados para mejorar la precisión y la interpretación de las predicciones.

**4.8. Variabilidad en las Predicciones**

**Ampliación:**
- **Análisis de Sensibilidad:** Realizar un análisis de sensibilidad para entender cómo diferentes variables afectan las predicciones y mitigar la variabilidad en las probabilidades asignadas.

**Nuevos Puntos:**
- **Implementación de Técnicas de Ensayo y Error:** Introducir técnicas de ensayo y error para evaluar cómo diferentes enfoques y técnicas afectan la variabilidad en las predicciones.

**4.9. Mejoras Adicionales**

**Ampliación:**
- **Optimización de Modelos Existentes:** Continuar con el ajuste y optimización de modelos existentes, incorporando nuevas técnicas y herramientas que puedan surgir en el campo del machine learning.

**Nuevos Puntos:**
- **Análisis de Resultados en Diferentes Contextos:** Evaluar cómo los modelos se comportan en diferentes contextos clínicos y demográficos para asegurar que sean robustos y aplicables a diversas poblaciones.

### Conclusión Final Caminos Abiertos

Para avanzar en el desarrollo de modelos predictivos en cáncer, se deben abordar múltiples frentes simultáneamente: acceso a datos diversificados y actualizados, implementación de técnicas avanzadas de procesamiento y generación de datos, mejora continua de modelos mediante la exploración de enfoques nuevos y la reducción del sobreajuste. La combinación de estos esfuerzos contribuirá a la creación de modelos más robustos, confiables y aplicables a un rango más amplio de situaciones clínicas.

## 5. Referencias

1. Salazar-Jordan, Revista Nova. (2009). Cuantificación de ADN libre en plasma sanguíneo de voluntarios sanos en una población bogotana. Recuperado de [https://revistas.unicolmayor.edu.co/index.php/nova/article/view/139/279](https://revistas.unicolmayor.edu.co/index.php/nova/article/view/139/279)

2. Alfaro et al. (2014). Onco-proteogenomics: cancer proteomics joins forces with genomics. *Nature Methods*. [https://www.nature.com/articles/nmeth.3138](https://www.nature.com/articles/nmeth.3138)

3. Crick, F. H. C. (1958). On protein synthesis. *Symposium of the Society for Experimental Biology*. [PDF](https://d1wqtxts1xzle7.cloudfront.net/31353481/Symp_Soc_Exp_Biol_1958_Crick_on_protein_synthesis-libre.pdf)

4. Mi Yang et al. (2020). Community Assessment of the Predictability of Cancer Protein and Phosphoprotein Levels from Genomics and Transcriptomics. *Cell Systems, 11*(4), 352-360. [https://www.cell.com/cell-systems/fulltext/S2405-4712(20)30242-8](https://www.cell.com/cell-systems/fulltext/S2405-4712(20)30242-8)

5. Saez-Rodriguez et al. (2016). Crowdsourcing biomedical research: leveraging communities as innovation engines. *Nature Reviews Genetics, 17*(8), 470-486. [https://www.nature.com/articles/nrg.2016.69](https://www.nature.com/articles/nrg.2016.69)

6. Wu et al. (2020). Fine-mapping of 150 breast cancer risk regions identifies 191 likely target genes. *PubMed*. [https://pubmed.ncbi.nlm.nih.gov/31911677/](https://pubmed.ncbi.nlm.nih.gov/31911677/)

7. Wong et al. (2019). Early Cancer Detection from Multianalyte Blood Test Results. *iScience, 15*, 332-341. [https://doi.org/10.1016/j.isci.2019.04.035](https://doi.org/10.1016/j.isci.2019.04.035)

8. Cohen et al. (2018). Detection and localization of surgically resectable cancers with a multi-analyte blood test. *Science, 359*(6378), 926-930. [https://doi.org/10.1126/science.aar3247](https://doi.org/10.1126/science.aar3247)

9. Smith et al. (2019). Cancer screening in the United States, 2019: a review of current American Cancer Society guidelines and current issues in cancer screening. *CA: A Cancer Journal for Clinicians, 69*(3), 184-210. [https://doi.org/10.3322/caac.21557](https://doi.org/10.3322/caac.21557)

10. Hackshaw et al. (2022). New genomic technologies for multi-cancer early detection: Rethinking the scope of cancer screening. *Cancer Cell, 40*(2), 109-113. [https://doi.org/10.1016/j.ccell.2022.01.005](https://doi.org/10.1016/j.ccell.2022.01.005)

11. LeeVan, E., & Pinsky, P. (2024). Predictive performance of cell-free nucleic acid-based multi-cancer early detection tests: a systematic review. *Clinical Chemistry, 70*(1), 90-101. [https://doi.org/10.1093/clinchem/hvaa190](https://doi.org/10.1093/clinchem/hvaa190)

12. Klein et al. (2021). Clinical validation of a targeted methylation-based multi-cancer early detection test using an independent validation set. *Annals of Oncology, 32*(9), 1167-1177. [https://doi.org/10.1016/j.annonc.2021.06.003](https://doi.org/10.1016/j.annonc.2021.06.003)

13. Clinical Cancer Bulletin. (2022). Multi-cancer early detection tests: pioneering a revolution in cancer screening. *Springer*. [https://link.springer.com/article/10.1007/s10555-022-09965-4](https://link.springer.com/article/10.1007/s10555-022-09965-4)

14. DNA Science. (2024). Multi-cancer Early Detection Blood Tests (MCED) Debut. *PLoS*. [https://dnascience.plos.org/article/doi/10.1371/journal.pone.0274855](https://dnascience.plos.org/article/doi/10.1371/journal.pone.0274855)
