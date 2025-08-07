# ♛ Queens Problem — Algoritmo Genético en Python

Este proyecto resuelve el clásico problema de las N reinas utilizando un enfoque evolutivo. El objetivo es ubicar N reinas en un tablero de NxN sin que ninguna se ataque entre sí. 
Se implementa un algoritmo genético que simula la evolución de soluciones mediante selección, cruce y mutación.

## 📘 Descripción general

- Representación de agentes como permutaciones de posiciones de reinas.
- Evaluación de soluciones mediante función de fitness basada en colisiones.
- Cruce entre agentes para generar descendencia.
- Mutación aleatoria para mantener diversidad genética.
- Selección de población basada en rendimiento y aleatoriedad controlada.

## 🧠 Algoritmo genético

- **Inicialización**: se genera una población aleatoria de agentes.
- **Fitness**: se calcula el número de colisiones entre reinas.
- **Cruce**: se combinan pares de agentes para generar nuevos candidatos.
- **Mutación**: se aplican alteraciones aleatorias con cierta probabilidad.
- **Selección**: se eligen los mejores, intermedios, peores y nuevos agentes para la siguiente generación.
- **Iteración**: el proceso se repite hasta encontrar una solución válida (fitness = 0).

## ⚙️ Parámetros configurables

```python
INITIAL_POPULATION = 100     # Tamaño de la población inicial
BOARD_SIZE = 10              # Tamaño del tablero (N reinas)
MUTATION_CHANCE = 0.1        # Probabilidad de mutación
best_pop = 0.5               # Porcentaje de mejor población seleccionada
mid_pop = 0.15               # Porcentaje de población intermedios seleccionada
least_pop = 0.10             # Porcentaje de peor población seleccionada
random_pop = 0.25            # Porcentaje de población nueva aleatorios (inmigración)
```
## ⚠️ Requisitos
Recomendado usar un entorno virtual con Jupyter instalado.

Instala las dependencias necesarias con:
```bash
pip install -r requirements.txt
```
## 📓 Ejecuta el Notebook
Abre el notebook desde Jupyter:
```bash
jupyter notebook queens_genetic_programming.ipynb
```

## 📄 Licencia
Proyecto bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
