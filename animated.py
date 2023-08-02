import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Leemos el archivo .log
name = 'herschel'
size= 8
with open(f'logs/{name}.log', 'r') as file:
    lines = file.readlines()

# Buscamos todas las apariciones de tableros
boards = []
current_board = []
for line in lines:
    if line.strip() == 'MEDIATOR: Tablero':
        # Comenzamos un nuevo tablero
        current_board = []
    elif line.strip() == 'Simulation Initialized':
        continue
    else:
        # Agregamos la línea al tablero actual
        current_board.append([0 if cell == 'M' else 1 for cell in line.split()])
        if len(current_board) == size:
            # Si el tablero está completo, lo agregamos a la lista de tableros
            boards.append(np.array(current_board))

fig, ax = plt.subplots()

def animate(i):
    ax.imshow(boards[i], cmap='binary', vmin=0, vmax=1)
    ax.set_title(f"Time {i}")  # Ajusta el título para mostrar el paso de tiempo actual
    
    #filename = f"{name}_{i}.png" 
    
    #plt.savefig(filename, bbox_inches='tight')

    # Generar líneas verticales
    for i in range(size):
        plt.axvline(x=i + 0.5, color='gray', lw=1)

    # Generar líneas horizontales
    for j in range(size):
        plt.axhline(y=j + 0.5, color='gray', lw=1)

    plt.xticks([])
    plt.yticks([])

  
ani = animation.FuncAnimation(fig, animate, frames=len(boards), interval=1500, repeat=False)
ani.save(f'{name}.gif', writer='ffmpeg', fps=1)

plt.show()

