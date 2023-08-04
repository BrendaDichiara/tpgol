import argparse
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def parse_args():
    """
    This function parses the command-line arguments.

    Returns:
        The parsed command-line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type=str, help="The name of the input file.", required=True)
    parser.add_argument("-o", "--output_file", type=str, help="The name of the output file.", required=True)
      
    return parser.parse_args()

args = parse_args()

def get_board_dimensions(input_file_path):
    """
    This function reads the input file and determines the dimensions of the board.

    Returns:
        N: The number of rows in the board.
        M: The number of columns in the board.
    """
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    start_index = lines.index("MEDIATOR: Tablero\n") + 1
    stop_index = lines.index("MEDIATOR: Tablero\n", start_index)

    N = stop_index - start_index
    M = len(lines[start_index].split())

    return N, M

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
  file_name = f'../output/{file_name}.log'
  with open(file_name, 'r') as file:
    lines = file.readlines()
  N,M = get_board_dimensions(file_name)
  boards = []
  current_board = []

  for line in lines:
    if line.strip() == 'MEDIATOR: Tablero':
      current_board = []
    else:
      row = [0 if cell == 'M' else 1 for cell in line.split()]
      current_board.append(row)
      
      if len(current_board) == N:
        boards.append(np.array(current_board))

  return boards,N,M

def plot_simulation():
  """
     This function reads the simulation boards from an input file and plots them as an animation.
  """
  boards,N,M = read_file(args.input_file)
  fig, ax = plt.subplots()

  for i in range(M):
    plt.axvline(x=i + 0.5, color='gray', lw=2)

  for j in range(N):
    plt.axhline(y=j + 0.5, color='gray', lw=2)

  plt.xticks([])
  plt.yticks([])

  im = ax.imshow(boards[0], cmap='binary', vmin=0, vmax=1) 
  
  def animate(i):
    im.set_array(boards[i])  
    ax.set_title(f"Gen {i}")  
 
  ani = animation.FuncAnimation(fig, animate, frames=len(boards), interval=1000, repeat=False)
  ani.save(f'{args.output_file}.gif', writer='Pillow', fps=1)
  
  plt.show()

if __name__ == "__main__":
  plot_simulation()
