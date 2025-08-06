# ☝🏻 Skin Cancer Classification with PyTorch

Este ejercicio implementa una `red neuronal convolucional (CNN)` para clasificar imágenes de lesiones cutáneas en dos categorías: benignas y malignas.
Utiliza `PyTorch` como framework principal y está diseñado para entrenar, evaluar y guardar el modelo de forma interactiva.

## 🗂️ Dataset
Puedes descargar el Dataset aquí: https://www.kaggle.com/datasets/fanconic/skin-cancer-malignant-vs-benign

El dataset contiene 3 carpetas, train, test y data. 
Data contiene las carpetas train y test repetidas así que eliminé las otras carpetas y usé Data.

Dentro de train y test se encuentran las imagenes clasificadas en carpetas benign y malignant.

## 🧠 Arquitectura del modelo
La red neuronal consta de:

2 capas convolucionales con `MaxPooling`

Varias capas densas con activación `LeakyReLU`

Salida con 2 neuronas (clasificación binaria)

Conv2d → MaxPool → Conv2d → MaxPool → Flatten → Linear → LeakyReLU → ... → Linear(2)

## ⚙️ Requisitos
Recomendado usar un entorno virtual con Jupyter instalado.

Instala las dependencias necesarias con:
```bash
pip install -r requirements.txt
```
## 📓 Ejecuta el Notebook
Abre el notebook desde Jupyter:
```bash
jupyter notebook sc_model.ipynb
```
Puedes elegir entre entrenar el modelo o solo hacer test. Si entrenas, podrás ajustar el learning rate y el número de épocas en cada ciclo.
Además puedes elegir guardar los mejores pesos.

## ⬆️ Posibles mejoras
Normalización y data augmentation

Transfer learning con modelos preentrenados

Métricas clínicas (precision, recall, F1-score)

Visualización de errores y matriz de confusión

## 📄 Licencia
Proyecto bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
