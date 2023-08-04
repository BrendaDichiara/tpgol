#include "utilit.h"

// Function to count the number of alive cells surrounding a given cell in a board
int count_alives(int rows, int cols, int cell_id, int *board)
{
    int count_alives = 0;
    int row = cell_id / cols;
    int col = cell_id % cols;
    for (int rowDelta = -1; rowDelta <= 1; rowDelta++)
    {
        for (int colDelta = -1; colDelta <= 1; colDelta++)
        {
            // Ignore current cell
            if (rowDelta == 0 && colDelta == 0)
                continue;

            // Compute the row and column indices of the neighboring cell
            int newRow = row + rowDelta;
            int newCol = col + colDelta;

            // Check if the indices are valid
            if (newRow < 0 || newRow >= rows || newCol < 0 || newCol >= cols)
                continue;

            int neighbor = newRow * cols + newCol;
            // If the neighboring cell is alive, increment the counter
            if (board[neighbor] == 1)
                count_alives++;
        }
    }
    return count_alives;
}
