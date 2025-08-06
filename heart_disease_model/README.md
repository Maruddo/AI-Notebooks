# 🫀 Modelo de Predicción de Enfermedad Cardíaca (PyTorch)

Desarrollado como parte de trabajo académico y exploración personal en Machine Learning.

Este proyecto implementa una red neuronal para predecir la presencia de enfermedad cardíaca a partir de datos clínicos estructurados. 
Está desarrollado íntegramente en un único script con PyTorch, e incluye funcionalidades para entrenamiento interactivo, evaluación, y predicciones personales desde la terminal.

## 📌 Características principales

- Preprocesamiento automático: codificación one-hot de sexo y rangos de edad.
- Normalización de datos clínicos para facilitar el aprendizaje.
- División del dataset en entrenamiento y prueba (80/20).
- Carga automática de los mejores pesos obtenidos en pruebas previas.
- Interfaz interactiva que solicita datos personales para realizar predicciones.

## 🧠 Arquitectura del modelo

La red neuronal consta de tres capas densas con activaciones ReLU. El diseño busca equilibrio entre simplicidad y capacidad de generalización:

- Entrada: 17 variables (datos clínicos + codificaciones)
- Capas ocultas: 100 y 35 neuronas
- Salida: 2 clases (presencia o ausencia de enfermedad)

## ⚙️ Requisitos
Recomendado usar un entorno virtual con Jupyter instalado.

Instala las dependencias necesarias ejecutando:
```bash
pip install -r requirements.txt
```
## 📓 Ejecuta el Notebook
Abre el notebook desde Jupyter:
```bash
jupyter notebook heart_disease.ipynb
```
Puedes elegir entre entrenar el modelo o introducir tus datos personales para obtener una predicción. Si entrenas, podrás ajustar el learning rate y el número de épocas en cada ciclo.
Además puedes elegir guardar los mejores pesos.

## 📄 Licencia
Proyecto bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
