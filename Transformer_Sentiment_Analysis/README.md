# 🎬 Clasificación de Sentimientos en Reseñas de Películas (PyTorch + Transformers)

Desarrollado como parte de una exploración personal en NLP y Deep Learning.

Este proyecto implementa una red neuronal basada en `TransformerEncoder` para predecir el sentimiento (positivo o negativo) de reseñas de películas. 
Está desarrollado en un único script con PyTorch, e incluye funcionalidades para entrenamiento interactivo, evaluación, y visualización de resultados.

## 📌 Características principales

- Tokenización automática con BERT (`bert-base-uncased`)
- Preprocesamiento de texto y codificación binaria de sentimientos
- División del dataset en entrenamiento y prueba (70/30)
- Carga automática de los mejores pesos obtenidos en pruebas previas
- Interfaz interactiva para ajustar hiperparámetros y guardar el modelo

## 🗂️ Dataset

Se utiliza el dataset de reseñas de películas IMDB, disponible en:
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

Debe contener dos columnas:
- `review`: texto de la reseña
- `sentiment`: etiqueta (`positive` o `negative`)

## 🧠 Arquitectura del modelo

La red neuronal consta de:

- Capa de embeddings
- 2 capas `TransformerEncoder` con atención multi-cabeza
- Capa final `Linear` para clasificación binaria

El diseño busca capturar relaciones contextuales profundas entre palabras sin usar modelos preentrenados completos.

## ⚙️ Requisitos

Recomendado usar un entorno virtual. 

Si quieres usar CUDA, usa la versión 12.8 o cambia el archivo requirements para tu versión: torch==2.8.0+cu128 → torch==2.8.0+cu{tuVersión}

Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```
## 📓 Ejecuta el Notebook
Abre el notebook desde Jupyter:
```bash
jupyter notebook Transformer_Sentiment_Analysis.ipynb
```
Puedes elegir entre entrenar el modelo o usar datos de test para obtener una predicción. Si entrenas, podrás ajustar el learning rate y el número de épocas en cada ciclo. Además puedes elegir guardar los mejores pesos.

## 📄 Licencia
Proyecto bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
