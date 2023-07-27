#include "utilit.h"

int suma(int a, int b)
{
    return a + b;
}

int count_alives(int rows, int cols, int cell_id, int *board)
{
    int count_alives = 0;
    int row = cell_id / rows;
    int col = cell_id % cols;
    for (int rowDelta = -1; rowDelta <= 1; rowDelta++)
    {
        for (int colDelta = -1; colDelta <= 1; colDelta++)
        {
            // Ignore displacement (0,0) as it's the current cell
            if (rowDelta == 0 && colDelta == 0)
                continue;

            int newRow = row + rowDelta;
            int newCol = col + colDelta;

            // Check if the indices are valid
            if (newRow < 0 || newRow >= rows || newCol < 0 || newCol >= cols)
                continue;

            int neighbor = newRow * rows + newCol;
            if (board[neighbor] == 1)
                count_alives++;
        }
    }
    return count_alives;
}
