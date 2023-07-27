#include "cell.h"
void cell::init(double t,...) {
//The 'parameters' variable contains the parameters transferred from the editor.
va_list parameters;
va_start(parameters,t);
//To get a parameter: %Name% = va_arg(parameters,%Type%)
//where:
//      %Name% is the parameter name
//	%Type% is the parameter type
char *fvar=va_arg(parameters,char*);
CID = getScilabVar(fvar);
state[0] = CID;

inf = 1e10;
sigma=inf;
}
double cell::ta(double t) {
//This function returns a double.
return sigma;
}
void cell::dint(double t) {
sigma=inf;
}
void cell::dext(Event x, double t) {
//The input event is in the 'x' variable.
//where:
//     'x.value' is the value (pointer to void)
//     'x.port' is the port number
//     'e' is the time elapsed since last transition
GameState* game = (GameState*)x.value;
int size = game->rows;
int count_alives = 0;
int row = CID / size;
int col = CID % size;
for (int rowDelta = -1; rowDelta <= 1; rowDelta++) {
    for (int colDelta = -1; colDelta <= 1; colDelta++) {
        // Ignore displacement (0,0) as it's the current cell
        if (rowDelta == 0 && colDelta == 0)
            continue;

        int newRow = row + rowDelta;
        int newCol = col + colDelta;

        // Check if the indices are valid
        if (newRow < 0 || newRow >= size || newCol < 0 || newCol >= size)
            continue;

        int neighbor = newRow * size + newCol;
        if (game->storage[neighbor] == 1)
            count_alives++;
    }
}

state[1] = game->storage[CID];
// Cell is currently alive
if (state[1] == 1) {
    if (count_alives < 2 || count_alives > 3)
        state[1] = 0;  // Cell dies
}
// Cell is currently dead
else {
    if (count_alives == 3)
        state[1] = 1;  // Cell becomes alive 
}
sigma = 1;

}
Event cell::lambda(double t) {
//This function returns an Event:
//     Event(%&Value%, %NroPort%)
//where:
//     %&Value% points to the variable which contains the value.
//     %NroPort% is the port number (from 0 to n-1)

return Event(state,0);
}
void cell::exit() {
//Code executed at the end of the simulation.

}
