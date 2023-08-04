import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Parse the command line arguments.
parser = argparse.ArgumentParser()
parser.add_argument("-N", "--N", type=int, help="The number of rows in board.")
parser.add_argument("-M", "--M", type=int, help="The number of columns in board.")
parser.add_argument("-i", "--input_file", type=str, help="The name of the input file.")
parser.add_argument("-o", "--output_file", type=str, help="The name of the output file.")
parser.add_argument("-p", "--plot_or_gif", type=str, choices=['plot', 'gif'], help="Specify 'plot' to generate a plot, 'gif' to generate a gif")

args = parser.parse_args()


def read_file(file_name):
  """
    This function reads a file and returns a list of boards.

    Parameters:
    file_name : str
        The name of the file to read.

    Returns:
    list
        A list of boards, where each board is a numpy array.
  """
  file_name = f'../output/gol/{file_name}.log'
  with open(file_name, 'r') as file:
    lines = file.readlines()

  boards = []
  current_board = []

  for line in lines:
    if line.strip() == 'MEDIATOR: Tablero':
      current_board = []
    elif line.strip() == 'Simulation Initialized':
      continue
    else:
      row = [0 if cell == 'M' else 1 for cell in line.split()]
      current_board.append(row)
      
      if len(current_board) == args.N:
        boards.append(np.array(current_board))

  return boards

def plot_simulation():

  """
     This function reads the simulation boards from an input file and plots them as an animation.
  """
 
  boards = read_file(args.input_file)
  fig, ax = plt.subplots()

  for i in range(args.M):
    plt.axvline(x=i + 0.5, color='gray', lw=2)

  for j in range(args.N):
    plt.axhline(y=j + 0.5, color='gray', lw=2)

  plt.xticks([])
  plt.yticks([])

  im = ax.imshow(boards[0], cmap='binary', vmin=0, vmax=1) 
  
  def animate(i):
    im.set_array(boards[i])  
    ax.set_title(f"Gen {i}")  

  ani = animation.FuncAnimation(fig, animate, frames=len(boards), interval=1000, repeat=False)
  
  if args.plot_or_gif == 'gif':
    ani.save(f'{args.output_file}.gif', writer='PillowWriter', fps=1)
  
  plt.show()

if __name__ == "__main__":
  plot_simulation()
