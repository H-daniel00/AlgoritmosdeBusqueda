# Proyecto de Inteligencia Artificial: Búsqueda de Matrices por Algoritmo A\*, Breadth-First Search, Depth-First Search

- **Integrantes**:

  - Hector Daniel Serrano Velasco
  - Samuel Cardenas Tellez
  - Saidt Melgarejo Lopez

- **Universidad**: Universidad Privada Domingo Savio
- **Carrera**: Ingeniería de Sistemas

## 📌 Introducción

Este proyecto tiene como finalidad desarrollar un sistema de búsqueda de caminos en una matriz utilizando tres algoritmos diferentes: A\*, Breadth-First Search (BFS) y Depth-First Search (DFS). Estos algoritmos son fundamentales en el campo de la inteligencia artificial y se utilizan para encontrar rutas óptimas en grafos y redes.

## 🎯 Objetivo

Implementar y comparar los algoritmos A\*, BFS y DFS en un entorno visual interactivo, permitiendo visualizar su funcionamiento y eficiencia en la búsqueda de caminos en una matriz.

## 📚 Marco Teórico

Se revisaron conceptos clave como la teoría de grafos, algoritmos de búsqueda y sus aplicaciones en la inteligencia artificial.

### Algoritmo A\*

El algoritmo A\* es un algoritmo de búsqueda de caminos que utiliza una función heurística para guiar su búsqueda. Combina las ventajas de BFS y Dijkstra's Algorithm, asegurando encontrar el camino más corto en el menor tiempo posible.

### Breadth-First Search (BFS)

BFS es un algoritmo de búsqueda que explora todos los nodos a una determinada distancia de la raíz antes de proceder a los nodos a mayores distancias. Es útil para encontrar el camino más corto en grafos no ponderados.

### Depth-First Search (DFS)

DFS es un algoritmo de búsqueda que explora lo más lejos posible a lo largo de cada rama antes de retroceder. Es útil en problemas que requieren recorrer todos los nodos o componentes de un grafo.

## 🛠️ Implementación

### Configuración de la Interfaz Gráfica

Utilizamos Tkinter para desarrollar una interfaz gráfica de usuario que permite al usuario generar una matriz, establecer puntos de inicio y final, y seleccionar muros. También se incluyen botones para ejecutar los algoritmos de búsqueda y visualizar los resultados.

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from queue import PriorityQueue, Queue

# Configurar la ventana de Tkinter
root = tk.Tk()
root.title("Algoritmo de Búsqueda")

# Crear el frame para las secciones de columnas, filas y botón "Generar"
frame_top = ttk.Frame(root)
frame_top.pack(side=tk.TOP, padx=10, pady=10)

# Labels y TextBox para columnas y filas
label_cols = ttk.Label(frame_top, text="Columnas:")
label_cols.grid(row=0, column=0, padx=5, pady=5)
entry_cols = ttk.Entry(frame_top)
entry_cols.grid(row=0, column=1, padx=5, pady=5)
label_rows = ttk.Label(frame_top, text="Filas:")
label_rows.grid(row=0, column=2, padx=5, pady=5)
entry_rows = ttk.Entry(frame_top)
entry_rows.grid(row=0, column=3, padx=5, pady=5)

# ComboBox para la velocidad
label_velocidad = ttk.Label(frame_top, text="Velocidad:")
label_velocidad.grid(row=0, column=4, padx=5, pady=5)
combo_velocidad = ttk.Combobox(frame_top, values=[600, 500, 400, 300, 200, 100, 50])
combo_velocidad.grid(row=0, column=5, padx=5, pady=5)
combo_velocidad.set(200)  # Valor por defecto

# Botón "Generar"
btn_generar = ttk.Button(frame_top, text="Generar")
btn_generar.grid(row=0, column=6, padx=5, pady=5)

# Crear el lienzo
canvas = tk.Canvas(root, width=600, height=600, bg="lightgray")
canvas.pack()

# Frame para los botones de control
frame_buttons = ttk.Frame(root)
frame_buttons.pack(side=tk.TOP, padx=10, pady=10)

# Botones de control
btn_inicio = ttk.Button(frame_buttons, text="Inicio")
btn_inicio.grid(row=0, column=0, padx=5, pady=5)
btn_final = ttk.Button(frame_buttons, text="Final")
btn_final.grid(row=0, column=1, padx=5, pady=5)
btn_muros = ttk.Button(frame_buttons, text="Muros")
btn_muros.grid(row=0, column=2, padx=5, pady=5)
btn_buscar_a_star = ttk.Button(frame_buttons, text="Buscar A*")
btn_buscar_a_star.grid(row=0, column=3, padx=5, pady=5)
btn_buscar_bfs = ttk.Button(frame_buttons, text="Buscar BFS")
btn_buscar_bfs.grid(row=0, column=4, padx=5, pady=5)
btn_buscar_dfs = ttk.Button(frame_buttons, text="Buscar DFS")
btn_buscar_dfs.grid(row=0, column=5, padx=5, pady=5)
btn_reiniciar = ttk.Button(frame_buttons, text="Nuevo")
btn_reiniciar.grid(row=0, column=6, padx=5, pady=5)
btn_desmarcar = ttk.Button(frame_buttons, text="Desmarcar")
btn_desmarcar.grid(row=0, column=7, padx=5, pady=5)
```

Este fragmento de código muestra cómo configurar una interfaz gráfica de usuario con Tkinter. Se crea una ventana principal con entradas para especificar las dimensiones de una matriz y la velocidad de la animación. Incluye botones para generar la matriz y controlar la búsqueda de caminos utilizando algoritmos como A\*, BFS y DFS.

### Desarrollo de la Logica de progracion para las Búsquedas

# Función para ejecutar el algoritmo A\*

```python
    # Función para ejecutar el algoritmo A*
    def buscar_camino():
    global camino_optimo, final
    if inicio is None or final is None:
        messagebox.showwarning("Advertencia", "Debes seleccionar el inicio y el final primero.")
        return
    limpiar_cuadro()
    camino_optimo = []
    fila_inicio, col_inicio = inicio
    fila_final, col_final = final

    # Crear una cola de prioridad
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((0, (fila_inicio, col_inicio)))

    # Inicializar la matriz de costos y la matriz de visitados
    costos = [[float('inf')] * len(matriz[0]) for _ in range(len(matriz))]
    costos[fila_inicio][col_inicio] = 0
    visitados = [[False] * len(matriz[0]) for _ in range(len(matriz))]
    padres = [[None] * len(matriz[0]) for _ in range(len(matriz))]
```

Este fragmento de código implementa el algoritmo A\* para encontrar el camino óptimo en una matriz. Verifica la selección de los puntos de inicio y final, limpia el cuadro de búsqueda, y utiliza una cola de prioridad para gestionar los nodos a explorar. La función evalúa los vecinos del nodo actual y actualiza los costos y padres de cada nodo visitado. Si encuentra un camino, lo reconstruye desde el final hasta el inicio y lo dibuja en el lienzo. En caso de no encontrar un camino, muestra un mensaje de error.

```python
    # Implementación del algoritmo A*
    while not cola_prioridad.empty():
        _, (fila_actual, col_actual) = cola_prioridad.get()
        if visitados[fila_actual][col_actual]:
            continue
        visitados[fila_actual][col_actual] = True

        # Si el nodo actual es el final, detener la búsqueda
        if (fila_actual, col_actual) == final:
            break

        for delta_fila, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nueva_fila = fila_actual + delta_fila
            nueva_col = col_actual + delta_col
            if (0 <= nueva_fila < len(matriz) and 0 <= nueva_col < len(matriz[0]) and (nueva_fila, nueva_col) not in muros):
                nuevo_costo = costos[fila_actual][col_actual] + 1
                if nuevo_costo < costos[nueva_fila][nueva_col]:
                    costos[nueva_fila][nueva_col] = nuevo_costo
                    prioridad = nuevo_costo + distancia_manhattan((nueva_fila, nueva_col), (fila_final, col_final))
                    cola_prioridad.put((prioridad, (nueva_fila, nueva_col)))
                    padres[nueva_fila][nueva_col] = (fila_actual, col_actual)

                    # Dibujar la celda en lila para mostrar el proceso de búsqueda
                    if (nueva_fila, nueva_col) != final:
                        dibujar_cuadrado(nueva_col, nueva_fila, "purple")
                    # Actualizar el lienzo a la velocidad seleccionada
                    root.update()
                    root.after(velocidad)  # Ajustar la velocidad de la animación

    # Verificar si se encontró un camino
    if padres[fila_final][col_final] is None:
        messagebox.showerror("Error", "No se pudo encontrar un camino que llegue al punto final")
        return

    # Reconstruir el camino óptimo
    fila_actual, col_actual = final  # Comenzar desde el nodo final
    while (fila_actual, col_actual) != inicio:  # Mientras no se alcance el nodo de inicio
        camino_optimo.append((fila_actual, col_actual))  # Agregar el nodo actual al camino óptimo
        fila_actual, col_actual = padres[fila_actual][col_actual]  # Moverse al nodo padre
    camino_optimo.reverse()  # Invertir el camino óptimo para que esté en orden desde el inicio hasta el final

    # Trazar el camino más óptimo pintando las cuadrículas de verde
    for row, col in camino_optimo:
        if (row, col) != final:  # Evitar cambiar el color del nodo final
            dibujar_cuadrado(col, row, "green")

    # Asegurarse de que el inicio y el final mantengan sus colores
    if inicio:
        dibujar_cuadrado(inicio[1], inicio[0], "blue")
    if final:
        dibujar_cuadrado(final[1], final[0], "red")

    # Actualizar la variable global final
    final = (fila_final, col_final)
```

Este fragmento de código implementa el algoritmo A\* para encontrar el camino óptimo en una matriz. Verifica la selección de los puntos de inicio y final, limpia el cuadro de búsqueda, y utiliza una cola de prioridad para gestionar los nodos a explorar. La función evalúa los vecinos del nodo actual y actualiza los costos y padres de cada nodo visitado. Si encuentra un camino, lo reconstruye desde el final hasta el inicio y lo dibuja en el lienzo. En caso de no encontrar un camino, muestra un mensaje de error.

```python
    # Función para ejecutar el algoritmo BFS
    def buscar_camino_bfs():
    global camino_optimo, final
    if inicio is None or final is None:
        messagebox.showwarning("Advertencia", "Debes seleccionar el inicio y el final primero.")
        return
    limpiar_cuadro()
    camino_optimo = []
    fila_inicio, col_inicio = inicio
    fila_final, col_final = final

    # Crear una cola de búsqueda
    cola = Queue()
    cola.put((fila_inicio, col_inicio))

    # Inicializar la matriz de costos y la matriz de visitados
    costos = [[float('inf')] * len(matriz[0]) for _ in range(len(matriz))]
    costos[fila_inicio][col_inicio] = 0
    padres = [[None] * len(matriz[0]) for _ in range(len(matriz))]
```

Este fragmento de código implementa la función buscar_camino_bfs(), la cual ejecuta el algoritmo de búsqueda en anchura (BFS). Primero, verifica si los puntos de inicio y final están definidos, y muestra una advertencia si no lo están. Luego, limpia el cuadro de búsqueda y inicializa las estructuras necesarias: una cola para gestionar los nodos a explorar, y matrices para los costos y padres de cada nodo en la matriz. Se prepara para buscar el camino más corto desde el inicio hasta el final dentro de una matriz.

```python
    # Implementación del algoritmo BFS
    while not cola.empty():
        fila_actual, col_actual = cola.get()
        if (fila_actual, col_actual) == final:
            break
        for delta_fila, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nueva_fila = fila_actual + delta_fila
            nueva_col = col_actual + delta_col
            if (0 <= nueva_fila < len(matriz) and 0 <= nueva_col < len(matriz[0]) and (nueva_fila, nueva_col) not in muros):
                nuevo_costo = costos[fila_actual][col_actual] + 1
                if nuevo_costo < costos[nueva_fila][nueva_col]:
                    costos[nueva_fila][nueva_col] = nuevo_costo
                    cola.put((nueva_fila, nueva_col))
                    padres[nueva_fila][nueva_col] = (fila_actual, col_actual)
                    # Dibujar la celda en lila para mostrar el proceso de búsqueda
                    if (nueva_fila, nueva_col) != final:
                        dibujar_cuadrado(nueva_col, nueva_fila, "purple")
                    # Actualizar el lienzo a la velocidad seleccionada
                    root.update()
                    root.after(velocidad)  # Ajustar la velocidad de la animación

    # Verificar si se encontró un camino
    if padres[fila_final][col_final] is None:
        messagebox.showerror("Error", "No se pudo encontrar un camino que llegue al punto final")
        return

    # Reconstruir el camino óptimo
    fila_actual, col_actual = final  # Comenzar desde el nodo final
    while (fila_actual, col_actual) != inicio:  # Mientras no se alcance el nodo de inicio
        camino_optimo.append((fila_actual, col_actual))  # Agregar el nodo actual al camino óptimo
        fila_actual, col_actual = padres[fila_actual][col_actual]  # Moverse al nodo padre
    camino_optimo.reverse()  # Invertir el camino óptimo para que esté en orden desde el inicio hasta el final

    # Trazar el camino más óptimo pintando las cuadrículas de verde
    for row, col in camino_optimo:
        if (row, col) != final:  # Evitar cambiar el color del nodo final
            dibujar_cuadrado(col, row, "green")

    # Asegurarse de que el inicio y el final mantengan sus colores
    if inicio:
        dibujar_cuadrado(inicio[1], inicio[0], "blue")
    if final:
        dibujar_cuadrado(final[1], final[0], "red")

    # Actualizar la variable global final
    final = (fila_final, col_final)
```

Este fragmento de código implementa el núcleo del algoritmo BFS (Breadth-First Search). Dentro de un bucle while, el código procesa nodos desde una cola de búsqueda hasta que esta esté vacía o se alcance el nodo final. Para cada nodo, se exploran sus vecinos válidos (no muros y dentro de los límites de la matriz), actualizando los costos y los padres de los nodos visitados. Además, se visualiza el proceso de búsqueda en un lienzo, dibujando los nodos explorados en color lila y ajustando la velocidad de la animación. Si se encuentra un camino al nodo final, se reconstruye y visualiza el camino óptimo en color verde. Al final, se aseguran de que los nodos de inicio y final mantengan sus colores distintivos.

```python
    # Función para ejecutar el algoritmo DFS
    def buscar_camino_dfs():
    global camino_optimo, final
    if inicio is None or final is None:
        messagebox.showwarning("Advertencia", "Debes seleccionar el inicio y el final primero.")
        return
    limpiar_cuadro()
    camino_optimo = []
    fila_inicio, col_inicio = inicio
    fila_final, col_final = final

    # Crear una pila de búsqueda
    pila = [(fila_inicio, col_inicio)]
```

Este fragmento de código define la función buscar_camino_dfs() que implementa el algoritmo de búsqueda en profundidad (DFS - Depth-First Search). Primero, verifica si los puntos de inicio y final han sido seleccionados, mostrando una advertencia si no es así. Luego, limpia el cuadro de dibujo y establece el camino óptimo como una lista vacía. La búsqueda se inicia desde el nodo inicial, utilizando una pila para mantener los nodos por explorar.

```python
    # Inicializar la matriz de costos y la matriz de visitados
    costos = [[float('inf')] * len(matriz[0]) for _ in range(len(matriz))]
    costos[fila_inicio][col_inicio] = 0
    padres = [[None] * len(matriz[0]) for _ in range(len(matriz))]

    # Implementación del algoritmo DFS
    while pila:
        fila_actual, col_actual = pila.pop()
        if (fila_actual, col_actual) == final:
            break
        for delta_fila, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nueva_fila = fila_actual + delta_fila
            nueva_col = col_actual + delta_col
            if (0 <= nueva_fila < len(matriz) and 0 <= nueva_col < len(matriz[0]) and (nueva_fila, nueva_col) not in muros):
                nuevo_costo = costos[fila_actual][col_actual] + 1
                if nuevo_costo < costos[nueva_fila][nueva_col]:
                    costos[nueva_fila][nueva_col] = nuevo_costo
                    pila.append((nueva_fila, nueva_col))
                    padres[nueva_fila][nueva_col] = (fila_actual, col_actual)
                    # Dibujar la celda en lila para mostrar el proceso de búsqueda
                    if (nueva_fila, nueva_col) != final:
                        dibujar_cuadrado(nueva_col, nueva_fila, "purple")
                    # Actualizar el lienzo a la velocidad seleccionada
                    root.update()
                    root.after(velocidad)  # Ajustar la velocidad de la animación

    # Verificar si se encontró un camino
    if padres[fila_final][col_final] is None:
        messagebox.showerror("Error", "No se pudo encontrar un camino que llegue al punto final")
        return

    # Reconstruir el camino óptimo
    fila_actual, col_actual = final  # Comenzar desde el nodo final
    while (fila_actual, col_actual) != inicio:  # Mientras no se alcance el nodo de inicio
        camino_optimo.append((fila_actual, col_actual))  # Agregar el nodo actual al camino óptimo
        fila_actual, col_actual = padres[fila_actual][col_actual]  # Moverse al nodo padre
    camino_optimo.reverse()  # Invertir el camino óptimo para que esté en orden desde el inicio hasta el final

    # Trazar el camino más óptimo pintando las cuadrículas de verde
    for row, col in camino_optimo:
        if (row, col) != final:  # Evitar cambiar el color del nodo final
            dibujar_cuadrado(col, row, "green")

    # Asegurarse de que el inicio y el final mantengan sus colores
    if inicio:
        dibujar_cuadrado(inicio[1], inicio[0], "blue")
    if final:
        dibujar_cuadrado(final[1], final[0], "red")

    # Actualizar la variable global final
    final = (fila_final, col_final)
```

Este bloque de código inicializa la matriz de costos y la matriz de padres para el algoritmo DFS (Depth-First Search). Luego, implementa el algoritmo DFS para buscar el camino óptimo en el grafo. La búsqueda continúa mientras la pila no esté vacía. En cada iteración, se extrae un nodo de la pila y se exploran sus vecinos. Si se encuentra el nodo final, se detiene la búsqueda. Si se encuentra un camino hacia un nodo no visitado, se actualizan los costos y se agrega el nodo a la pila. Durante la búsqueda, se dibujan las celdas exploradas en color lila para mostrar el proceso de búsqueda. Una vez que se encuentra el camino óptimo, se reconstruye hacia atrás desde el nodo final hasta el nodo inicial, invirtiendo el orden para obtener el camino desde el inicio hasta el final. Finalmente, se traza el camino más óptimo pintando las celdas en verde, y se actualizan los colores de los nodos de inicio y final en el lienzo.

## 📋 Metodología de trabajo utilizando Kanban

- **Recopilación de Datos**: No aplica en este contexto, ya que los algoritmos de búsqueda no requieren datos específicos para su implementación..
- **Preprocesamiento**: Preparación de los datos del problema o del espacio de búsqueda, como la representación de un grafo o la definición de los estados iniciales y finales.
- **Modelado**: Implementación de los algoritmos de búsqueda, como A\*, BFS y DFS, utilizando las estructuras de datos adecuadas y optimizando los parámetros según sea necesario.
- **Evaluación**: Evaluación del rendimiento de los algoritmos mediante métricas como la eficiencia en términos de tiempo y espacio, así como la calidad de las soluciones encontradas en diferentes escenarios de prueba.

## 🖥️ Modelado o Sistematización

La implementación de los algoritmos de búsqueda se realizó después de un exhaustivo análisis de las características del problema y las posibles soluciones. Se ajustaron los parámetros relevantes y se seleccionaron las estructuras de datos más adecuadas para representar el espacio de búsqueda. Además, se llevó a cabo una optimización continua para mejorar la eficiencia y la efectividad de los algoritmos en la resolución de problemas específicos.

## 📊 Conclusiones

Los algoritmos implementados demostraron una efectividad destacada en la resolución de problemas de búsqueda en diferentes tipos de espacios de búsqueda. A través de la evaluación de métricas como el tiempo de ejecución, la complejidad espacial y la calidad de la solución encontrada, se pudo observar el potencial de estos algoritmos para abordar una amplia gama de desafíos en el ámbito de la inteligencia artificial y la optimización. Además, se identificaron áreas de mejora y posibles extensiones para futuros trabajos en la investigación y aplicación de estos algoritmos.

## 📚 Bibliografía

- Bird, S., Klein, E., & Loper, E. (2009). _Natural Language Processing with Python_. O'Reilly Media.
- Chollet, F. (2017). _Deep Learning with Python_. Manning Publications.

## 📁 Anexos

- Código Fuente: [GitHub](https://github.com/H-daniel00/AlgoritmosdeBusqueda.git)
