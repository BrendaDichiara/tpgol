import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Leemos el archivo .log
name = 'gosper_2'
with open(f'logs/{name}.log', 'r') as file:
    lines = file.readlines()

# Buscamos todas las apariciones de tableros
boards = []
current_board = []
N = 25  # Filas
M = 38  # Columnas
for line in lines:
    if line.strip() == 'MEDIATOR: Tablero':
        # Comenzamos un nuevo tablero
        current_board = []
    elif line.strip() == 'Simulation Initialized':
        continue
    else:
        # Agregamos la línea al tablero actual
        row = [0 if cell == 'M' else 1 for cell in line.split()]
        current_board.append(row)
        # Si el tablero está completo, lo agregamos a la lista de tableros
        if len(current_board) == N:
            boards.append(np.array(current_board))

fig, ax = plt.subplots()

# Generar líneas verticales
for i in range(M):
    plt.axvline(x=i + 0.5, color='gray', lw=2)

# Generar líneas horizontales
for j in range(N):
    plt.axhline(y=j + 0.5, color='gray', lw=2)

plt.xticks([])
plt.yticks([])

im = ax.imshow(boards[0], cmap='binary', vmin=0, vmax=1)  # Primera imagen

def animate(i):
    im.set_array(boards[i])  # Actualizamos la imagen
    ax.set_title(f"Gen {i}")  # Ajusta el título para mostrar el paso de tiempo actual

ani = animation.FuncAnimation(fig, animate, frames=len(boards), interval=500, repeat=False)
ani.save(f'{name}.gif', writer='PillowWriter', fps=10)
plt.show()
