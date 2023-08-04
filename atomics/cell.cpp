#include "cell.h"
void cell::init(double t,...) {
va_list parameters;
va_start(parameters,t);

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
GameState* game = (GameState*)x.value;
int cid = state[CID];

int alives = count_alives(game->rows,game->cols,cid,game->board);

state[LIFE_STATE] = game->board[cid];

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

if (game->board[cid] == state[LIFE_STATE])
	sigma = inf;
else
	sigma = 1;


}
Event cell::lambda(double t) {
return Event(state,0);
}
void cell::exit() {
//Code executed at the end of the simulation.

}
