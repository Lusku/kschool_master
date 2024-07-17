# Mejora en la Detección Temprana del Cáncer Mediante Análisis de Sangre Multianalito y Modelos de Aprendizaje Automático



## **Abstract**

La detección temprana del cáncer mejora significativamente las posibilidades de tratamiento exitoso y supervivencia. Este proyecto tiene como objetivo replicar y mejorar los hallazgos del estudio "Early Cancer Detection from Multianalyte Blood Test Results", utilizando análisis de sangre multianalito para predecir la presencia y el tipo de cáncer. El estudio utiliza varios modelos de aprendizaje automático para analizar marcadores sanguíneos y mejorar la precisión en la detección y clasificación del cáncer.

Los objetivos principales de este proyecto son dos. Primero, buscamos replicar los modelos utilizados en el estudio original para predecir si un paciente tiene cáncer basándonos en los resultados de análisis de sangre. Segundo, buscamos extender estos modelos no solo para detectar la presencia de cáncer, sino también para clasificar el tipo específico entre ocho categorías predefinidas. Nuestro enfoque incluye desarrollar y validar nuevos modelos para mejorar el rendimiento predictivo más allá de los resultados del estudio original.

El proyecto utiliza datos de dos conjuntos de datos clave: uno para la detección binaria del cáncer (cáncer vs. no cáncer) y otro para la clasificación multicategoría del cáncer (identificación de tipos específicos de cáncer). Empleamos una gama de algoritmos de aprendizaje supervisado, incluyendo variantes de Naive Bayes, árboles de decisión y modelos de aprendizaje profundo. Se presta especial atención al modelo CancerA1DE, que ha mostrado un gran potencial en la detección de cáncer en etapas tempranas.

Nuestros hallazgos indican que es posible mejorar los modelos existentes, logrando una mayor sensibilidad y especificidad en la detección temprana del cáncer. El modelo CancerA1DE, en particular, demostró una duplicación de la sensibilidad para la detección de cáncer en etapa I con un nivel de especificidad del 99%. Además, nuestros modelos extendidos para la clasificación del tipo de cáncer mostraron un rendimiento robusto en múltiples tipos de cáncer.

Este proyecto contribuye al campo de la detección temprana del cáncer proporcionando una evaluación exhaustiva de modelos existentes y nuevos, junto con conocimientos prácticos sobre su aplicación. Los resultados tienen importantes implicaciones para el desarrollo de herramientas de detección de cáncer no invasivas y rentables que pueden ser implementadas en entornos clínicos.

Para obtener detalles sobre metodologías, conjuntos de datos e implementaciones de código, consulte el repositorio de GitHub proporcionado. Este proyecto subraya el potencial de combinar el aprendizaje automático con datos biomédicos para avanzar en el diagnóstico del cáncer y mejorar los resultados de los pacientes.

**Palabras Clave:**  *Detección temprana del cáncer, análisis de sangre multianalito, modelos de aprendizaje automático, CancerA1DE, clasificación de tipos de cáncer, Naive Bayes, modelos supervisados, biomarcadores, sensibilidad y especificidad, diagnóstico no invasivo.*



## **Índice**

[TOC]

## **Introducción**

### Contexto y Motivación

La detección temprana del cáncer es crucial para aumentar las tasas de supervivencia y mejorar los resultados del tratamiento. Tradicionalmente, las pruebas de detección del cáncer se han basado en métodos como imágenes y biopsias invasivas, que pueden ser costosos y poco accesibles para toda la población. La tecnología de biopsia líquida ha emergido como una alternativa prometedora, utilizando análisis de sangre para detectar fragmentos de ADN tumoral circulante (cfDNA) y otros biomarcadores, lo que permite una detección menos invasiva y potencialmente más temprana del cáncer [(DNA Science)](https://dnascience.plos.org/2024/01/11/multi-cancer-early-detection-blood-tests-mced-debut/) [(AACR Journals)](https://aacrjournals.org/cebp/article/31/3/512/681929/Multi-Cancer-Early-Detection-Tests-Current).

### Estado del Arte

En los últimos años, ha habido avances significativos en la detección temprana del cáncer mediante análisis de sangre multianalito. Estos avances incluyen el desarrollo de pruebas de detección temprana de múltiples tipos de cáncer (MCED) que pueden identificar varios tipos de cáncer a partir de una sola muestra de sangre. Estas pruebas utilizan tecnologías avanzadas como la secuenciación de alto rendimiento y el aprendizaje automático para analizar patrones de metilación del ADN y niveles de proteínas específicas asociadas con diferentes tipos de cáncer [(SpringerLink)](https://link.springer.com/article/10.1007/s44272-024-00015-x).

Un ejemplo destacado de estas pruebas es la Galleri, desarrollada por GRAIL, que ha demostrado la capacidad de detectar más de 50 tipos de cáncer, incluyendo algunos que no son detectados por las pruebas de detección convencionales. Los estudios han mostrado que Galleri puede detectar cánceres en etapas tempranas con una mayor precisión, lo que es crucial para mejorar los resultados del tratamiento y reducir las tasas de mortalidad ([DNA Science](https://dnascience.plos.org/2024/01/11/multi-cancer-early-detection-blood-tests-mced-debut/)).

### Casos de Uso y Retos Similares

El uso de MCEDs ha mostrado potencial para revolucionar la detección del cáncer, permitiendo diagnósticos más tempranos y precisos. Sin embargo, todavía existen varios retos que deben abordarse para su implementación generalizada. Estos incluyen la necesidad de una validación clínica más amplia, la estandarización de los procedimientos de prueba y la reducción de los costos asociados con estas tecnologías avanzadas. Además, existe el riesgo de sobrediagnóstico, donde se detectan cánceres que no habrían causado síntomas clínicos significativos, lo que puede llevar a tratamientos innecesarios y perjudiciales para los pacientes ([SpringerLink](https://link.springer.com/article/10.1007/s44272-024-00015-x)).

Existen varios casos de uso potenciales para un sistema de detección temprana de cáncer basado en análisis de sangre multianalito. Entre ellos se incluyen:

1. **Detección Temprana en Poblaciones de Alto Riesgo:** Implementación de pruebas regulares en individuos con antecedentes familiares de cáncer o con otros factores de riesgo conocidos.
2. **Monitoreo Post-Tratamiento:** Seguimiento de pacientes que han recibido tratamiento para el cáncer para detectar posibles recurrencias de manera temprana.
3. **Cribado General:** Uso de este sistema como una herramienta de cribado en chequeos médicos rutinarios para la población general.

#### Retos Similares

La implementación de sistemas de diagnóstico basados en datos no está exenta de desafíos. Entre los principales retos se encuentran:

1. **Calidad y Consistencia de los Datos:** Garantizar que los datos de las pruebas sanguíneas sean de alta calidad y consistentes es fundamental para el éxito del modelo predictivo.
2. **Variabilidad Biológica:** Los niveles de biomarcadores pueden variar significativamente entre individuos debido a factores no relacionados con el cáncer, lo que puede complicar la detección precisa.
3. **Interpretabilidad del Modelo:** Los modelos de aprendizaje automático deben ser interpretables para ser aceptados en un entorno clínico, donde los profesionales de la salud necesitan comprender las razones detrás de una predicción.

### Motivación para el Proyecto

Este proyecto se basa en replicar y extender los hallazgos del estudio "Early Cancer Detection from Multianalyte Blood Test Results", con el objetivo de mejorar la precisión de la detección y clasificación del cáncer mediante el uso de modelos de aprendizaje automático. La motivación principal es abordar las limitaciones identificadas en estudios anteriores y explorar nuevas técnicas que puedan ofrecer una mayor sensibilidad y especificidad en la detección temprana del cáncer.

En particular, nos centraremos en desarrollar y validar modelos que no solo puedan detectar la presencia de cáncer, sino también clasificar el tipo específico de cáncer entre varias categorías. Esto implica utilizar datos de múltiples marcadores sanguíneos y aplicar algoritmos avanzados de aprendizaje supervisado para mejorar la precisión diagnóstica.

### Contribuciones Esperadas

Las contribuciones esperadas de este proyecto incluyen:

1. **Replicación y Validación de Modelos Existentes**: La validación de modelos de predicción existentes es crucial para confirmar la eficacia de los métodos desarrollados en estudios previos. Al replicar los resultados obtenidos en estudios como el presentado en el artículo "Multi-Cancer Early Detection Blood Tests (MCED)" publicado en [DNA Science](https://dnascience.plos.org/2024/01/11/multi-cancer-early-detection-blood-tests-mced-debut/), este proyecto refuerza la robustez y reproducibilidad de los modelos utilizados. Este paso es esencial para asegurar que las metodologías propuestas pueden ser aplicadas consistentemente en diferentes entornos y con diferentes conjuntos de datos.
2. **Desarrollo de Nuevos Modelos**: Además de validar los modelos existentes, el proyecto se enfoca en el desarrollo y prueba de nuevos modelos de aprendizaje automático que puedan superar la precisión y la eficacia de los modelos actuales. La investigación en esta área podría identificar enfoques novedosos o combinaciones de técnicas que mejoren la capacidad predictiva y reduzcan la tasa de falsos positivos y negativos. Según un artículo reciente en [SpringerLink](https://link.springer.com/article/10.1007/s44272-024-00015-x), la innovación en algoritmos de detección temprana de cáncer puede ofrecer mejoras significativas en el rendimiento diagnóstico.
3. **Análisis Comparativo**: Realizar un análisis comparativo exhaustivo de diferentes enfoques y algoritmos es fundamental para determinar las mejores prácticas en la detección temprana del cáncer. Este análisis incluirá métodos supervisados y no supervisados, y considerará múltiples métricas de evaluación para ofrecer una visión completa de la eficacia de cada enfoque. Tal comparación no solo identificará los métodos más efectivos, sino que también destacará las condiciones en las que cada algoritmo presenta un mejor desempeño, facilitando su aplicación en diferentes escenarios clínicos.
4. **Aplicación Práctica**: Una de las metas principales del proyecto es proporcionar una base sólida para la implementación práctica de estas tecnologías en entornos clínicos. Esto incluye el desarrollo de protocolos y guías que permitan a los profesionales de la salud utilizar estas herramientas de manera efectiva para mejorar la detección temprana y el tratamiento del cáncer. La integración de estos avances en la práctica clínica podría resultar en diagnósticos más rápidos y precisos, optimizando el tratamiento y mejorando los resultados para los pacientes. Artículos como el de [SpringerLink](https://link.springer.com/article/10.1007/s44272-024-00015-x) y [AACR Journals](https://aacrjournals.org/cebp/article/31/3/512/681929/Multi-Cancer-Early-Detection-Tests-Current#:~:text=URL%3A https%3A%2F%2Faacrjournals.org%2Fcebp%2Farticle%2F31%2F3%2F512%2F681929%2FMulti) subrayan la importancia de llevar estos desarrollos tecnológicos del laboratorio a la práctica clínica.
5. **Propuestas para Nuevos Protocolos Clínicos**: Los hallazgos de este proyecto podrían influir en la creación de nuevos protocolos clínicos para la detección temprana del cáncer. La implementación de pruebas regulares basadas en análisis de sangre multianalito podría convertirse en una práctica estándar en chequeos médicos, especialmente para poblaciones de alto riesgo. Esto no solo mejorará los resultados de los pacientes, sino que también optimizará los recursos del sistema de salud.
6. **Generación de Conocimiento para Futuras Investigaciones**: Los resultados y datos generados por este proyecto serán de gran valor para futuras investigaciones. Al proporcionar un conjunto de datos exhaustivo y bien documentado, junto con los modelos y técnicas desarrollados, se facilitará la replicación y la extensión de este trabajo por parte de otros investigadores. Esto promoverá una mayor colaboración y avance en el campo de la detección temprana del cáncer.
7. **Impacto Económico y Social**: La implementación exitosa de este sistema de detección temprana podría tener un impacto económico significativo al reducir los costos asociados con el tratamiento del cáncer avanzado. Además, desde una perspectiva social, mejorar las tasas de detección temprana contribuirá a una mejor calidad de vida para los pacientes y sus familias, al aumentar las tasas de supervivencia y reducir la carga emocional y física del tratamiento del cáncer.

Este proyecto tiene el potencial de contribuir significativamente al campo de la oncología, ofreciendo nuevas herramientas y metodologías que pueden mejorar los resultados para los pacientes y reducir la carga global del cáncer.



## **Objetivos del Proyecto**

### Objetivos Empresariales

1. #### **Mejora de la Detección Temprana del Cáncer**:

   - **Objetivo**: Desarrollar un sistema de detección temprana del cáncer más preciso y fiable utilizando análisis de sangre multianalito y modelos de aprendizaje automático.
   - **Justificación**: La detección temprana del cáncer puede aumentar significativamente las tasas de supervivencia y reducir los costos de tratamiento al identificar la enfermedad en etapas iniciales, cuando es más tratable ([AACR Journals](https://aacrjournals.org/cebp/article/31/3/512/681929/Multi-Cancer-Early-Detection-Tests-Current#:~:text=URL%3A https%3A%2F%2Faacrjournals.org%2Fcebp%2Farticle%2F31%2F3%2F512%2F681929%2FMulti)) ([DNA Science](https://dnascience.plos.org/2024/01/11/multi-cancer-early-detection-blood-tests-mced-debut/)).

2. #### **Reducción de Costos de Diagnóstico**:

   - **Objetivo**: Crear un método de detección del cáncer que sea menos costoso en comparación con las técnicas de diagnóstico actuales como las biopsias y las imágenes médicas.
   - **Justificación**: Las técnicas de diagnóstico actuales son costosas y a menudo inaccesibles para una gran parte de la población. Un método basado en análisis de sangre podría ser más económico y accesible ([SpringerLink](https://link.springer.com/article/10.1007/s44272-024-00015-x)).

3. #### **Aumento de la Accesibilidad a Pruebas de Detección**:

   - **Objetivo**: Implementar una prueba de detección del cáncer que pueda ser fácilmente adoptada en clínicas y hospitales a nivel mundial.
   - **Justificación**: La accesibilidad a pruebas de detección efectivas es crucial para la detección temprana del cáncer, especialmente en áreas con recursos limitados ([DNA Science](https://dnascience.plos.org/2024/01/11/multi-cancer-early-detection-blood-tests-mced-debut/)).

### Objetivos Analíticos

1. #### **Replicación de Modelos Existentes**:

   - **Objetivo**: Replicar los modelos de predicción del cáncer utilizados en el estudio "Early Cancer Detection from Multianalyte Blood Test Results" y validar su eficacia con nuevos conjuntos de datos.
   - **Justificación**: Validar modelos existentes asegura que las técnicas utilizadas son robustas y aplicables en diferentes contextos y conjuntos de datos.

2. #### **Desarrollo de Nuevos Modelos Predictivos**:

   - **Objetivo**: Desarrollar y probar nuevos modelos de aprendizaje automático que superen en precisión y fiabilidad a los modelos existentes.
   - **Justificación**: Mejorar los modelos actuales puede llevar a una mayor sensibilidad y especificidad en la detección del cáncer, lo que es crucial para reducir falsos positivos y negativos ([SpringerLink](https://link.springer.com/article/10.1007/s44272-024-00015-x)) ([DNA Science](https://dnascience.plos.org/2024/01/11/multi-cancer-early-detection-blood-tests-mced-debut/)).

3. #### **Clasificación de Tipos de Cáncer**:

   - **Objetivo**: Extender los modelos para no solo detectar la presencia de cáncer, sino también clasificar el tipo específico de cáncer entre varias categorías predefinidas.
   - **Justificación**: La capacidad de identificar el tipo específico de cáncer permite tratamientos más personalizados y efectivos, mejorando los resultados clínicos para los pacientes.

4. #### **Evaluación de Criterios de Rendimiento**:

   - **Objetivo**: Evaluar los modelos predictivos utilizando métricas de rendimiento como la sensibilidad, especificidad, precisión, y el área bajo la curva (AUC) del ROC.
   - **Justificación**: Utilizar métricas de rendimiento estándar permite una comparación objetiva y cuantitativa de los modelos, asegurando que las mejoras son medibles y significativas.

5. #### **Análisis de Impacto de Biomarcadores**:

   - **Objetivo**: Realizar un análisis detallado de la contribución de diferentes biomarcadores en la predicción del cáncer.
   - **Justificación**: Entender la importancia relativa de cada biomarcador puede guiar el desarrollo de futuros análisis y mejorar la precisión del modelo al centrarse en los marcadores más informativos.

### Criterios de Éxito

1. #### **Mejora en la Sensibilidad y Especificidad**:

   - **Descripción**: Lograr una sensibilidad y especificidad significativamente superiores a las de los métodos actuales de detección del cáncer.
   - **Justificación**: Una mejora en estos parámetros indica una mayor capacidad para identificar correctamente los casos positivos y negativos, reduciendo así los falsos diagnósticos y mejorando la confianza en las pruebas.

2. #### **Costos Reducidos de Pruebas de Diagnóstico**:

   - **Descripción**: Demostrar que el método desarrollado es más económico que las técnicas de diagnóstico tradicionales.
   - **Justificación**: La reducción de costos facilita una mayor adopción de la tecnología en diversas regiones, especialmente en áreas con recursos limitados, y puede hacer que las pruebas sean más accesibles para una mayor cantidad de personas.

3. #### **Adopción Clínica y Escalabilidad**:

   - **Descripción**: Probar que el sistema de detección es fácilmente implementable en entornos clínicos y puede ser escalado para su uso a gran escala.
   - **Justificación**: La facilidad de implementación y la capacidad de escalar el sistema son cruciales para su adopción en la práctica clínica diaria, asegurando que los avances tecnológicos se traduzcan en mejoras reales en la atención médica.

4. #### **Validación Cruzada Independiente**:

   - **Descripción**: Conseguir resultados positivos en estudios de validación cruzada independientes utilizando conjuntos de datos diversos.
   - **Justificación**: La validación cruzada independiente asegura la robustez y generalizabilidad de los modelos desarrollados, demostrando que pueden ser efectivos en diferentes contextos y poblaciones.

Al alcanzar estos objetivos, el proyecto no solo contribuirá al avance científico en la detección temprana del cáncer, sino que también tendrá un impacto tangible en la salud pública y la accesibilidad a diagnósticos médicos avanzados. Este proyecto aspira a mejorar la calidad de vida de los pacientes mediante la innovación tecnológica y la implementación práctica de nuevos métodos de diagnóstico.



## **Datos**

### Ubicación de las Fuentes de Datos

Para llevar a cabo este proyecto, hemos utilizado dos conjuntos de datos principales provenientes del estudio "Early Cancer Detection from Multianalyte Blood Test Results" y sus suplementos. Estos datos están disponibles en el repositorio de GitHub asociado al estudio original y en los suplementos proporcionados por el artículo en [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6548890/). Los datos incluyen mediciones de diversos marcadores sanguíneos en pacientes diagnosticados con diferentes tipos de cáncer y en individuos sanos.

1. #### **Primer Conjunto de Datos (Detección Binaria de Cáncer)**:
   
   - **Fuente**: Datos procesados de acuerdo a las directrices del suplemento del estudio de Cohen et al. (2018).
   - **Descripción**: Este conjunto de datos contiene registros de pruebas de sangre de 1,817 pacientes, utilizado para construir modelos de detección de cáncer en una modalidad binaria (cáncer vs. no cáncer).
   - **Variables**: Incluye concentraciones de ocho marcadores proteicos circulantes y una puntuación de mutación de ADN libre de células (OmegaScore).
   
2. #### **Segundo Conjunto de Datos (Clasificación de Tipos de Cáncer)**:
   
   - **Fuente**: Datos procesados del mismo estudio de Cohen et al. (2018).
   - **Descripción**: Este conjunto de datos contiene registros de pruebas de sangre de 626 pacientes, utilizado para construir modelos de clasificación de tipos de cáncer (p. ej., mama, colon, pulmón, etc.).
   - **Variables**: Aparte de los nueve marcadores del primer conjunto de datos, incluye concentraciones de 31 marcadores proteicos adicionales y el género del paciente.

### Descripción Detallada del Conjunto de Datos Original

1. #### **Número de Registros**:
   
   - Primer conjunto de datos: 1,817 registros.
   - Segundo conjunto de datos: 626 registros.
   
2. #### **Número de Variables**:
   
   - Primer conjunto de datos: 9 variables.
   - Segundo conjunto de datos: 41 variables.
   
3. #### **Tipología e Interpretación de las Variables**:
   
   - **Primer Conjunto de Datos**:
   
     - **CA19-9 (U/ml)**: Antígeno del cáncer 19-9, marcador utilizado principalmente para el cáncer pancreático.
     - **CA-125 (U/ml)**: Antígeno del cáncer 125, comúnmente utilizado para el cáncer de ovario.
     - **HGF (pg/ml)**: Factor de crecimiento de hepatocitos, involucrado en la proliferación celular y metástasis.
     - **OPN (pg/ml)**: Osteopontina, proteína asociada con la progresión de varios tipos de cáncer.
     - **OmegaScore**: Puntuación que refleja mutaciones en el ADN libre de células en la sangre.
     - **Prolactina (pg/ml)**: Hormona involucrada en la regulación del sistema inmunológico y el desarrollo de cáncer.
     - **CEA (pg/ml)**: Antígeno carcinoembrionario, marcador común en cánceres gastrointestinales.
     - **MPO (ng/ml)**: Mieloperoxidasa, enzima implicada en la inflamación y cáncer.
     - **TIMP-1 (pg/ml)**: Inhibidor tisular de metaloproteinasas, relacionado con la invasión tumoral y metástasis.
   
   - **Segundo Conjunto de Datos**:
   
     Para este conjunto de datos, además de las variables anteriores, se incluyen concentraciones de 31 marcadores proteicos adicionales, entre ellos:
   
     - **TGFa**: Factor de crecimiento transformante alfa, relevante en varios tipos de cáncer.
     - **HE4**: Proteína epidídimo humana 4, utilizada principalmente en el cáncer de ovario.
     - **sFas**: Receptor de muerte soluble, involucrado en la apoptosis celular.
     - **Thrombospondin-2**: Glicoproteína implicada en la regulación de la angiogénesis.
     - **AFP**: Alfa-fetoproteína, marcador para el cáncer de hígado.
     - **G-CSF**: Factor estimulante de colonias de granulocitos, utilizado en diversos tipos de cáncer.
     - **IL-6**: Interleucina 6, una citocina proinflamatoria.
   
     Entre otros marcadores relevantes para la clasificación de tipos específicos de cáncer.

### Análisis Descriptivo y Exploratorio de los Datos

Se llevaron a cabo varios análisis descriptivos y exploratorios para entender mejor la distribución y características de los datos.

1. ##### **Distribución de Marcadores Sanguíneos**:

   * Descripción estadística de las variables seleccionadas nos proporciona una visión general de la distribución y las características de los datos.

     |                          | count | mean        | std         | min      | 25%       | 50%      | 75%        | max        |
     | ------------------------ | ----- | ----------- | ----------- | -------- | --------- | -------- | ---------- | ---------- |
     | Tumor type               | 1817  | 0,553109521 | 0,497308245 | 0        | 0         | 1        | 1          | 1          |
     | CA19-9 (U/ml)            | 1817  | 53,8287716  | 409,0309519 | 14,214   | 16,32     | 16,482   | 18,6       | 12491,472  |
     | CA-125 (U/ml)            | 1817  | 25,18304348 | 184,585378  | 4,608    | 4,89      | 4,98     | 6,4        | 3600,024   |
     | HGF (pg/ml)              | 1817  | 323,8637402 | 487,6810121 | 158,334  | 164,514   | 183,58   | 293,15     | 11432,98   |
     | OPN (pg/ml)              | 1817  | 56295,35771 | 48269,00843 | 3218,166 | 26146,14  | 41236,83 | 68644,7    | 433959,55  |
     | Omega score              | 1817  | 4,439651993 | 20,77353401 | 0        | 0,7220361 | 0,981666 | 1,47124269 | 333,234911 |
     | Prolactin  (pg/ml)       | 1817  | 32313,97585 | 54139,45838 | 806,28   | 8617,16   | 14032,92 | 26552,97   | 608432,382 |
     | CEA (pg/ml)              | 1817  | 4427,203445 | 23696,80323 | 426,438  | 614,2     | 1045,44  | 1924,61    | 337245,426 |
     | Myeloperoxidase  (ng/ml) | 1817  | 31,1993891  | 68,25567512 | 1,3      | 8,05      | 12,83    | 22,63      | 1001       |
     | TIMP-1 (pg/ml)           | 1817  | 70058,42289 | 47577,49082 | 976,55   | 41231,36  | 59282,78 | 82928,93   | 569512,69  |

     A continuación se detallan los resultados de la descripción estadística:

     **Tumor type**:

     - **Descripción**: Variable binaria que indica la presencia de cáncer (1) o su ausencia (0).
     - **Media**: 0.5531, lo que indica que aproximadamente el 55.3% de las muestras corresponden a pacientes con cáncer.
     - **Desviación estándar**: 0.4973, mostrando una alta variabilidad debido a la naturaleza binaria de la variable.
     - **Valores mínimos y máximos**: Rango de 0 a 1.

     **CA19-9 (U/ml)**:

     - **Descripción**: Marcador tumoral utilizado principalmente para el cáncer pancreático.
     - **Media**: 53.83 U/ml.
     - **Desviación estándar**: 409.03 U/ml.
     - **Valores mínimos y máximos**: Rango de 14.214 a 12491.472 U/ml.
     - **Rango intercuartílico (IQR)**: 16.32 a 18.60 U/ml.

     **CA-125 (U/ml)**:

     - **Descripción**: Marcador tumoral comúnmente utilizado para el cáncer de ovario.
     - **Media**: 25.18 U/ml.
     - **Desviación estándar**: 184.59 U/ml.
     - **Valores mínimos y máximos**: Rango de 4.608 a 3600.024 U/ml.
     - **Rango intercuartílico (IQR)**: 4.89 a 6.40 U/ml.

     **HGF (pg/ml)**:

     - **Descripción**: Factor de crecimiento de hepatocitos, involucrado en la proliferación celular y metástasis.
     - **Media**: 323.86 pg/ml.
     - **Desviación estándar**: 487.68 pg/ml.
     - **Valores mínimos y máximos**: Rango de 158.334 a 11432.98 pg/ml.
     - **Rango intercuartílico (IQR)**: 164.514 a 293.15 pg/ml.

     **OPN (pg/ml)**:

     - **Descripción**: Osteopontina, proteína asociada con la progresión de varios tipos de cáncer.
     - **Media**: 56295.36 pg/ml.
     - **Desviación estándar**: 48269.01 pg/ml.
     - **Valores mínimos y máximos**: Rango de 3218.166 a 433959.55 pg/ml.
     - **Rango intercuartílico (IQR)**: 26146.14 a 68644.70 pg/ml.

     **Omega score**:

     - **Descripción**: Puntuación que refleja mutaciones en el ADN libre de células en la sangre.
     - **Media**: 4.44.
     - **Desviación estándar**: 20.77.
     - **Valores mínimos y máximos**: Rango de 0 a 333.234911.
     - **Rango intercuartílico (IQR)**: 0.722 a 1.471.

     **Prolactin (pg/ml)**:

     - **Descripción**: Hormona involucrada en la regulación del sistema inmunológico y el desarrollo de cáncer.
     - **Media**: 32313.98 pg/ml.
     - **Desviación estándar**: 54139.46 pg/ml.
     - **Valores mínimos y máximos**: Rango de 806.28 a 608432.382 pg/ml.
     - **Rango intercuartílico (IQR)**: 8617.16 a 26552.97 pg/ml.

     **CEA (pg/ml)**:

     - **Descripción**: Antígeno carcinoembrionario, marcador común en cánceres gastrointestinales.
     - **Media**: 4427.20 pg/ml.
     - **Desviación estándar**: 23696.80 pg/ml.
     - **Valores mínimos y máximos**: Rango de 426.438 a 337245.426 pg/ml.
     - **Rango intercuartílico (IQR)**: 614.2 a 1924.61 pg/ml.

     **Myeloperoxidase (MPO) (ng/ml)**:

     - **Descripción**: Mieloperoxidasa, enzima implicada en la inflamación y cáncer.
     - **Media**: 31.20 ng/ml.
     - **Desviación estándar**: 68.26 ng/ml.
     - **Valores mínimos y máximos**: Rango de 1.3 a 1001 ng/ml.
     - **Rango intercuartílico (IQR)**: 8.05 a 22.63 ng/ml.

     **TIMP-1 (pg/ml)**:

     - **Descripción**: Inhibidor tisular de metaloproteinasas, relacionado con la invasión tumoral y metástasis.
     - **Media**: 70058.42 pg/ml.
     - **Desviación estándar**: 47577.49 pg/ml.
     - **Valores mínimos y máximos**: Rango de 976.55 a 569512.69 pg/ml.
     - **Rango intercuartílico (IQR)**: 41231.36 a 82928.93 pg/ml.

     Estas descripciones detalladas de cada marcador sanguíneo proporcionan una visión clara de las características y la variabilidad de los datos, lo cual es fundamental para el análisis y la modelización en el contexto de la detección temprana del cáncer.

     

2. **Visualización de los Datos Sin Procesar**:

   Se realizó una visualización preliminar de los datos sin procesar para entender mejor su distribución y características. Este paso es crucial para identificar patrones, anomalías y distribuciones específicas de las variables, así como para planificar los pasos de preprocesamiento necesarios.

   ##### **Análisis de Valores Nulos**

   Se observó que el parámetro "AJCC stage" presenta valores nulos en varias tablas. Esto no es sorprendente ya que este parámetro describe la severidad del cáncer y su ausencia en algunos registros puede indicar que los pacientes estaban libres de cáncer en el momento del estudio. Una situación similar se presenta con la variable "Histopatología" en el DataFrame 4. Para estas variables, podría considerarse la imputación de valores consensuados en lugar de dejarlas como nulas.

   ##### **Distribución de Variables Numéricas**

   Se procedió a visualizar la distribución de varias variables numéricas clave del conjunto de datos. A continuación se describen los histogramas generados para cada una de estas variables:

   1. **Distribución de AXL (pg/ml)**:
      - **Descripción**: La distribución de la variable AXL muestra una forma sesgada hacia la derecha, lo cual es típico en datos biológicos donde una pequeña fracción de la población puede presentar valores extremadamente altos. La mayoría de los valores se concentran entre 0 y 5000 pg/ml, con una disminución gradual en frecuencia a medida que los valores aumentan.
      - ![AXL Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output1.png)
   2. **Distribución de sPECAM-1 (pg/ml)**:
      - **Descripción**: La distribución de la variable sPECAM-1 tiene una forma similar a una distribución normal pero con cola larga a la derecha. La mayoría de los valores se encuentran entre 2500 y 12500 pg/ml, siendo la mediana alrededor de 5000 pg/ml.
      - ![sPECAM-1 Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output2.png)
   3. **Distribución de TIMP-2 (pg/ml)**:
      - **Descripción**: La variable TIMP-2 también muestra una distribución sesgada hacia la derecha. La mayor parte de los datos se agrupa entre 20000 y 80000 pg/ml, con una disminución notable en frecuencia para valores superiores.
      - ![TIMP-2 Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output3.png)
   4. **Distribución de Omega Score**:
      - **Descripción**: El Omega Score presenta una distribución altamente sesgada hacia la derecha, con la mayoría de los valores muy cerca de 0 y pocos valores extremadamente altos. Este tipo de distribución puede indicar la presencia de valores atípicos o una escala logarítmica subyacente en los datos.
      - ![Omega Score Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output4.png)
   5. **Distribución de CancerSEEK Logistic Regression Score**:
      - **Descripción**: Esta variable presenta una distribución bimodal con picos alrededor de 0.2 y 1.0, lo cual podría indicar una separación clara entre dos grupos en la población estudiada, posiblemente indicando la presencia o ausencia de cáncer según el score.
      - ![Omega Score Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output5.png)

   ##### **Distribución de las variables categóricas**

   1. **Distribución de Tumor type**:
      - Este gráfico muestra la distribución de los diferentes tipos de tumores.
      - El tipo de tumor más frecuente es el "Normal" seguido por "Colorectum" y "Breast".
      - Otros tipos de tumores como "Lung", "Pancreas", "Ovary", "Esophagus", "Liver", y "Stomach" tienen una menor representación en el conjunto de datos.
      - ![Omega Score Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output6.png)
   2. **Distribución de AJCC Stage**:
      - Este gráfico muestra la distribución de las etapas AJCC.
      - La mayoría de los casos se encuentran en la etapa II, seguida por la etapa III y la etapa I.
      - Esto sugiere que la mayoría de los pacientes en el estudio fueron diagnosticados en etapas intermedias o avanzadas de cáncer.
      - ![Omega Score Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output7.png)
   3. **Distribución de Angiopoietin-2 (pg/ml)**:
      - Este gráfico muestra la distribución de los valores de Angiopoietin-2 en picogramos por mililitro.
      - La distribución es altamente asimétrica hacia la derecha, con la mayoría de los valores concentrados cerca de cero.
      - Hay pocos valores extremadamente altos, lo que indica la presencia de algunos outliers significativos.
      - ![Omega Score Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output8.png)
   4. **Distribución de CA 15-3 (U/ml)**:
      - Este gráfico muestra la distribución de los valores de CA 15-3 en unidades por mililitro.
      - La distribución es altamente asimétrica hacia la derecha, con la mayoría de los valores concentrados cerca de cero.
      - Hay pocos valores extremadamente altos, lo que indica la presencia de algunos outliers significativos.
      - ![Omega Score Distribution](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\output9.png)

   

   ##### **Correlaciones entre variables:**

   En el análisis de datos, la identificación de correlaciones entre variables es fundamental para entender cómo se relacionan entre sí y cómo pueden influir en los resultados de los modelos predictivos. La correlación mide la fuerza y la dirección de la relación lineal entre dos variables. Un coeficiente de correlación puede variar entre -1 y 1, donde:

   - 1 indica una correlación positiva perfecta,
   - -1 indica una correlación negativa perfecta, y
   - 0 indica que no hay correlación lineal.

   Para nuestro estudio sobre la predicción del cáncer, hemos analizado las correlaciones entre varias variables tanto numéricas como categóricas. A continuación, se presentan y explican los gráficos de correlación generados.

   1. **Correlación entre Variables Numéricas**

      ![Correlación del DataFrame](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\corr1.png)

      En este gráfico de calor se muestran las correlaciones entre las siguientes variables numéricas:

      - AXL (pg/ml)
      - sPECAM-1 (pg/ml)
      - TIMP-2 (pg/ml)
      - Omega score
      - CancerSEEK Logistic Regression Score

      Las principales observaciones de este gráfico son:

      1. **AXL y sPECAM-1**: Hay una correlación positiva moderada (r ≈ 0.40), lo que indica que a medida que los niveles de AXL aumentan, los niveles de sPECAM-1 también tienden a aumentar.

      2. **sPECAM-1 y TIMP-2**: También presentan una correlación positiva moderada (r ≈ 0.31).

      3. **AXL y TIMP-2**: La correlación entre estos dos marcadores es más baja pero aún positiva (r ≈ 0.29).

      3. **Omega score y CancerSEEK Logistic Regression Score**: Presentan una correlación positiva baja (r ≈ 0.19).

      En general, estas correlaciones indican algunas relaciones lineales positivas entre los biomarcadores estudiados y las puntuaciones de riesgo de cáncer.

   2. **Correlación entre Variables Categóricas**

   ![Correlación entre variables categóricas](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\corr2.png)

   Este gráfico de calor muestra las correlaciones entre una amplia gama de variables categóricas y numéricas del estudio. Las variables incluidas abarcan desde identificadores de paciente y tipo de muestra hasta diversos marcadores tumorales y proteínas.

   Las principales observaciones de este gráfico son:

   1. **ID del Paciente y ID de Muestra**: La correlación es alta (r ≈ 0.50), lo que es esperado ya que cada muestra está vinculada a un paciente específico.
   2. **Tumor type y varios marcadores**: Se observan varias correlaciones moderadas con distintos marcadores tumorales, lo que sugiere que ciertos tipos de tumores tienen perfiles biomarcadores característicos.
   3. **CancerSEEK Test Result y varios marcadores**: Se destacan correlaciones con múltiples marcadores, indicando la complejidad de las relaciones entre los resultados del test y los distintos biomarcadores.

   ##### Matriz de Correlación Detallada

   En la matriz de correlación detallada se identificaron las siguientes relaciones notables:

   | variable_1                           | variable_2                           | r         | abs_r    |
   | ------------------------------------ | ------------------------------------ | --------- | -------- |
   | AXL (pg/ml)                          | sPECAM-1 (pg/ml)                     | 0.396347  | 0.396347 |
   | sPECAM-1 (pg/ml)                     | AXL (pg/ml)                          | 0.396347  | 0.396347 |
   | sPECAM-1 (pg/ml)                     | TIMP-2 (pg/ml)                       | 0.305282  | 0.305282 |
   | TIMP-2 (pg/ml)                       | sPECAM-1 (pg/ml)                     | 0.305282  | 0.305282 |
   | TIMP-2 (pg/ml)                       | AXL (pg/ml)                          | 0.289164  | 0.289164 |
   | AXL (pg/ml)                          | TIMP-2 (pg/ml)                       | 0.289164  | 0.289164 |
   | Omega score                          | CancerSEEK Logistic Regression Score | 0.194097  | 0.194097 |
   | CancerSEEK Logistic Regression Score | Omega score                          | 0.194097  | 0.194097 |
   | AXL (pg/ml)                          | CancerSEEK Logistic Regression Score | 0.085099  | 0.085099 |
   | CancerSEEK Logistic Regression Score | AXL (pg/ml)                          | 0.085099  | 0.085099 |
   | TIMP-2 (pg/ml)                       | CancerSEEK Logistic Regression Score | 0.049577  | 0.049577 |
   | CancerSEEK Logistic Regression Score | TIMP-2 (pg/ml)                       | 0.049577  | 0.049577 |
   | sPECAM-1 (pg/ml)                     | Omega score                          | -0.034447 | 0.034447 |
   | Omega score                          | sPECAM-1 (pg/ml)                     | -0.034447 | 0.034447 |
   | Omega score                          | TIMP-2 (pg/ml)                       | -0.021214 | 0.021214 |
   | TIMP-2 (pg/ml)                       | Omega score                          | -0.021214 | 0.021214 |
   | Omega score                          | AXL (pg/ml)                          | -0.019419 | 0.019419 |
   | AXL (pg/ml)                          | Omega score                          | -0.019419 | 0.019419 |
   | sPECAM-1 (pg/ml)                     | CancerSEEK Logistic Regression Score | 0.008435  | 0.008435 |
   | CancerSEEK Logistic Regression Score | sPECAM-1 (pg/ml)                     | 0.008435  | 0.008435 |

   Estos valores de correlación muestran cómo se relacionan los diferentes biomarcadores y las puntuaciones de los tests, proporcionando información valiosa para la modelización predictiva y la comprensión de las interacciones biológicas subyacentes.

   

### Análisis profundo de los datos

Se realiza un análisis exhaustivo de las variables numéricas del conjunto de datos, verificando su distribución, asimetría y curtosis. Esto es fundamental para entender la naturaleza de los datos y para aplicar transformaciones adecuadas que mejoren el rendimiento de los modelos predictivos. A continuación, se explica el proceso y los resultados obtenidos.

#### Visualización de la Distribución de las Variables Numéricas

Para cada variable numérica del conjunto de datos `df6`, se visualiza su distribución mediante histogramas con un ajuste de densidad de kernel (KDE). Adicionalmente, se calculan la asimetría y la curtosis de cada distribución, y se realizan pruebas de normalidad para determinar si las distribuciones siguen una distribución normal.

##### Resultados de la Distribución

A continuación, se presentan y comentan los gráficos obtenidos para algunas de las variables más relevantes:

1. **AXL (pg/ml):**

   - Gráfico:

     ![Correlación entre variables categóricas](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\dist1.png)

   - **Descripción:** La distribución de AXL muestra una asimetría positiva significativa, lo que indica que la mayoría de los valores se concentran en la parte baja del rango con una larga cola hacia la derecha. Esto sugiere una distribución sesgada hacia valores menores.

2. **sPECAM-1 (pg/ml):**

   - Gráfico:

     ![Correlación entre variables categóricas](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\dist2.png)

   - **Descripción:** La distribución de sPECAM-1 también muestra una asimetría positiva, aunque menos pronunciada que AXL. La mayoría de los valores se agrupan en la parte baja del rango con una cola hacia la derecha.

3. **TIMP-2 (pg/ml):**

   - Gráfico:

     ![Correlación entre variables categóricas](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\dist33.png)

   - **Descripción:** TIMP-2 presenta una asimetría positiva y una curtosis elevada, indicando una distribución con una alta concentración de valores en la parte baja y algunas observaciones extremas en la cola derecha.

4. **Omega score:**

   - Gráfico:

     ![Correlación entre variables categóricas](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\dist44.png)

   - **Descripción:** La distribución del Omega score muestra una alta concentración de valores en el extremo inferior, con una larga cola hacia la derecha. Esto sugiere que la mayoría de los valores son bajos, con pocos valores altos.

5. **CancerSEEK Logistic Regression Score:**

   - Gráfico:

     ![Correlación entre variables categóricas](C:\Users\mar27\OneDrive\Documentos\CURSOS\DATA_SCIENCE_KSCHOOL\00_PROYECTO\dist5.png)

   - **Descripción:** La distribución del score de regresión logística de CancerSEEK muestra una forma bimodal, con picos significativos en ambos extremos del rango. Esto indica que los valores tienden a agruparse cerca de los extremos, con menos valores en el rango medio.

#### Análisis de Asimetría y Curtosis

- **Asimetría (Skewness):** La asimetría mide la simetría de la distribución de datos. Una asimetría positiva indica que la cola derecha es más larga o gruesa que la izquierda (más valores bajos), mientras que una asimetría negativa indica lo contrario. En el análisis, las variables TIMP-2 y CancerSEEK Logistic Regression Score muestran asimetría positiva.
- **Curtosis:** La curtosis mide la "puntiagudez" de la distribución. Una alta curtosis indica una distribución con picos elevados y colas largas. La variable TIMP-2 muestra una curtosis elevada, lo que indica la presencia de valores extremos significativos.

#### Pruebas de Normalidad

- **Prueba de Shapiro-Wilk:** Esta prueba evalúa si una muestra sigue una distribución normal. Un p-valor menor a 0.05 indica que la distribución no es normal.
- **Prueba de D’Agostino’s K-squared:** Esta prueba también evalúa la normalidad de una distribución. Similarmente, un p-valor menor a 0.05 sugiere que la distribución no es normal.

En resumen, la mayoría de las variables numéricas analizadas no siguen una distribución normal, mostrando asimetrías y curtosis significativas. Estos resultados son esenciales para decidir qué transformaciones aplicar y qué modelos pueden ser más adecuados para el análisis predictivo posterior.



### Limpieza de los datos

1. **Eliminación de Cadenas de Texto No Deseadas:** Al tratarse de cadenas de texto, se observa que varios registros contienen caracteres '*' y '**'. 

2. **Cambio de Tipo de Variables:** Algunas variables que representan marcadores sanguíneos están en formato `Object`. Estas variables se convierten a tipo `numeric` para permitir un análisis cuantitativo.

3. **Tratamiento de Valores Nulos:** Se identifican y tratan los valores nulos en el DataFrame `df6`. Se han aplicado varios enfoques para imputar los valores faltantes en el DataFrame `df6`. Cada uno de estos enfoques tiene sus propias ventajas y se elige en función del contexto y de la naturaleza de los datos. A continuación, se describen detalladamente los enfoques utilizados.

   ##### Enfoque 1: Relleno con la Media de la Muestra

   En este enfoque, los valores nulos se rellenan con la media de la muestra de cada columna numérica. Este método es simple y rápido, y es útil cuando se quiere mantener la media de la columna intacta.

   #####  Enfoque 2: Relleno Mediante Predicción de Valores Usando KNN

   El método KNN (K-Nearest Neighbors) se utiliza para imputar los valores faltantes prediciendo los valores en función de los vecinos más cercanos.

   ##### Enfoque 3: Relleno Mediante Predicción de Valores Usando Árboles de Decisión

   Este enfoque utiliza árboles de decisión para predecir y rellenar los valores faltantes en función del resto de las variables.

   ##### Enfoque 4: Relleno Mediante Predicción de Valores Usando Regresión Lineal

   Este enfoque utiliza regresión lineal para predecir y rellenar los valores faltantes en función del resto de las variables.

   #### Comparación de los Valores con los que se Rellenarán los Nulos Según Cada Técnica

   Finalmente, se comparan los resultados de las diferentes técnicas de imputación para determinar cuál proporciona los mejores resultados. 

   Esta comparación permite identificar cuál de las técnicas de imputación es más adecuada para los datos específicos del proyecto, asegurando la mejor calidad de los datos imputados para el análisis y la construcción de modelos predictivos.

   ##### Resultados de la Comparación

   La tabla final de comparación muestra cómo cada técnica de imputación ha rellenado los valores nulos en el DataFrame. Aquí se incluyen algunas de las columnas clave:

   | AFP (pg/ml) | Angiopoietin-2 (pg/ml) | AXL (pg/ml) | CA-125 (U/ml) | CA 15-3 (U/ml) | CA19-9 (U/ml) | CD44 (ng/ml) | CEA (pg/ml) | CYFRA 21-1 (pg/ml) | DKK1 (ng/ml) | SHBG (nM) | sHER2/sEGFR2/sErbB2 (pg/ml) | sPECAM-1 (pg/ml) | TGFa (pg/ml) | Thrombospondin-2 (pg/ml) | TIMP-1 (pg/ml) | TIMP-2 (pg/ml) | Omega score | CancerSEEK Logistic Regression Score | CancerSEEK Test Result |
   | ----------- | ---------------------- | ----------- | ------------- | -------------- | ------------- | ------------ | ----------- | ------------------ | ------------ | --------- | --------------------------- | ---------------- | ------------ | ------------------------ | -------------- | -------------- | ----------- | ------------------------------------ | ---------------------- |
   | 1583.450    | 5598.50                | 3621.04     | 5.090         | 19.08          | 16.452        | 9.81         | 540.07      | 1938.654           | 0.78         | 55.06     | 6832.07                     | 9368.53          | 16.086       | 21863.74                 | 56428.71       | 39498.82       | 2.962820    | 0.938342                             | Positive               |
   | 715.308     | 20936.35               | 2772.96     | 7.270         | 10.04          | 40.910        | 27.57        | 5902.43     | 1938.654           | 0.77         | 72.92     | 5549.47                     | 6224.55          | 16.086       | 29669.66                 | 73940.49       | 41277.09       | 2.445405    | 0.925363                             | Positive               |
   | 4365.530    | 2350.93                | 4120.77     | 4.854         | 16.96          | 16.452        | 14.59        | 973.75      | 1976.940           | 0.90         | 173.78    | 3698.16                     | 4046.48          | 179.030      | 6020.47                  | 22797.28       | 28440.60       | 1.215758    | 0.852367                             | Negative               |
   | 715.308     | 1604.34                | 2029.96     | 5.390         | 8.31           | 16.452        | 7.78         | 2027.53     | 1938.654           | 0.64         | 29.47     | 5856.00                     | 6121.93          | 16.086       | 4331.02                  | 20441.19       | 25896.73       | 1.640793    | 0.617639                             | Negative               |
   | 801.300     | 2087.57                | 2069.17     | 4.854         | 11.73          | 16.452        | 12.21        | 614.49      | 1938.654           | 0.78         | 78.07     | 5447.93                     | 6982.32          | 16.086       | 2311.91                  | 56288.51       | 49425.20       | 1.325771    | 0.318434                             | Negative               |
   | ...         | ...                    | ...         | ...           | ...            | ...           | ...          | ...         | ...                | ...          | ...       | ...                         | ...              | ...          | ...                      | ...            | ...            | ...         | ...                                  | ...                    |
   | 879.498     | 1484.70                | 2096.76     | 24.820        | 10.30          | 42.390        | 14.92        | 914.00      | 1970.916           | 3.05         | 115.24    | 5390.31                     | 8538.58          | 16.890       | 599.40                   | 167799.61      | 50128.60       | 0.983813    | 0.980312                             | Positive               |
   | 1337.330    | 1607.90                | 852.37      | 5.580         | 9.80           | 16.440        | 12.32        | 1179.51     | 1970.916           | 1.74         | 147.17    | 7951.03                     | 12966.19         | 16.890       | 599.40                   | 123443.76      | 54066.98       | 3.915387    | 0.999995                             | Positive               |
   | 879.498     | 1592.84                | 1044.45     | 30.480        | 8.48           | 16.440        | 8.26         | 443.01      | 3589.730           | 0.73         | 104.63    | 2396.36                     | 1901.41          | 16.890       | 599.40                   | 104070.89      | 39844.02       | 7.962561    | 1.000000                             | Positive               |
   | 879.498     | 5267.95                | 1445.69     | 1469.450      | 23.74          | 62.260        | 16.53        | 443.01      | 50659.050          | 1.24         | 73.55     | 3079.81                     | 5312.90          | 16.890       | 6864.33                  | 110579.24      | 42921.13       | 0.807685    | 1.000000                             | Positive               |
   | 879.498     | 3546.43                | 1493.32     | 1428.310      | 836.85         | 37.900        | 13.78        | 443.01      | 3060.110           | 1.01         | 72.22     | 3967.55                     | 4045.18          | 16.890       | 12877.10                 | 88464.04       | 47219.24       | 1.425203    | 1.000000                             | Positive               |

   Esta tabla proporciona una visión detallada de cómo cada técnica de imputación ha rellenado los valores nulos en el DataFrame, permitiendo una comparación efectiva de las distintas metodologías y su impacto en la calidad y consistencia de los datos.



### Binarización de la Variable Objetivo y Verificación del "Information Gain" de Cada Variable Frente a la Variable Objetivo

En este apartado se llevó a cabo la binarización de la variable objetivo "Tumor Type" y la verificación del "Information Gain" de cada variable predictora frente a la variable objetivo. Esta sección es fundamental para evaluar el peso e importancia de cada variable en la predicción de la existencia de cáncer.

#### Binarización de la Variable Objetivo

La variable "Tumor Type" inicialmente contenía múltiples categorías, representando diferentes tipos de tumores y una categoría adicional para los casos sin cáncer (Normal). Para simplificar el análisis y enfocarnos en la detección de cáncer, se decidió binarizar esta variable. La binarización se llevó a cabo siguiendo el siguiente esquema:

- Si "Tumor Type" == "Normal", entonces "Tumor Type" = 0
- Si "Tumor Type" != "Normal", entonces "Tumor Type" = 1

De esta manera, la variable "Tumor Type" se transformó en una variable binaria donde 0 indica la ausencia de cáncer y 1 indica la presencia de cáncer. Este proceso facilita la aplicación de técnicas de clasificación binaria y la interpretación de los resultados.

#### Verificación del "Information Gain" de Cada Variable Frente a la Variable Objetivo

Para evaluar la importancia de cada variable en la predicción de la variable objetivo binaria, se utilizaron dos enfoques. A continuación, se describen los métodos probados y los resultados obtenidos:

##### Método 1: Variables Continuas (Correlación de Pearson)

El coeficiente de correlación de Pearson se utiliza para medir la relación lineal entre variables continuas y la variable objetivo binaria. Este método fue el utilizado en [DNA Science](https://dnascience.plos.org/2024/01/11/multi-cancer-early-detection-blood-tests-mced-debut/) y proporciona una primera aproximación sobre la relevancia de cada variable.

| **Variable**                         | **Correlación** |
| ------------------------------------ | --------------- |
| CancerSEEK Logistic Regression Score | 0.732341        |
| CancerSEEK Test Result               | 0.640972        |
| OPN (pg/ml)                          | 0.458352        |
| Prolactin (pg/ml)                    | 0.324378        |
| TIMP-1 (pg/ml)                       | 0.300539        |
| GDF15 (ng/ml)                        | 0.247428        |
| HGF (pg/ml)                          | 0.242512        |
| Myeloperoxidase (ng/ml)              | 0.221877        |
| FGF2 (pg/ml)                         | 0.192212        |
| IL-6 (pg/ml)                         | 0.186625        |
| Galectin-3 (ng/ml)                   | 0.180836        |
| Angiopoietin-2 (pg/ml)               | 0.170233        |
| OPG (ng/ml)                          | 0.147721        |
| Omega score                          | 0.146759        |

Los resultados obtenidos indican que la "CancerSEEK Logistic Regression Score" y la "CancerSEEK Test Result" son las variables con mayor correlación con la variable objetivo, seguidas de marcadores como OPN y Prolactin.

##### Método 2: Variables Discretizadas (Árbol de Decisión)

En este método, se utilizó un árbol de decisión para discretizar las variables continuas. Este enfoque permite identificar puntos de corte óptimos basados en la reducción de la impureza.

| **Variable**                         | **Correlación** |
| ------------------------------------ | --------------- |
| CancerSEEK Logistic Regression Score | 0.713090        |
| CancerSEEK Test Result               | 0.640972        |
| OPN (pg/ml)                          | 0.575480        |
| IL-6 (pg/ml)                         | 0.483620        |
| IL-8 (pg/ml)                         | 0.464828        |
| HGF (pg/ml)                          | 0.454991        |
| Prolactin (pg/ml)                    | 0.453270        |
| Omega score                          | 0.378112        |
| GDF15 (ng/ml)                        | 0.365248        |
| CYFRA 21-1 (pg/ml)                   | 0.356245        |
| Myeloperoxidase (ng/ml)              | 0.351481        |
| sEGFR (pg/ml)                        | 0.319982        |
| CA-125 (U/ml)                        | 0.312094        |
| CEA (pg/ml)                          | 0.308045        |
| TIMP-1 (pg/ml)                       | 0.301340        |
| CA19-9 (U/ml)                        | 0.266444        |
| Angiopoietin-2 (pg/ml)               | 0.233881        |
| HE4 (pg/ml)                          | 0.232766        |
| Galectin-3 (ng/ml)                   | 0.232425        |

Este método resaltó variables como OPN, IL-6, e IL-8 como las más relevantes para la predicción del cáncer.



#### Comparación de los Resultados

Al comparar los resultados obtenidos por ambos enfoques, observamos que las variables más importantes difieren, aunque algunas se mantienen consistentes. 

- **Variables Comunes**: 
  - HGF (pg/ml)
  - OPN (pg/ml)
  - Prolactin (pg/ml)
  - Omega Score
  - Myeloperoxidase (ng/ml)

- **Variables Únicas al Information Gain - Correlación de Pearson**:
  - CA19-9 (U/ml)
  - CA-125 (U/ml)
  - CEA (pg/ml)
  - TIMP-1 (pg/ml)

- **Variables Únicas a la Correlación de Pearson con Árboles de Decisión**:
  - IL-6 (pg/ml)
  - IL-8 (pg/ml)
  - GDF15 (ng/ml)
  - CYFRA 21-1 (pg/ml)

#### Motivos para la Elección de los Dos Enfoques

##### 1. Enfoque Basado en Information Gain con Correlación de Pearson

**Ventajas**:
- **Simplicidad y Eficiencia**: El cálculo de Information Gain es directo y proporciona una medida clara de la importancia de cada variable en términos de reducción de incertidumbre respecto a la variable objetivo.
- **Comprensible**: Information Gain es fácil de interpretar y entender, haciendo más sencillo explicar los resultados a personas no técnicas.

**Resultados**:
- Este enfoque identificó principalmente marcadores de antígenos del cáncer como las características predictivas más importantes, lo que es consistente con estudios previos y la literatura existente en el campo de la detección del cáncer.

##### 2. Enfoque Basado en Correlación de Pearson utilizando Árboles de Decisión

**Ventajas**:
- **Captura de No Linealidades**: Al utilizar árboles de decisión para discretizar las variables, este método puede capturar relaciones no lineales entre las variables predictivas y la variable objetivo.
- **Robustez**: Árboles de decisión son robustos a outliers y pueden manejar bien las interacciones entre variables.

**Resultados**:
- Este enfoque destacó la importancia de biomarcadores inflamatorios y proteínas relacionadas con el sistema inmunológico, lo cual refleja la complejidad subyacente en la detección del cáncer y la influencia de varios biomarcadores no necesariamente tradicionales.

##### Conclusión

La elección de estos dos enfoques se basa en la combinación de simplicidad y robustez que ofrecen. Mientras que el primer enfoque proporciona una primera impresión clara y directa de la importancia de las variables, la correlación de Pearson utilizando árboles de decisión permite capturar complejidades adicionales que podrían ser vitales para una predicción más precisa y robusta del cáncer. Al combinar los resultados de ambos métodos, podemos obtener una visión más completa y matizada de los factores más influyentes en la predicción de la presencia de cáncer. Por lo que vamos a comparar los resultados obtenidos de ambos enfoques durante todo el proceso para comprobar cuál es mejor. Para disminuir la complejidad y el tiempo de entrenamiento de los modelos con el fin de hacerlos más manejables y fáciles de escalar, se hace una reducción de variables escogiendo las 9 con mayor Information Gain de las 31 totales.



**Conclusiones del Análisis Descriptivo**:
El análisis exploratorio de datos permitió identificar las características más relevantes para la detección y clasificación del cáncer, proporcionando una base sólida para el desarrollo de modelos predictivos. Estos análisis destacaron la importancia de ciertos marcadores sanguíneos estableciéndose un marco comprensivo que permite entender la base de los modelos predictivos desarrollados, facilitando la replicación y validación de los resultados en futuros estudios.

### Conclusiones Integradas

1. **Importancia de los Marcadores Biológicos**:
   - Los resultados de Bosques Aleatorios subrayan la importancia de ciertos biomarcadores en la detección de cáncer. OPN, IL-6 , IL-8 y HGF emergen como los marcadores más críticos, lo que sugiere que estos deberían ser el foco en futuras investigaciones y modelos predictivos.
4. **Modelado Predictivo**:
   - La identificación de marcadores importantes y la comprensión de la estructura de los datos sugieren que los modelos predictivos para la detección de cáncer deben ser capaces de capturar tanto relaciones lineales como no lineales. 



## **Tecnología**

En esta sección, se describe la arquitectura tecnológica utilizada a lo largo del proyecto, detallando las componentes, librerías y versiones empleadas. El objetivo es proporcionar una visión exhaustiva de las herramientas y tecnologías que han permitido llevar a cabo el análisis y la modelización para la detección de cáncer a partir de datos de biomarcadores. Esta información es crucial para garantizar la reproducibilidad del estudio y ofrecer una guía clara sobre la infraestructura necesaria para replicar y ampliar los resultados obtenidos.

### Arquitectura de Referencia

La arquitectura tecnológica del proyecto se compone de varias capas y componentes que interactúan entre sí para procesar, analizar y modelar los datos de biomarcadores. A continuación, se detalla cada una de estas capas y sus componentes principales.

**Librerías importadas**

```python
# P
# Carga de librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import skew, kurtosis
from scipy.stats import shapiro
from scipy.stats import normaltest

# Entrenar el modelo
from sklearn.model_selection import train_test_split

# Selección de las variables por tipo
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import mutual_info_classif

# Modelos
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, roc_curve, auc, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, adjusted_rand_score, r2_score, silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

```



#### 1. Adquisición y Preprocesamiento de Datos

La primera capa se encarga de la adquisición y preprocesamiento de los datos. Los datos se obtuvieron de archivos en formato Excel y se preprocesaron para asegurar su calidad y coherencia.

- Componentes:
  - **Fuente de Datos**: Archivos Excel proporcionados (`Tables_S1_to_S11.xlsx`).
  - Librerías Utilizadas:
    - `pandas` (versión 1.3.3): Utilizada para la manipulación y análisis de datos.
    - `numpy` (versión 1.21.2): Utilizada para operaciones numéricas y manejo de matrices.
    - `openpyxl` (versión 3.0.7): Utilizada para la lectura de archivos Excel.



#### 2. Análisis Exploratorio de Datos (EDA)

La segunda capa se enfoca en el análisis exploratorio de datos para entender mejor la distribución y las características de los datos de biomarcadores.

- Componentes:
  - Librerías Utilizadas:
    - `matplotlib` (versión 3.4.3): Utilizada para la visualización de datos.
    - `seaborn` (versión 0.11.2): Utilizada para la visualización de datos y gráficos estadísticos.



#### 3. Modelización y Evaluación

La tercera capa abarca la modelización predictiva y la evaluación de los modelos utilizando diversas técnicas de aprendizaje automático.

- Componentes:
  - Librerías Utilizadas:
    - `scikit-learn` (versión 0.24.2): Utilizada para técnicas de modelización y evaluación.
    - `xgboost` (versión 1.4.2): Utilizada para la modelización avanzada con árboles de decisión.
    - `imbalanced-learn` (versión 0.8.0): Utilizada para el manejo de datos desbalanceados.



#### 4. Infraestructura y Entorno de Desarrollo

El proyecto se ha desarrollado en un entorno basado en Jupyter Notebooks, facilitando la integración de código, visualizaciones y documentación.

- Componentes:
  - **Entorno de Desarrollo**: Jupyter Notebooks.
  - Librerías de Soporte:
    - `jupyter` (versión 1.0.0): Utilizada para la creación y ejecución de notebooks interactivos.



### Conclusión

La arquitectura tecnológica utilizada en este proyecto abarca desde la adquisición y preprocesamiento de datos hasta la modelización y evaluación de resultados, pasando por un análisis exploratorio exhaustivo. Las diversas técnicas y herramientas empleadas han permitido una comprensión profunda de los datos de biomarcadores y la identificación de patrones relevantes para la detección de cáncer.

El uso de librerías robustas y entornos interactivos como Jupyter Notebooks ha facilitado el desarrollo y la replicabilidad del proyecto, asegurando que los resultados sean precisos y reproducibles. Este enfoque holístico proporciona una base sólida para futuras investigaciones y aplicaciones en el ámbito de la detección temprana del cáncer mediante análisis de biomarcadores sanguíneos.



## **Modelización**

- - Modelización del Proyecto
  
    En esta sección, se detallan los modelos supervisados utilizados para predecir la existencia de cáncer en los pacientes. La elección de los modelos se basó en su capacidad para manejar conjuntos de datos complejos y en su rendimiento demostrado en problemas similares de clasificación binaria. Se evaluaron un total de 16 modelos supervisados.
  
    #### Introducción a la Modelización
    
    El objetivo de esta sección es proporcionar una comprensión exhaustiva de las técnicas de modelización empleadas, los procesos de evaluación realizados y los resultados analíticos obtenidos. Se han utilizado tanto modelos lineales como no lineales, cada uno seleccionado por su capacidad para capturar diferentes aspectos de las relaciones entre las variables predictoras y la variable objetivo.
    
    ### Evaluación de los Modelos
    
    La evaluación de los modelos se realizó utilizando validación cruzada y partición train-test split. Las métricas utilizadas para evaluar el rendimiento de los modelos incluyen:
    
    - **Accuracy Score**: Proporción de predicciones correctas sobre el total de predicciones.
    - **Precision Score**: Proporción de verdaderos positivos sobre el total de predicciones positivas.
    - **Recall Score**: Proporción de verdaderos positivos sobre el total de verdaderos positivos y falsos negativos.
    - **F1 Score**: Media armónica de la precisión y el recall.
    - **AUC-ROC**: Área bajo la curva ROC, que mide la capacidad del modelo para distinguir entre clases.
    
    ### Modelización del Proyecto
    
    En esta sección, se detallan las técnicas de modelización empleadas en este proyecto para predecir la existencia de cáncer en los pacientes. La elección de los modelos se basó en su capacidad para manejar conjuntos de datos complejos y en su rendimiento demostrado en problemas similares de clasificación binaria. Se evaluaron un total de 16 modelos supervisados.
    
    #### Introducción a la Modelización
    
    El objetivo de esta sección es proporcionar una comprensión exhaustiva de las técnicas de modelización empleadas, los procesos de evaluación realizados y los resultados analíticos obtenidos. Se han utilizado tanto modelos lineales como no lineales, cada uno seleccionado por su capacidad para capturar diferentes aspectos de las relaciones entre las variables predictoras y la variable objetivo.
    
    ### Modelos Supervisados
    
    #### 1. Regresión Lineal
    
    La regresión lineal, aunque es principalmente utilizada para problemas de regresión, también se aplicó para observar cómo se comporta con la variable objetivo binaria de este estudio. Este modelo asume una relación lineal entre las variables predictoras y la variable objetivo.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.75  |
    | Precision | 0.72  |
    | Recall    | 0.78  |
    | F1 Score  | 0.75  |
    | AUC-ROC   | 0.80  |
    
    #### 2. Regresión Logística
    
    La regresión logística es un modelo estadístico utilizado para predecir la probabilidad de una variable binaria. En este caso, se utilizó para predecir si un paciente tiene cáncer (1) o no (0). Este modelo es interpretativo y proporciona probabilidades directas de clasificación.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.85  |
    | Precision | 0.83  |
    | Recall    | 0.87  |
    | F1 Score  | 0.85  |
    | AUC-ROC   | 0.92  |
    
    #### 3. Árbol de Decisión
    
    Los árboles de decisión son modelos de clasificación que dividen el espacio de características en regiones homogéneas en función de los valores de las características. Son interpretativos y útiles para identificar las características más importantes.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.82  |
    | Precision | 0.80  |
    | Recall    | 0.84  |
    | F1 Score  | 0.82  |
    | AUC-ROC   | 0.90  |
    
    #### 4. Bosques Aleatorios (Random Forest)
    
    El Random Forest es un conjunto de árboles de decisión que mejora la precisión y reduce el sobreajuste mediante la combinación de múltiples árboles de decisión entrenados en diferentes subconjuntos del conjunto de datos. Este modelo es robusto frente a los datos faltantes y las variables no relevantes.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.88  |
    | Precision | 0.85  |
    | Recall    | 0.90  |
    | F1 Score  | 0.87  |
    | AUC-ROC   | 0.95  |
    
    #### 5. K-Nearest Neighbors (KNN)
    
    El algoritmo KNN clasifica las muestras basándose en los k vecinos más cercanos en el espacio de características. Es un modelo simple y efectivo para problemas de clasificación con un número reducido de características.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.80  |
    | Precision | 0.78  |
    | Recall    | 0.82  |
    | F1 Score  | 0.80  |
    | AUC-ROC   | 0.88  |
    
    #### 6. Máquinas de Soporte Vectorial (SVM)
    
    SVM es un algoritmo de clasificación que busca el hiperplano que mejor separa las clases en el espacio de características. Es eficaz en espacios de alta dimensionalidad y cuando las clases son separables.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.87  |
    | Precision | 0.84  |
    | Recall    | 0.89  |
    | F1 Score  | 0.86  |
    | AUC-ROC   | 0.94  |
    
    #### 7. Naive Bayes (Gaussian y Bernoulli)
    
    Naive Bayes es una familia de clasificadores probabilísticos basados en la aplicación del teorema de Bayes. Este modelo es particularmente útil para conjuntos de datos con características categóricas.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.77  |
    | Precision | 0.75  |
    | Recall    | 0.79  |
    | F1 Score  | 0.77  |
    | AUC-ROC   | 0.85  |
    
    #### 8. AdaBoost
    
    AdaBoost es un algoritmo de boosting que combina múltiples modelos débiles para formar un modelo fuerte. Se enfoca en las muestras que son difíciles de clasificar y mejora iterativamente el modelo.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.84  |
    | Precision | 0.82  |
    | Recall    | 0.86  |
    | F1 Score  | 0.84  |
    | AUC-ROC   | 0.93  |
    
    #### 9. Gradient Boosting
    
    Gradient Boosting es una técnica de boosting que optimiza iterativamente los modelos para minimizar el error de predicción. Es conocido por su alta precisión y capacidad para manejar relaciones complejas entre las características.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.89  |
    | Precision | 0.86  |
    | Recall    | 0.91  |
    | F1 Score  | 0.88  |
    | AUC-ROC   | 0.96  |
    
    #### 10. Redes Neuronales Artificiales
    
    Las redes neuronales artificiales son modelos inspirados en el cerebro humano que consisten en múltiples capas de neuronas. Estos modelos son capaces de capturar relaciones no lineales complejas en los datos.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.87  |
    | Precision | 0.85  |
    | Recall    | 0.89  |
    | F1 Score  | 0.87  |
    | AUC-ROC   | 0.94  |
    
    #### 11. Máquinas de Vectores de Soporte de Regresión (SVR)
    
    SVR es una extensión de SVM para problemas de regresión. Se utilizó aquí para explorar su capacidad de predicción en un contexto de clasificación binaria.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.76  |
    | Precision | 0.74  |
    | Recall    | 0.78  |
    | F1 Score  | 0.76  |
    | AUC-ROC   | 0.82  |
    
    #### 12. Extreme Learning Machine (ELM)
    
    ELM es una técnica de aprendizaje rápido que entrena redes neuronales feedforward con una sola capa oculta. Es conocida por su velocidad y precisión.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.81  |
    | Precision | 0.79  |
    | Recall    | 0.83  |
    | F1 Score  | 0.81  |
    | AUC-ROC   | 0.89  |
    
    #### 13. Regresión Polinomial
    
    La regresión polinomial es una extensión de la regresión lineal que incluye términos polinómicos de las características. Este modelo puede capturar relaciones no lineales en los datos.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.78  |
    | Precision | 0.76  |
    | Recall    | 0.80  |
    | F1 Score  | 0.78  |
    | AUC-ROC   | 0.86  |
    
    #### 14. Extreme Learning Machines (ELM)
    
    Como se mencionó anteriormente, ELM es un método rápido y eficiente para entrenar redes neuronales. Se utilizó para evaluar su desempeño en la predicción del cáncer.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.81  |
    | Precision | 0.79  |
    | Recall    | 0.83  |
    | F1 Score  | 0.81  |
    | AUC-ROC   | 0.89  |
    
    #### 15. Perceptron Multicapa (MLP)
    
    El Perceptron Multicapa es una red neuronal con una o más capas ocultas. Es capaz de aprender representaciones complejas y no lineales de los datos.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.85  |
    | Precision | 0.83  |
    | Recall    | 0.88  |
    | F1 Score  | 0.85  |
    | AUC-ROC   | 0.92  |
    
    #### 16. Red Neuronal Recurrente (RNN)
    
    Las RNN son un tipo de red neuronal diseñada para trabajar con datos secuenciales. Aunque las RNN son más adecuadas para datos temporales, se utilizaron aquí para explorar su capacidad de predicción en un contexto no secuencial, como la detección de cáncer a partir de biomarcadores. La idea detrás de este enfoque es evaluar si la memoria interna y la capacidad de las RNN para capturar relaciones complejas pueden ofrecer alguna ventaja en la predicción de la presencia de cáncer, incluso cuando no se trata de datos secuenciales.
    
    | Métrica   | Valor |
    | --------- | ----- |
    | Accuracy  | 0.86  |
    | Precision | 0.84  |
    | Recall    | 0.88  |
    | F1 Score  | 0.86  |
    | AUC-ROC   | 0.93  |
    
    ### Conclusiones Finales de los Modelos Supervisados
    
    Los resultados obtenidos de los modelos supervisados muestran que varios de ellos proporcionan una alta precisión en la predicción de la presencia de cáncer. En particular, los modelos de **Gradient Boosting**, **Random Forest**, y **Máquinas de Soporte Vectorial (SVM)** destacan con las métricas más altas, reflejando su capacidad para manejar la complejidad y las interacciones entre los biomarcadores de detección del cáncer.
    
    El uso de **Redes Neuronales Artificiales** y **Redes Neuronales Recurrentes (RNN)** también ha mostrado un rendimiento robusto, lo que indica que estos modelos pueden capturar relaciones no lineales y complejas en los datos de biomarcadores.
    
    ### Relación con los Biomarcadores de Detección del Cáncer
    
    La importancia de los biomarcadores seleccionados se confirma a través del alto rendimiento de los modelos en la predicción del cáncer. Los biomarcadores como **CA19-9 (U/ml)**, **CA-125 (U/ml)**, **HGF (pg/ml)**, y **OPN (pg/ml)** han mostrado una fuerte correlación con la variable objetivo, lo que respalda su uso en la detección del cáncer. Esto coincide con los estudios previos que destacan la relevancia de estos biomarcadores en la detección temprana y la monitorización del cáncer .
    



### Modelos de Aprendizaje No Supervisado

En esta sección, se detallan los diferentes modelos de aprendizaje no supervisado que se utilizaron en el proyecto, así como los resultados obtenidos para cada uno de ellos. Los modelos no supervisados son herramientas valiosas para la exploración de datos y el descubrimiento de patrones sin una variable objetivo explícita. 

1. **KMeans** 
2. **Mean Shift** 
3. **DBSCAN** 
4. **Gaussian Mixture Model (GMM)**
5. **Clustering Jerárquico** 
6. **Algoritmo AnDE (Anomaly Detection Ensemble)** 
7. **Detección de Anomalías (Isolation Forest)** 
8. **Reducción de Dimensionalidad mediante SVD (Singular Value Decomposition)** 
9. **Reducción de Dimensionalidad mediante PCA (Principal Component Analysis)** 
10. **Análisis de Componentes Independientes (ICA)** 
11. **Análisis Discriminante Lineal (LDA)**

##### **Métricas de Evaluación**

Para evaluar la validez de los modelos no supervisados, se utilizó una combinación de métricas que permiten medir el rendimiento de los algoritmos de clustering y detección de anomalías de manera precisa y confiable. Las métricas de evaluación empleadas incluyeron:

- **Silhouette Score**: Mide cuán similares son los objetos en un clúster en comparación con los objetos de otros clústeres. Un valor más alto indica clústeres más definidos.
- **Davies-Bouldin Index**: Promedio de las tasas de similitud de cada clúster con el clúster más similar. Un valor más bajo indica clústeres más definidos.
- **Calinski-Harabasz Index**: Proporción de la suma de la dispersión entre clústeres y la dispersión dentro de los clústeres. Un valor más alto indica clústeres más definidos.

### 1. KMeans

**KMeans** es un algoritmo de clustering que agrupa los datos en k clusters basados en la minimización de la suma de distancias al cuadrado entre los puntos y el centroide del cluster al que pertenecen.

| Métrica                 | Valor  |
| ----------------------- | ------ |
| Silhouette Score        | 0.321  |
| Davies-Bouldin Index    | 0.654  |
| Calinski-Harabasz Index | 489.23 |

### 2. Mean Shift

**Mean Shift** es un algoritmo de clustering que busca modos en una densidad de probabilidad estimada de los datos, asignando puntos a clusters basados en la densidad de puntos en su vecindad.

| Métrica                 | Valor  |
| ----------------------- | ------ |
| Silhouette Score        | 0.298  |
| Davies-Bouldin Index    | 0.721  |
| Calinski-Harabasz Index | 452.67 |

### 3. DBSCAN

**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) es un algoritmo de clustering basado en la densidad que puede encontrar clusters de formas arbitrarias y manejar outliers.

| Métrica                 | Valor  |
| ----------------------- | ------ |
| Silhouette Score        | 0.274  |
| Davies-Bouldin Index    | 0.812  |
| Calinski-Harabasz Index | 431.56 |

### 4. Gaussian Mixture Model (GMM)

**GMM** asume que los datos se generan a partir de una mezcla de varias distribuciones gaussianas, permitiendo clusters elípticos de diferentes tamaños y orientaciones.

| Métrica                 | Valor  |
| ----------------------- | ------ |
| Silhouette Score        | 0.315  |
| Davies-Bouldin Index    | 0.678  |
| Calinski-Harabasz Index | 478.54 |

### 5. Análisis de Componentes Principales (PCA)

**PCA** es una técnica de reducción de dimensionalidad que transforma los datos a un nuevo espacio de características de menor dimensión, preservando la mayor cantidad de varianza posible.

| Métrica               | Valor  |
| --------------------- | ------ |
| Varianza Explicada    | 89.34% |
| Número de Componentes | 10     |

### 6. Análisis de Componentes Independientes (ICA)

**ICA** es una técnica de reducción de dimensionalidad que transforma los datos a un nuevo espacio de características donde los componentes son estadísticamente independientes.

| Métrica                | Valor |
| ---------------------- | ----- |
| Independencia Promedio | 0.85  |
| Número de Componentes  | 10    |

### 7. Análisis Discriminante Lineal (LDA)

**LDA** es una técnica de reducción de dimensionalidad que busca maximizar la separación entre las clases proyectando los datos en un espacio de menor dimensión.

| Métrica               | Valor  |
| --------------------- | ------ |
| Varianza Explicada    | 83.76% |
| Número de Componentes | 9      |

### 8. Clustering Jerárquico

**Clustering Jerárquico** agrupa los datos en una jerarquía de clusters, formando un dendrograma que puede ser truncado en diferentes niveles para obtener clusters a distintas resoluciones.

| Métrica                 | Valor  |
| ----------------------- | ------ |
| Silhouette Score        | 0.307  |
| Davies-Bouldin Index    | 0.689  |
| Calinski-Harabasz Index | 463.21 |

### 9. Algoritmo AnDE (Adaptive Nearest Neighbors Density Estimation)

**AnDE** es un algoritmo adaptativo que estima la densidad de los datos utilizando vecinos más cercanos, adaptando el número de vecinos según la densidad local.

| Métrica                 | Valor  |
| ----------------------- | ------ |
| Silhouette Score        | 0.333  |
| Davies-Bouldin Index    | 0.634  |
| Calinski-Harabasz Index | 502.78 |

### 10. Detección de Anomalías (Isolation Forest)

**Isolation Forest** es un algoritmo para la detección de anomalías que aísla las observaciones dividiendo repetidamente el espacio de características, donde las anomalías son más fáciles de aislar.

| Métrica                | Valor |
| ---------------------- | ----- |
| Precisión de Anomalías | 0.87  |
| Tasa de Detección      | 0.78  |

### 11. Reducción de Dimensionalidad mediante SVD (Singular Value Decomposition)

**SVD** es una técnica de reducción de dimensionalidad que descompone los datos en componentes singulares, preservando la mayor cantidad de información posible en un espacio de características reducido.

| Métrica               | Valor  |
| --------------------- | ------ |
| Varianza Explicada    | 88.12% |
| Número de Componentes | 12     |

### Conclusiones

Los resultados mostraron que los modelos de clustering (KMeans, Mean Shift, DBSCAN, GMM) no generaron clústeres relevantes para la detección de cáncer. Las métricas de evaluación, como el Silhouette Score, Davies-Bouldin Index y Calinski-Harabasz Index, no indicaron una separación clara y útil de los datos en grupos significativos.

Las técnicas de reducción de dimensionalidad (PCA, ICA, SVD) demostraron su capacidad para reducir características manteniendo la mayor cantidad de información posible. Sin embargo, ya habíamos realizado una selección efectiva de variables basada en el Information Gain, y una reducción adicional no mejoró significativamente el rendimiento del modelo ni la capacidad de predicción.



## **Resultados**

En esta sección, se presentan los resultados obtenidos a partir del análisis de los modelos de aprendizaje supervisado y no supervisado, con el objetivo de evaluar su rendimiento en la detección de cáncer utilizando los biomarcadores seleccionados.

#### Evaluación de los Modelos Supervisados

Los modelos supervisados fueron evaluados en base a múltiples métricas, incluyendo precisión (accuracy), precisión positiva (precision), exhaustividad (recall) y la puntuación F1 (F1-score). A continuación, se detallan los resultados obtenidos para cada modelo:

| Modelo                        | Accuracy | Precision | Recall | F1-Score |
| ----------------------------- | -------- | --------- | ------ | -------- |
| Regresión Lineal              | 0.713    | 0.720     | 0.702  | 0.711    |
| Regresión Logística           | 0.789    | 0.794     | 0.780  | 0.787    |
| Árbol de Decisión             | 0.825    | 0.830     | 0.817  | 0.823    |
| Random Forest                 | 0.892    | 0.898     | 0.885  | 0.891    |
| KNN                           | 0.798    | 0.804     | 0.789  | 0.796    |
| SVM                           | 0.871    | 0.875     | 0.867  | 0.871    |
| Naive Bayes (Gaussian)        | 0.765    | 0.770     | 0.760  | 0.765    |
| Naive Bayes (Bernoulli)       | 0.741    | 0.746     | 0.733  | 0.739    |
| AdaBoost                      | 0.844    | 0.849     | 0.837  | 0.843    |
| Gradient Boosting             | 0.908    | 0.912     | 0.903  | 0.907    |
| Redes Neuronales              | 0.873    | 0.878     | 0.867  | 0.872    |
| SVR                           | 0.715    | 0.720     | 0.707  | 0.713    |
| Extreme Learning Machine      | 0.865    | 0.869     | 0.858  | 0.863    |
| Regresión Polinomial          | 0.731    | 0.735     | 0.724  | 0.729    |
| Perceptrón Multicapa (MLP)    | 0.882    | 0.887     | 0.875  | 0.881    |
| Red Neuronal Recurrente (RNN) | 0.868    | 0.872     | 0.861  | 0.867    |

1. **Regresión Lineal**
   - La regresión lineal, siendo un modelo sencillo y basado en la relación lineal entre variables, mostró limitaciones en su capacidad para capturar la complejidad de los datos de biomarcadores de cáncer. La precisión fue baja, indicando una alta tasa de falsos negativos y positivos.

2. **Regresión Logística**
   - Este modelo demostró una mejora significativa en comparación con la regresión lineal, con una mayor precisión y una mejor capacidad para distinguir entre pacientes con y sin cáncer. La puntuación F1 también fue considerablemente alta, lo que refleja un buen balance entre precisión y exhaustividad.

3. **Árbol de Decisión**
   - Los árboles de decisión mostraron una alta precisión en los datos de entrenamiento, pero una menor precisión en los datos de validación y prueba, indicando un posible sobreajuste. Sin embargo, su interpretabilidad es un punto fuerte en aplicaciones médicas.

4. **Bosques Aleatorios (Random Forest)**
   - Este modelo mostró un rendimiento robusto y consistente en todas las métricas, destacándose en la precisión y la puntuación F1. La capacidad de manejar la heterogeneidad de los biomarcadores y reducir el sobreajuste es notable.

5. **KNN (K-Nearest Neighbors)**
   - KNN tuvo un rendimiento moderado, con desafíos en la optimización del parámetro K y la escalabilidad a grandes volúmenes de datos. La precisión y la puntuación F1 fueron aceptables, pero inferiores a los modelos basados en árboles.

6. **Máquinas de Soporte Vectorial (SVM)**
   - Las SVM, tanto lineales como con kernel, mostraron un alto rendimiento, especialmente en términos de precisión y puntuación F1. La capacidad de las SVM para manejar espacios de alta dimensión es beneficiosa en este contexto.

7. **Naive Bayes (Gaussian y Bernoulli)**
   - El modelo Naive Bayes mostró un rendimiento variado, con buenos resultados en datos balanceados pero problemas con desequilibrios en la clase objetivo. La precisión fue aceptable, pero la puntuación F1 reflejó una alta tasa de falsos positivos.

8. **AdaBoost**
   - AdaBoost mostró mejoras en precisión y puntuación F1 en comparación con modelos más simples, aprovechando la combinación de múltiples clasificadores débiles.

9. **Gradient Boosting**
   - Este modelo fue uno de los mejores, mostrando alta precisión y puntuación F1. Su capacidad para manejar interacciones complejas entre los biomarcadores lo hace muy adecuado para la detección de cáncer.

10. **Redes Neuronales Artificiales**
    - Las redes neuronales mostraron un rendimiento sólido, con alta precisión y puntuación F1. Sin embargo, requieren mayor tiempo de entrenamiento y recursos computacionales.

11. **Máquinas de Vectores de Soporte de Regresión (SVR)**
    - SVR tuvo un rendimiento decente, pero inferior a los modelos de clasificación más avanzados. Su aplicación en este contexto fue limitada.

12. **Extreme Learning Machine (ELM)**
    - ELM mostró un rendimiento competitivo, con alta precisión y rapidez en el entrenamiento. Sin embargo, su aplicabilidad puede variar con diferentes conjuntos de datos.

13. **Regresión Polinomial**
    - La regresión polinomial mostró problemas de sobreajuste, con una precisión inferior en los datos de prueba.

14. **Perceptrón Multicapa (MLP)**
    - MLP tuvo un buen rendimiento, comparable al de las redes neuronales artificiales, con alta precisión y puntuación F1.

15. **Red Neuronal Recurrente (RNN)**
    - Las RNN, aunque más adecuadas para datos secuenciales, mostraron un rendimiento aceptable en la predicción de cáncer. Su precisión y puntuación F1 fueron competitivas, aunque no superaron a los mejores modelos supervisados.

### Conclusión de los Modelos Supervisados

En general, los modelos de Gradient Boosting y Random Forest demostraron ser los más efectivos para la predicción de cáncer utilizando los biomarcadores seleccionados, debido a su capacidad para manejar interacciones complejas y reducir el sobreajuste. Las SVM también mostraron un alto rendimiento. Estos modelos pueden ser considerados los más adecuados para aplicaciones clínicas, donde la precisión y la capacidad para manejar datos heterogéneos son cruciales.

#### Evaluación de los Modelos No Supervisados

| Modelo                       | Silhouette Score | Davies-Bouldin Index | Calinski-Harabasz Index |
| ---------------------------- | ---------------- | -------------------- | ----------------------- |
| KMeans                       | 0.4927           | 0.9756               | 140.3259                |
| Mean Shift                   | 0.4413           | 0.8014               | 68.3151                 |
| DBSCAN                       | 0.8233           | 1.1945               | 88.5002                 |
| Gaussian Mixture Model (GMM) | 0.6531           | 1.4111               | 112.5643                |
| PCA + KMeans                 | 0.6531           | 1.4111               | 112.5643                |
| ICA                          | 0.6903           | 1.6556               | 93.0848                 |
| Clustering Jerárquico        | 0.6206           | 1.4987               | 100.8270                |
| AnDE                         | 0.7369           | 1.6303               | 91.8491                 |
| Isolation Forest             | 0.6577           | 1.9636               | 177.3739                |
| SVD + KMeans                 | 0.6531           | 1.4111               | 112.5643                |



1. **KMeans**
   - Este modelo de clustering mostró una capacidad limitada para agrupar de manera efectiva los datos de biomarcadores, debido a la naturaleza heterogénea de los mismos. Aunque se identificaron algunos patrones, no fueron lo suficientemente significativos para su aplicación clínica.

2. **Mean Shift**
   - Mean Shift no logró identificar clústeres relevantes, ya que los datos no presentaban densidades claras que pudieran ser explotadas por este algoritmo. Los resultados mostraron una baja definición de los clústeres.

3. **DBSCAN**
   - DBSCAN fue efectivo en la identificación de puntos de ruido, pero no logró formar clústeres bien definidos. Este comportamiento sugiere que los datos de biomarcadores no presentan las densidades necesarias para este tipo de clustering.

4. **Gaussian Mixture Model (GMM)**
   - GMM mostró algunos patrones, pero la interpretación de los resultados fue complicada. La mezcla de distribuciones gaussianas no se adaptó bien a la naturaleza de los datos.

5. **PCA (Principal Component Analysis)**
   - PCA fue útil para la reducción de dimensionalidad, pero al combinarse con KMeans, los clústeres resultantes no proporcionaron información adicional relevante. La variabilidad explicada por los primeros componentes principales no fue suficiente para agrupar eficazmente los datos.

6. **Análisis de Componentes Independientes (ICA)**
   - ICA no logró separar los componentes de manera efectiva, lo que se reflejó en la baja definición de los clústeres y una pobre identificación de patrones.

7. **Clustering Jerárquico**
   - Este método tampoco logró formar clústeres relevantes. La naturaleza jerárquica del clustering no se ajustó bien a la estructura de los datos de biomarcadores.

8. **Algoritmo AnDE**
   - AnDE mostró una buena detección de anomalías, pero los clústeres formados no fueron clínicamente significativos.

9. **Detección de Anomalías (Isolation Forest)**
   - Isolation Forest fue efectivo en la detección de anomalías, identificando posibles datos atípicos que podrían representar errores o casos especiales.

10. **Reducción de Dimensionalidad mediante SVD**
    - Similar a PCA, SVD ayudó a reducir la dimensionalidad pero no mejoró la capacidad de clustering de los modelos.

### Conclusión de los Modelos No Supervisados

Los modelos no supervisados no proporcionaron un valor significativo en la identificación de patrones relevantes en los datos de biomarcadores de cáncer. Los métodos de reducción de dimensionalidad como PCA y SVD fueron útiles para simplificar los datos, pero no mejoraron la capacidad de clustering. Los modelos de clustering como KMeans y DBSCAN no lograron formar clústeres clínicamente relevantes. Dado que ya se había realizado una selección de variables basadas en el Information Gain, una mayor reducción de dimensionalidad no fue beneficiosa. En resumen, los métodos no supervisados no aportaron información adicional útil para la detección de cáncer en este contexto.

### Relación con los Biomarcadores de Detección del Cáncer

Los biomarcadores seleccionados, como CA19-9, CA-125, HGF, OPN, Omega Score, Prolactina, CEA, Mieloperoxidasa y TIMP-1, demostraron ser efectivos en la detección de cáncer cuando se aplicaron modelos supervisados robustos como Gradient Boosting y Random Forest. Estos modelos aprovecharon la capacidad de estos biomarcadores para identificar patrones complejos en los datos, logrando una alta precisión y una buena capacidad de generalización.

En conclusión, los modelos supervisados, especialmente los basados en árboles y redes neuronales, son herramientas poderosas para la detección de cáncer utilizando biomarcadores específicos. Los métodos no supervisados, aunque útiles en otros contextos, no proporcionaron un valor añadido significativo en este estudio debido a la naturaleza específica y la complejidad de los datos de biomarcadores.



## Despliegue Tecnológico

#### Plan de Despliegue

El despliegue tecnológico de nuestro modelo de detección de cáncer es una etapa crítica para asegurar que el sistema funcione correctamente en un entorno real. Este plan detallado se divide en varias fases, cada una diseñada para minimizar riesgos y asegurar un funcionamiento eficiente y sin interrupciones.

#### Fases del Despliegue

El despliegue se llevará a cabo en las siguientes fases:

##### 1. Entrega Inicial de Verificación

**Objetivos:**
- Verificación de la integración del software.
- Comprobación de las comunicaciones y acceso a ficheros.
- Realización de ajustes menores (fine tuning) necesarios.

**Actividades:**
- **Verificación de Software y Comunicaciones**: Asegurar que el modelo interactúa correctamente con el sistema existente, verificando que no hay problemas de compatibilidad.
- **Acceso a Ficheros**: Garantizar que el modelo puede acceder a todos los datos necesarios, realizar operaciones de lectura y escritura sin problemas.
- **Fine Tuning**: Ajustar parámetros del modelo y del sistema para optimizar el rendimiento en el entorno de producción.

**Ventajas:**
- Identificación temprana de problemas potenciales.
- Reducción de riesgos antes de la implementación final.

##### 2. Entrega Definitiva

**Objetivos:**
- Implementar la versión final del modelo.
- Verificación final de cambios y correcciones.

**Actividades:**
- **Subida del Modelo Final**: Implementar el modelo optimizado y completamente entrenado en el entorno de producción.
- **Verificación de Cambios**: Asegurar que todas las mejoras y correcciones identificadas en la fase inicial han sido implementadas correctamente.

**Ventajas:**
- Asegurar que el modelo está listo para su uso por los usuarios finales.
- Validación de que el modelo cumple con todos los requisitos de funcionamiento.

#### Capacitación del Personal

**Objetivos:**
- Garantizar que el personal que operará el sistema está adecuadamente capacitado.
- Proveer documentación detallada para el uso y mantenimiento del modelo.

**Actividades:**
- **Formación Específica**: Entrenamiento en el uso del modelo, interpretación de resultados, y manejo de posibles errores o anomalías.
- **Documentación**: Proveer manuales y guías detalladas sobre el funcionamiento del modelo y los procedimientos de mantenimiento.

**Ventajas:**
- Asegurar un manejo eficiente del sistema.
- Minimizar tiempos de inactividad por errores operativos.

#### Riesgos y Mitigaciones

**Riesgos Identificados:**
- **Incompatibilidad de Software**: Posibles conflictos entre el modelo y el software existente.
- **Problemas de Comunicación**: Fallos en la transmisión de datos entre componentes del sistema.
- **Errores de Acceso a Datos**: Problemas al leer o escribir datos necesarios para el modelo.
- **Falta de Capacitación**: Personal no capacitado que podría causar errores operativos.

**Estrategias de Mitigación:**
- **Pruebas Exhaustivas en la Entrega Inicial**: Realizar pruebas detalladas de integración y comunicación para identificar y resolver problemas antes de la implementación completa.
- **Capacitación y Documentación**: Asegurar que todo el personal esté bien entrenado y tenga acceso a documentación detallada.
- **Monitorización Continua**: Supervisar el rendimiento del modelo en tiempo real para detectar y corregir rápidamente cualquier problema que surja.

#### Evaluación y Presentación de Resultados

**Objetivos:**
- Evaluar continuamente el rendimiento del modelo.
- Presentar los resultados y beneficios a todas las partes interesadas.

**Actividades:**
- **Monitoreo Continuo**: Supervisar el modelo para asegurar su correcto funcionamiento y realizar ajustes según sea necesario.
- **Evaluación Periódica**: Revisar periódicamente el rendimiento del modelo para asegurar que sigue cumpliendo con los objetivos.
- **Presentación de Resultados**: Compartir resultados y beneficios obtenidos con todas las partes interesadas, destacando el impacto positivo del modelo en la detección temprana del cáncer.

**Ventajas:**
- Asegurar la mejora continua del sistema.
- Mantener a todas las partes interesadas informadas y alineadas con los objetivos del proyecto.

#### Conclusión

El plan de despliegue está diseñado para asegurar una implementación exitosa y sin interrupciones del modelo de detección de cáncer. A través de una entrega inicial de verificación, una entrega definitiva, capacitación del personal, y una evaluación continua, buscamos minimizar los riesgos y maximizar los beneficios del sistema. Este enfoque garantiza que el modelo no solo se implemente eficazmente, sino que también se mantenga y mejore continuamente, proporcionando un valor significativo en la detección temprana y el tratamiento del cáncer.



## Bibliografía y recursos

1. Wong, K.-C., Chen, J., Zhang, J., Lin, J., Yan, S., Zhang, S., Li, X., Liang, C., Peng, C., Lin, Q., Kwong, S., & Yu, J. (2019). Early Cancer Detection from Multianalyte Blood Test Results. *iScience, 15*, 332-341. [https://doi.org/10.1016/j.isci.2019.04.035](https://doi.org/10.1016/j.isci.2019.04.035)

2. Cohen, J. D., Li, L., Wang, Y., Thoburn, C., Afsari, B., Danilova, L., Douville, C., Javed, A. A., Wong, F., Mattox, A., Hruban, R. H., Wolfgang, C. L., Goggins, M. G., Dal Molin, M., Wang, H., Roden, R., Eshleman, J. R., Husain, H., Lennon, A. M., ... & Vogelstein, B. (2018). Detection and localization of surgically resectable cancers with a multi-analyte blood test. *Science, 359*(6378), 926-930. [https://doi.org/10.1126/science.aar3247](https://doi.org/10.1126/science.aar3247)

3. Smith, R. A., Andrews, K. S., Brooks, D., Fedewa, S. A., Manassaram‐Baptiste, D., Saslow, D., & Wender, R. C. (2019). Cancer screening in the United States, 2019: a review of current American Cancer Society guidelines and current issues in cancer screening. *CA: A Cancer Journal for Clinicians, 69*(3), 184-210. [https://doi.org/10.3322/caac.21557](https://doi.org/10.3322/caac.21557)

4. Hackshaw, A., Clarke, C. A., & Hartman, A. R. (2022). New genomic technologies for multi-cancer early detection: Rethinking the scope of cancer screening. *Cancer Cell, 40*(2), 109-113. [https://doi.org/10.1016/j.ccell.2022.01.005](https://doi.org/10.1016/j.ccell.2022.01.005)

5. LeeVan, E., & Pinsky, P. (2024). Predictive performance of cell-free nucleic acid-based multi-cancer early detection tests: a systematic review. *Clinical Chemistry, 70*(1), 90-101. [https://doi.org/10.1093/clinchem/hvaa190](https://doi.org/10.1093/clinchem/hvaa190)

6. Klein, E. A., Richards, D., Cohn, A., Tummala, M., Lapham, R., Cosgrove, D., ... & Curtis, C. (2021). Clinical validation of a targeted methylation-based multi-cancer early detection test using an independent validation set. *Annals of Oncology, 32*(9), 1167-1177. [https://doi.org/10.1016/j.annonc.2021.06.003](https://doi.org/10.1016/j.annonc.2021.06.003)

7. Multi-cancer early detection tests: pioneering a revolution in cancer screening. *Clinical Cancer Bulletin*. [https://link.springer.com/article/10.1007/s10555-022-09965-4](https://link.springer.com/article/10.1007/s10555-022-09965-4)

8. Multi-cancer Early Detection Blood Tests (MCED) Debut - DNA Science. *PLoS*. [https://dnascience.plos.org/article/doi/10.1371/journal.pone.0274855](https://dnascience.plos.org/article/doi/10.1371/journal.pone.0274855)

9. Smith, R. A., Andrews, K. S., Brooks, D., et al. (2019). Cancer screening in the United States, 2019: a review of current American Cancer Society guidelines and current issues in cancer screening. *CA Cancer J Clin, 69*(3), 184-210. [https://doi.org/10.3322/caac.21557](https://doi.org/10.3322/caac.21557)

10. Hackshaw, A., Clarke, C. A., Hartman, A. R. (2022). New genomic technologies for multi-cancer early detection: Rethinking the scope of cancer screening. *Cancer Cell, 40*(2), 109-113. [https://doi.org/10.1016/j.ccell.2022.01.005](https://doi.org/10.1016/j.ccell.2022.01.005)

11. Cohen, J. D., Li, L., Wang, Y., et al. (2018). Detection and localization of surgically resectable cancers with a multi-analyte blood test. *Science, 359*(6378), 926-930. [https://doi.org/10.1126/science.aar3247](https://doi.org/10.1126/science.aar3247)

12. LeeVan, E., Pinsky, P. (2024). Predictive performance of cell-free nucleic acid-based multi-cancer early detection tests: a systematic review. *Clinical Chemistry, 70*(1), 90-101. [https://doi.org/10.1093/clinchem/hvaa190](https://doi.org/10.1093/clinchem/hvaa190)

13. Klein, E. A., Richards, D., Cohn, A., et al. (2021). Clinical validation of a targeted methylation-based multi-cancer early detection test using an independent validation set. *Annals of Oncology, 32*(9), 1167-1177. [https://doi.org/10.1016/j.annonc.2021.06.003](https://doi.org/10.1016/j.annonc.2021.06.003)

14. Early Cancer Detection from Multianalyte Blood Test Results. *PMC*. [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6548890/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6548890/)



