# 🧭 A* maze solver with Pyamaze | Resolver laberintos de Pyamaze con A*
This project demonstrates the A* (A-star) pathfinding algorithm implemented in Python using the ``pyamaze`` library. It generates a maze with ``pyamaze`` and finds the shortest path from the bottom-right corner to the top-left using Manhattan distance as the heuristic.

Este proyecto demuestra el algoritmo A* implementado en Python usando la librería ``pyamaze``. Genera un laberinto con ``pyamaze`` y encuentra el camino más corto desde la esquina de abajo a la derecha hasta la de arriba a la derecha usando la distancia Manhattan como heurística.

## 📘 Not a Notebook
This section does not use Jupyter Notebooks.

Esta sección no usa Notebooks de Jupyter.

## 🚀 Features | Características
- Maze generation using ``pyamaze``  
  Generación de laberintos con ``pyamaze``

- A* algorithm with Manhattan heuristic  
  Algoritmo A* con heurística Manhattan

- Visual path tracing with an agent  
  Visualización del camino con un agente

- Execution time measurement  
  Medición del tiempo de ejecución

## ⚙️ Requirements | Requisitos
To run the code you only need ``pyamaze`` | Para ejecutar el código solo necesitas ``pyamaze``

Install requirements | Instalar requisitos:
```
bash
pip install -r requirements.txt
```
## 🧠 How It Works | Cómo Funciona
- Heuristic: Manhattan distance (``abs(x1 - x2) + abs(y1 - y2)``)  
  Heurística: distancia Manhattan (``abs(x1 - x2) + abs(y1 - y2)``)

- Cost calculation: g_score (cost from start cell to current cell) and f_score (``g_score + heuristic``)  
  Cálculo de coste: g_score (coste de la celda inicial a la actual) y f_score (``g_score + heuristic``)
  
- Priority Queue: Used to select the next cell with the lowest estimated cost (f_score)  
  Cola de prioridad: selecciona la siguiente celda con el menor coste estimado (f_score)
  
- Path Reconstruction: Backtracks from the goal to the start using a dictionary  
  Reconstrucción del camino: retrocede desde el objetivo hasta el inicio usando un diccionario

🖼️ Visualization | Visualización
An agent traces the optimal path found by A* in the maze. Footprints are enabled for clarity.  
Un agente recorre el camino óptimo encontrado por A* en el laberinto. Las huellas están activadas para mayor claridad.

📄 License | Licencia
Distributed under the MIT License. See the LICENSE file for more details.  
Distribuido bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
