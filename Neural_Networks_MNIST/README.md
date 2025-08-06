# 🧠 Redes Neuronales para MNIST

Uno de los primeros proyectos de redes neuronales, perfecto para empezar a entenderlas.

Este proyecto implementa una red neuronal desde cero para clasificar dígitos escritos a mano del dataset MNIST. 
Está desarrollado en un notebook de Jupyter utilizando **NumPy**, lo que lo convierte en una excelente herramienta didáctica para entender los fundamentos del aprendizaje profundo.

## 📘 Descripción general

- Implementación manual de capas: `Linear`, `ReLU`, `Flatten`, `Input`.
- Propagación hacia adelante (`forward`) y hacia atrás (`backward`) sin frameworks externos.
- Entrenamiento con codificación one-hot y función de activación `softmax`.
- Evaluación con precisión y matriz de confusión.
- Visualización con `matplotlib` y `seaborn`.

## 🗂️ Dataset

Este es el dataset de MNIST usado con este Notebook: https://www.kaggle.com/datasets/hojjatk/mnist-dataset
Tener en cuenta que por defecto en el Notebook este dataset está dentro de una carpeta llamada ``dataset``

## 🧠 Arquitectura del modelo

- Entrada: 784 neuronas (28×28 píxeles)
- Capa oculta: 100 neuronas con activación ``ReLU``
- Salida: 10 neuronas (una por dígito)
- Activación final: ``softmax``

## 📈 Entrenamiento

-Función de pérdida: MSE 
-Optimización manual con gradiente descendente
-Coste por época impreso en consola

## ⚙️ Requisitos

Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## 📓 Ejecuta el Notebook
Abre el notebook desde Jupyter:
```bash
jupyter notebook Transformer_Sentiment_Analysis.ipynb
```

## ⬆️ Posibles Mejoras
Implementar ``cross-entropy`` como función de pérdida

Añadir más capas ocultas o regularización

Visualizar ejemplos mal clasificados

Guardar pesos del modelo y reutilizarlos

## 📄 Licencia

Proyecto bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
