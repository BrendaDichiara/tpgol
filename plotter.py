import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def read_file(file_name,N):
  """Leer el archivo de entrada y devolver una lista de listas de enteros.

  Args:
    file_name: El nombre del archivo de entrada.

  Returns:
    Una lista de listas de enteros, donde cada lista representa una fila del tablero.
  """
  file_name = f'../output/gol/{file_name}.log'
  with open(file_name, 'r') as file:
    lines = file.readlines()

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
      row = [0 if cell == 'M' else 1 for cell in line.split()]
      current_board.append(row)
      # Si el tablero está completo, lo agregamos a la lista de tableros
      if len(current_board) == N:
        boards.append(np.array(current_board))

  return boards

def main():
  # Parse the command line arguments.
  parser = argparse.ArgumentParser()
  parser.add_argument("-N", "--N", type=int, default=25, help="The number of rows in the data.")
  parser.add_argument("-M", "--M", type=int, default=38, help="The number of columns in the data.")
  parser.add_argument("-i", "--input_file", type=str, default="logs/gosper_2.log", help="The name of the input file.")
  parser.add_argument("-o", "--output_file", type=str, default="gosper_2.gif", help="The name of the output file.")

  args = parser.parse_args()

  # Read the data from the input file.
  boards = read_file(args.input_file,args.N)

  # Plot the data.
  fig, ax = plt.subplots()

  # Generar líneas verticales
  for i in range(args.M):
    plt.axvline(x=i + 0.5, color='gray', lw=2)

  # Generar líneas horizontales
  for j in range(args.N):
    plt.axhline(y=j + 0.5, color='gray', lw=2)

  plt.xticks([])
  plt.yticks([])

  im = ax.imshow(boards[0], cmap='binary', vmin=0, vmax=1)  # Primera imagen

  def animate(i):
    im.set_array(boards[i])  # Actualizamos la imagen
    ax.set_title(f"Gen {i}")  # Ajusta el título para mostrar el paso de tiempo actual

  ani = animation.FuncAnimation(fig, animate, frames=len(boards), interval=500, repeat=False)
  ani.save(f'{args.output_file}.gif', writer='PillowWriter', fps=10)
  plt.show()

if __name__ == "__main__":
  main()
