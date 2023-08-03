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
state[CID] = getScilabVar(fvar);
inf = 1e10;
sigma=inf;
}
double cell::ta(double t) {
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
int cid = state[CID];

int alives = count_alives(game->rows,game->cols,cid,game->storage);
state[LIFE_STATE] = game->storage[cid];

// Cell is currently alive
if (state[LIFE_STATE] == ALIVE) {
    // Check if 'alives' is in the 'survivor_rules' array
    if (!game->survivor_rules[alives])
        state[LIFE_STATE] = DEAD;  // Cell dies
}
// Cell is currently dead
else {
    // Check if 'alives' is in the 'birth_rules' array
    if (game->birth_rules[alives])
        state[LIFE_STATE] = ALIVE;  // Cell becomes alive 
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
