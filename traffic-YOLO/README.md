# 🚦 Traffic Video Analytics with YOLO

Este proyecto utiliza el modelo YOLO para realizar análisis de tráfico en vídeo, incluyendo detección de vehículos, seguimiento, trazado de trayectorias y activación de zonas personalizadas. 
Se aprovecha la biblioteca `supervision` para anotaciones avanzadas.

## 🎥 Vídeo analizado
He editado un video para este ejercicio, puedes descargarlo desde aquí: https://drive.google.com/file/d/128eyOBpUADYPJEbv5SQq6oS0F9lXyDoc/view?usp=drive_link

Vídeo original: https://www.youtube.com/watch?v=KnPiP9PkLAs

Recuerda cambiar la ruta del vídeo en el Notebook para que coincida con la tuya

## 📘 Descripción general

- Detección de objetos en vídeo con YOLO.
- Seguimiento de vehículos con `ByteTrack`.
- Análisis de zonas: líneas de entrada/salida y polígonos personalizados.
- Anotación visual de cajas, etiquetas, trazas y zonas.
- Captura de fotogramas y visualización en tiempo real.

## 🧠 Funcionalidades clave
setup_zones(): define un polígono de interés y tres líneas de análisis.

initialize_tools(): carga el modelo YOLO, el tracker, el suavizador y los anotadores.

process_frame(): procesa cada fotograma, aplica detección, seguimiento y anotación.

process_video(): recorre el vídeo, muestra los resultados en tiempo real y permite guardar un fotograma.

## ⚙️ Requisitos
Recomendado usar un entorno virtual con Jupyter instalado. 

Si quieres usar CUDA, usa la versión 12.8 o cambia el archivo requirements para tu versión: torch==2.8.0+cu128 → torch==2.8.0+cu{tuVersión}

Instala las dependencias necesarias con:
```bash
pip install -r requirements.txt
```
## 📓 Ejecuta el Notebook
Abre el notebook desde Jupyter:
```bash
jupyter notebook traffic-yolo.ipynb
```

## ⬆️ Posibles mejoras
Soporte para múltiples vídeos en lote.

Exportar estadísticas de tráfico por zona.

## 📄 Licencia
Proyecto bajo la licencia MIT. Ver el archivo LICENSE para más detalles.





