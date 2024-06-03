import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from queue import PriorityQueue
from collections import deque
import time
import itertools

# Configurar la ventana de Tkinter
root = tk.Tk()
root.title("Algoritmo A*")

# Crear el frame izquierdo para los controles
frame_izquierdo = ttk.Frame(root)
frame_izquierdo.pack(side=tk.LEFT, padx=10, pady=10)

# Crear un GroupBox para los controles
groupbox_controles = ttk.LabelFrame(frame_izquierdo, text="Controles")
groupbox_controles.pack(fill=tk.BOTH, expand=True)

# Labels y TextBox para columnas y filas
label_cols = ttk.Label(groupbox_controles, text="Columnas:")
label_cols.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_cols = ttk.Entry(groupbox_controles)
entry_cols.grid(row=0, column=1, padx=5, pady=5)

label_rows = ttk.Label(groupbox_controles, text="Filas:")
label_rows.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_rows = ttk.Entry(groupbox_controles)
entry_rows.grid(row=1, column=1, padx=5, pady=5)

# Botón "Generar"
btn_generar = ttk.Button(groupbox_controles, text="Generar")
btn_generar.grid(row=2, column=1,  padx=5, pady=5)

# Botón "Información"
btn_informacion = ttk.Button(groupbox_controles, text="Información")
btn_informacion.grid(row=3, column=1,padx=5, pady=5)

# ComboBox para la velocidad
label_velocidad = ttk.Label(groupbox_controles, text="Velocidad:")
label_velocidad.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
combo_velocidad = ttk.Combobox(groupbox_controles, values=[600, 500, 400, 300, 200, 100, 50, 10])
combo_velocidad.grid(row=4, column=1, padx=5, pady=5)
combo_velocidad.set(200)  # Valor por defecto

# ComboBox para el algoritmo
label_algoritmo = ttk.Label(groupbox_controles, text="Algoritmo:")
label_algoritmo.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
combo_algoritmo = ttk.Combobox(groupbox_controles, values=["Algoritmo A*", "DFS", "BFS", "Dijkstra"], width=13)
combo_algoritmo.grid(row=5, column=1, padx=5, pady=5)


# Botones de control
btn_inicio = ttk.Button(groupbox_controles, text="Inicio")
btn_inicio.grid(row=6, column=1, padx=5, pady=5)
btn_final = ttk.Button(groupbox_controles, text="Final")
btn_final.grid(row=7, column=1, padx=5, pady=5)

btn_muros = ttk.Button(groupbox_controles, text="Muros")
btn_muros.grid(row=8, column=1, padx=5, pady=5)

# Botones de control
btn_buscar = ttk.Button(groupbox_controles, text="Buscar")
btn_buscar.grid(row=10, column=1, padx=5, pady=5)

btn_reiniciar = ttk.Button(groupbox_controles, text="Reiniciar")
btn_reiniciar.grid(row=11, column=1, padx=5, pady=5)

btn_desmarcar = ttk.Button(groupbox_controles, text="Desmarcar")
btn_desmarcar.grid(row=12, column=1, padx=5, pady=5)

# Crear el lienzo
canvas = tk.Canvas(root, width=400, height=400, bg="lightgray")
canvas.pack(side=tk.LEFT, padx=10, pady=10)

# Crear el frame derecho
frame_derecho = ttk.Frame(root)
frame_derecho.pack(side=tk.LEFT, padx=10, pady=10)

# Crear un GroupBox para los cálculos
groupbox_calculos = ttk.LabelFrame(frame_izquierdo, text="Cálculos")
groupbox_calculos.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Labels para los valores h, g, n, f, p
label_fm = ttk.Label(groupbox_calculos, text="Proceso:")
label_fm.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
label_h = ttk.Label(groupbox_calculos, text="h:")
label_h.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
label_g = ttk.Label(groupbox_calculos, text="g:")
label_g.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
label_n = ttk.Label(groupbox_calculos, text="n:")
label_n.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
label_f = ttk.Label(groupbox_calculos, text="f:")
label_f.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
label_p = ttk.Label(groupbox_calculos, text="p:")
label_p.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
label_tiempo_a_estrella = ttk.Label(groupbox_calculos, text="Tiempo A*:")
label_tiempo_a_estrella.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
label_tiempo_dfs = ttk.Label(groupbox_calculos, text="Tiempo DFS:")
label_tiempo_dfs.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
label_tiempo_bfs = ttk.Label(groupbox_calculos, text="Tiempo BFS:")
label_tiempo_bfs.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
label_tiempo_dijkstra = ttk.Label(groupbox_calculos, text="Tiempo Dijkstra:")
label_tiempo_dijkstra.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)
label_fm = ttk.Label(groupbox_calculos, text="Formula:")
label_fm.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
label_gh = ttk.Label(groupbox_calculos, text="F = g + h")
label_gh.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
label_ff = ttk.Label(groupbox_calculos, text="F = f")
label_ff.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

# Variables globales
matriz = []
inicio = None
final = None
muros = []
celda_size = 20
modo = None
velocidad = 200  # Velocidad por defecto
informacion = []
g_score = {}

# Función para generar la matriz
def generar_matriz():
    global matriz, celda_size, generador_letras
    global matriz, celda_size, generador_letras,inicio, final, muros
    canvas.delete("all")  # Limpiar todo el lienzo
    cols = int(entry_cols.get())
    rows = int(entry_rows.get())
    matriz = [[0 for _ in range(cols)] for _ in range(rows)]

    # Ajustar tamaño de celda en función de las dimensiones de la matriz
    celda_size = min(400 // cols, 400 // rows)

    # Redimensionar canvas
    canvas.config(width=cols * celda_size, height=rows * celda_size)

    # Reiniciar generador de letras
    generador_letras = generar_letras()

    # Reiniciar inicio, final y muros
    inicio = None
    final = None
    muros = []

    # Reiniciar las etiquetas p, h, n, g, f
    label_p.config(text="p:")
    label_h.config(text="h:")
    label_n.config(text="n:")
    label_g.config(text="g:")
    label_f.config(text="f:")
    label_gh.config(text="F = g + h")
    label_ff.config(text="F = f")

     # Reiniciar los valores de tiempo
    label_tiempo_a_estrella.config(text="Tiempo A*: ")
    label_tiempo_dfs.config(text="Tiempo DFS: ")
    label_tiempo_bfs.config(text="Tiempo BFS: ")
    label_tiempo_dijkstra.config(text="Tiempo Dijkstra: ")

    dibujar_matriz(cols, rows)

# Función para generar letras del abecedario
# def generar_letras():
#     letras = [chr(i) for i in range(ord('a'), ord('z')+1)]
#     for a in letras:
#         yield a
#     for a in letras:
#         for b in letras:
#             yield a + b

def generar_letras():
    letras = [chr(i) for i in range(97, 123) if i != 241]  # Excluyendo la letra "ñ"
    for n in itertools.count(1):
        for combo in itertools.product(letras, repeat=n):
            yield ''.join(combo)

# Probando la función
secuencia = generar_letras()
for _ in range(10):  # Generar las primeras 10 letras de la secuencia
    print(next(secuencia))

# Crear generador de letras del abecedario
generador_letras = generar_letras()

# Función para dibujar la matriz
def dibujar_matriz(cols, rows):
    canvas.delete("all")
    for i in range(rows):
        for j in range(cols):
            x1 = j * celda_size
            y1 = i * celda_size
            x2 = x1 + celda_size
            y2 = y1 + celda_size
            fill_color = "white"
            if (i, j) == inicio:
                fill_color = "blue"
            elif (i, j) == final:
                fill_color = "red"
            elif (i, j) in muros:
                fill_color = "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="gray")
            # Obtener la letra correspondiente del generador de letras del abecedario y colocarla en el centro del cuadro
            letra = next(generador_letras)
            letra_x = (x1 + x2) // 2
            letra_y = (y1 + y2) // 2
            canvas.create_text(letra_x, letra_y, text=letra)

# Función para seleccionar el inicio
def seleccionar_inicio(event):
    global inicio, letra_inicio
    if inicio:
        return  # No permitir colocar un segundo inicio
    col = event.x // celda_size
    row = event.y // celda_size
    if 0 <= col < len(matriz[0]) and 0 <= row < len(matriz):
        if (row, col) != final:
            dibujar_cuadrado(col, row, "blue")
            inicio = (row, col)
            letra_inicio = obtener_letra(row, col)  # Obtener la letra correspondiente al inicio seleccionado
            label_p.config(text=f"p: {letra_inicio}")  # Actualizar la etiqueta "p" con la letra del inicio

# Función para obtener la letra de una celda específica
def obtener_letra(row, col):
    generador_letras_temp = generar_letras()
    for r in range(len(matriz)):
        for c in range(len(matriz[0])):
            letra = next(generador_letras_temp)
            if (r, c) == (row, col):
                return letra

# Función para seleccionar el final
def seleccionar_final(event):
    global final, nuevo_final
    col = event.x // celda_size
    row = event.y // celda_size
    if 0 <= col < len(matriz[0]) and 0 <= row < len(matriz):
        if (row, col) != inicio:
            nuevo_final = (row, col)
            if final:
                dibujar_cuadrado(final[1], final[0], "white")
            dibujar_cuadrado(col, row, "red")
            final = (row, col)

# Función para seleccionar los muros
def seleccionar_muros(event):
    col = event.x // celda_size
    row = event.y // celda_size
    if 0 <= col < len(matriz[0]) and 0 <= row < len(matriz):
        if (row, col) != inicio and (row, col) != final:
            dibujar_cuadrado(col, row, "gray")
            if (row, col) not in muros:
                muros.append((row, col))

# Función para seleccionar o desmarcar muros con arrastre
def arrastrar_muros(event):
    col = event.x // celda_size
    row = event.y // celda_size
    if 0 <= col < len(matriz[0]) and 0 <= row < len(matriz):
        if (row, col) != inicio and (row, col) != final:
            if (row, col) not in muros:
                dibujar_cuadrado(col, row, "gray")
                muros.append((row, col))

# Función para desmarcar una casilla
def desmarcar(event):
    global inicio, final
    col = event.x // celda_size
    row = event.y // celda_size
    if 0 <= col < len(matriz[0]) and 0 <= row < len(matriz):
        dibujar_cuadrado(col, row, "white")
        if (row, col) == inicio:
            inicio = None
        elif (row, col) == final:
            # Eliminar rastro del final desmarcado
            dibujar_cuadrado(col, row, "white")
            final = None
        if (row, col) in muros:
            muros.remove((row, col))

        # Actualizar inicio y final si se desmarcan
        if inicio is None or final is None:
            return
        if modo == "inicio":
            inicio = (row, col)
        elif modo == "final":
            final = (row, col)

# Función para mostrar la información
def mostrar_informacion(event):
    global modo, g_score
    if modo == "informacion":
        col = event.x // celda_size
        row = event.y // celda_size
        if 0 <= col < len(matriz[0]) and 0 <= row < len(matriz):
            h_val = heuristica((row, col), final)
            g_val = g_score.get((row, col), 0)  # Si no se ha visitado la celda, el valor de g será 0
            f_val = g_val + h_val
            n_val = obtener_letra(row, col)
            label_p.config(text=f"p: {letra_inicio}")
            label_h.config(text=f"h: {h_val}")
            label_g.config(text=f"g: {g_val}")
            label_n.config(text=f"n: {n_val}")
            label_f.config(text=f"f: {f_val}")
            label_gh.config(text=f"F = {g_val} + {h_val}")
            label_ff.config(text=f"F = {f_val}")
    else:
        messagebox.showinfo("Información", "Primero debes seleccionar el modo 'Información'.")

# Función para limpiar los cuadros antes de buscar
def limpiar_cuadro():
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i, j) != inicio and (i, j) != final and (i, j) not in muros:
                dibujar_cuadrado(j, i, "white")

# Función para dibujar un cuadrado en la matriz
def dibujar_cuadrado(col, row, color):
    x1 = col * celda_size
    y1 = row * celda_size
    x2 = x1 + celda_size
    y2 = y1 + celda_size
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
    letra = obtener_letra(row, col)
    letra_x = (x1 + x2) // 2
    letra_y = (y1 + y2) // 2
    canvas.create_text(letra_x, letra_y, text=letra)

# Función para calcular la distancia manhattan
def distancia_manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Función para limpiar los cuadros antes de buscar
def limpiar_cuadro():
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i, j) != inicio and (i, j) != final and (i, j) not in muros:
                dibujar_cuadrado(j, i, "white")

# Función para calcular el camino
def buscar_camino():
    global final, g_score, temporizador
    if not inicio:
        messagebox.showerror("Error", "Debe seleccionar el inicio")
        return
    limpiar_cuadro()
    start_time = time.time()
    while True:
        if not final:
            messagebox.showerror("Error", "Debe seleccionar el final")
            return
        open_set = PriorityQueue()
        open_set.put((0, inicio))
        came_from = {}
        g_score = {inicio: 0}
        f_score = {inicio: heuristica(inicio, final)}

        while not open_set.empty():
            current = open_set.get()[1]

            if current == final:
                reconstruir_camino(came_from, current)
                return

            for vecino in obtener_vecinos(current):
                temp_g_score = g_score[current] + costo_movimiento(current, vecino)
                if vecino not in g_score or temp_g_score < g_score[vecino]:
                    came_from[vecino] = current
                    g_score[vecino] = temp_g_score
                    f_score[vecino] = temp_g_score + heuristica(vecino, final)
                    open_set.put((f_score[vecino], vecino))

                    # Actualizar etiquetas h, g, n, f
                    h_val = heuristica(vecino, final)
                    g_val = temp_g_score
                    f_val = g_val + h_val
                    n_val = obtener_letra(*vecino)

                    label_h.config(text=f"h: {h_val}")
                    label_g.config(text=f"g: {g_val}")
                    label_n.config(text=f"n: {n_val}")
                    label_f.config(text=f"f: {f_val}")
                    label_gh.config(text=f"F = {g_val} + {h_val}")
                    label_ff.config(text=f"F = {f_val}")
                    if vecino != final:
                        dibujar_cuadrado(vecino[1], vecino[0], "yellow")
                    root.update()
                    root.after(velocidad)

            # Verificar si el destino ha cambiado durante la búsqueda
            if final != nuevo_final:
                final = nuevo_final
            end_time = time.time()
            elapsed_time = end_time - start_time
            segundos_totales = elapsed_time
            segundos = int(segundos_totales)
            milisegundos = int((segundos_totales - segundos) * 1000)
            label_tiempo_a_estrella.config(text=f"Tiempo Algoritmo A*: {segundos} segundos {milisegundos} milisegundos")

        # Verificar si se encontró un camino
        if final not in came_from:
            messagebox.showerror("Error", "No se pudo encontrar un camino que llegue al punto final")
            return

# Función para obtener los vecinos de una celda
def obtener_vecinos(celda):
    vecinos = []
    row, col = celda
    if row > 0 and (row-1, col) not in muros:
        vecinos.append((row-1, col))
    if row < len(matriz) - 1 and (row+1, col) not in muros:
        vecinos.append((row+1, col))
    if col > 0 and (row, col-1) not in muros:
        vecinos.append((row, col-1))
    if col < len(matriz[0]) - 1 and (row, col+1) not in muros:
        vecinos.append((row, col+1))
    return vecinos

# Función para calcular el costo del movimiento
def costo_movimiento(celda1, celda2):
    row1, col1 = celda1
    row2, col2 = celda2
    if row1 != row2 and col1 != col2:
        return 14  # Diagonal
    else:
        return 10  # Vertical u horizontal

# Función para calcular la heurística (distancia Manhattan)
def heuristica(celda1, celda2):
    row1, col1 = celda1
    row2, col2 = celda2
    return (abs(row1 - row2) + abs(col1 - col2)) * 10

# Función para reconstruir el camino en reversa
def reconstruir_camino(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    # Dibujar el camino en reversa
    for position in reversed(path):
        if position != inicio:
            if position != final:
                dibujar_cuadrado(position[1], position[0], "green")
            root.update()
            root.after(velocidad)

def mostrar_informacion_detalle(event):
    global modo
    if modo == "informacion":
        mostrar_informacion(event)
    else:
        messagebox.showinfo("Información", "Primero debes seleccionar el modo 'Información'.")

# Función para la búsqueda en profundidad (DFS)
def buscar_camino_dfs():
    # Reiniciar los valores de los labels h, g, f, p
    label_h.config(text="h: ")
    label_g.config(text="g: ")
    label_f.config(text="f: ")
    label_p.config(text="p: ")
    label_gh.config(text="F = g + h")
    label_ff.config(text="F = ")
    if not inicio or not final:
        messagebox.showerror("Error", "Debe definir el punto de inicio y el punto final.")
        return
    limpiar_cuadro()
    start_time = time.time()
    stack = [inicio]
    came_from = {}
    visited = set()

    while stack:
        current = stack.pop()
        
        if current == final:
            reconstruir_camino(came_from, current)
            return

        if current not in visited:
            visited.add(current)
            for neighbor in obtener_vecinos(current):
                if neighbor not in visited:
                    stack.append(neighbor)
                    came_from[neighbor] = current

                    # Actualizar etiquetas de n
                    n_val = obtener_letra(*neighbor)
                    label_n.config(text=f"n: {n_val}")

                    if neighbor != final:  # Si el vecino no es el destino, colorearlo de amarillo
                        dibujar_cuadrado(neighbor[1], neighbor[0], "yellow")
                        root.update()
                        root.after(velocidad)
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        segundos_totales = elapsed_time
                        segundos = int(segundos_totales)
                        milisegundos = int((segundos_totales - segundos) * 1000)
                        label_tiempo_dfs.config(text=f"Tiempo DFS: {segundos} segundos {milisegundos} milisegundos")

    messagebox.showinfo("Resultado", "No se encontró un camino.")

# Función para la búsqueda en anchura (BFS)
def buscar_camino_bfs():
    # Reiniciar los valores de los labels h, g, f, p
    label_h.config(text="h: ")
    label_g.config(text="g: ")
    label_f.config(text="f: ")
    label_p.config(text="p: ")
    label_gh.config(text="F = g + h")
    label_ff.config(text="F = ")
    if not inicio or not final:
        messagebox.showerror("Error", "Debe definir el punto de inicio y el punto final.")
        return
    limpiar_cuadro()
    start_time = time.time()
    queue = deque([inicio])
    came_from = {}
    visited = set()
    visited.add(inicio)

    while queue:
        current = queue.popleft()

        if current == final:
            reconstruir_camino(came_from, current)
            return

        for neighbor in obtener_vecinos(current):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current

                # Actualizar etiquetas de n
                n_val = obtener_letra(*neighbor)
                label_n.config(text=f"n: {n_val}")

                if neighbor != final:  # Si el vecino no es el destino, colorearlo de amarillo
                    dibujar_cuadrado(neighbor[1], neighbor[0], "yellow")
                    root.update()
                    root.after(velocidad)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    segundos_totales = elapsed_time
                    segundos = int(segundos_totales)
                    milisegundos = int((segundos_totales - segundos) * 1000)
                    label_tiempo_bfs.config(text=f"Tiempo BFS: {segundos} segundos {milisegundos} milisegundos")
                    
    messagebox.showinfo("Resultado", "No se encontró un camino.")

# Función para la búsqueda con el algoritmo de Dijkstra
def buscar_camino_dijkstra():
    # Reiniciar los valores de los labels h, g, f, p
    label_h.config(text="h: ")
    label_g.config(text="g: ")
    label_f.config(text="f: ")
    label_p.config(text="p: ")
    label_gh.config(text="F = g + h")
    label_ff.config(text="F = ")
    if not inicio or not final:
        messagebox.showerror("Error", "Debe definir el punto de inicio y el punto final.")
        return
    limpiar_cuadro()
    start_time = time.time()
    frontier = PriorityQueue()
    frontier.put((0, inicio))
    came_from = {}
    cost_so_far = {}
    came_from[inicio] = None
    cost_so_far[inicio] = 0

    while not frontier.empty():
        current_cost, current = frontier.get()

        if current == final:
            reconstruir_camino(came_from, current)  # Llamar a la función de reconstrucción de camino
            return

        for next_node in obtener_vecinos(current):
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                frontier.put((priority, next_node))
                came_from[next_node] = current

                # Actualizar etiqueta de n
                n_val = obtener_letra(*next_node)
                label_n.config(text=f"n: {n_val}")

                if next_node != final:  # Si el vecino no es el destino, colorearlo de amarillo
                    dibujar_cuadrado(next_node[1], next_node[0], "yellow")
                    root.update()
                    root.after(velocidad)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    segundos_totales = elapsed_time
                    segundos = int(segundos_totales)
                    milisegundos = int((segundos_totales - segundos) * 1000)
                    label_tiempo_dijkstra.config(text=f"Tiempo Dijkstra: {segundos} segundos {milisegundos} milisegundos")

    messagebox.showinfo("Resultado", "No se encontró un camino.")

# Función para seleccionar el algoritmo seleccionado
def buscar():
    algoritmo = combo_algoritmo.get()
    if algoritmo == "Algoritmo A*":
        buscar_camino()
    elif algoritmo == "DFS":
        buscar_camino_dfs()
    elif algoritmo == "BFS":
        buscar_camino_bfs()
    elif algoritmo == "Dijkstra":
        buscar_camino_dijkstra()
    else:
        messagebox.showwarning("Advertencia", "Debe seleccionar un algoritmo.")

# Función para reiniciar
def reiniciar():
    global inicio, final, muros
    inicio = None
    final = None
    muros = []
    
    generar_matriz()
    
    # Reiniciar los valores de las etiquetas
    label_h.config(text="h:")
    label_g.config(text="g:")
    label_n.config(text="n:")
    label_f.config(text="f:")
    label_p.config(text="p:")
    label_gh.config(text="F = g + h")
    label_ff.config(text="F = ")
    # Reiniciar los valores de tiempo
    label_tiempo_a_estrella.config(text="Tiempo A*: ")
    label_tiempo_dfs.config(text="Tiempo DFS: ")
    label_tiempo_bfs.config(text="Tiempo BFS: ")
    label_tiempo_dijkstra.config(text="Tiempo Dijkstra: ")

# Funciones para cambiar modos
def activar_modo_inicio():
    global modo
    modo ="inicio"
    canvas.unbind("<Button-1>")  # Desvincular cualquier evento de clic del ratón
    canvas.unbind("<B1-Motion>")  # Desvincular el arrastre de muros
    canvas.bind("<Button-1>", seleccionar_inicio)

def activar_modo_final():
    global modo
    modo = "final"
    canvas.unbind("<Button-1>")  # Desvincular cualquier evento de clic del ratón
    canvas.unbind("<B1-Motion>")  # Desvincular el arrastre de muros
    canvas.bind("<Button-1>", seleccionar_final)

def activar_modo_muros():
    global modo
    modo = "muros"
    canvas.unbind("<Button-1>")  # Desvincular cualquier evento de clic del ratón
    canvas.bind("<Button-1>", seleccionar_muros)
    canvas.bind("<B1-Motion>", arrastrar_muros)  # Vincular el arrastre de muros

def activar_modo_desmarcar():
    global modo
    modo = "desmarcar"
    canvas.unbind("<Button-1>")  # Desvincular cualquier evento de clic del ratón
    canvas.unbind("<B1-Motion>")  # Desvincular el arrastre de muros
    canvas.bind("<Button-1>", desmarcar)

def activar_modo_informacion():
    global modo
    modo = "informacion"
    canvas.unbind("<Button-1>")  # Desvincular cualquier evento de clic del ratón
    canvas.unbind("<B1-Motion>")  # Desvincular el arrastre de muros
    canvas.bind("<Button-1>", mostrar_informacion_detalle)
                
# Función para actualizar la velocidad seleccionada
def actualizar_velocidad(event):
    global velocidad
    velocidad = int(combo_velocidad.get())

# Asignar funciones a los botones y combobox
btn_generar.config(command=generar_matriz)
btn_inicio.config(command=activar_modo_inicio)
btn_final.config(command=activar_modo_final)
btn_informacion.config(command=activar_modo_informacion)
btn_muros.config(command=activar_modo_muros)
btn_desmarcar.config(command=activar_modo_desmarcar)
btn_buscar.config(command=buscar)
btn_reiniciar.config(command=reiniciar)
combo_velocidad.bind("<<ComboboxSelected>>", actualizar_velocidad)

# Iniciar el bucle principal de Tkinter
root.mainloop()