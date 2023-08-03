#include "mediator.h"
void mediator::init(double t,...) {
va_list parameters;
va_start(parameters,t);
char* file_name_raw = va_arg(parameters, char*);

std::ifstream file;
std::string file_name = "../patterns/" + std::string(file_name_raw) + ".txt";

file.open(file_name.data());
if (!file.is_open()) {
    std::cerr << "Error openinggg file\n";
    return;  // or exit(-1), or throw an exception, etc.
}

int rows, cols;
file >> rows;
file >> cols;

//Initialization of GameState structure
game = (GameState*) malloc(sizeof(GameState));
game->storage = (int *) malloc(sizeof(int) * (rows*cols + 1));
game->rows = rows;  
game->cols = cols;  

for (int i = 0; i < rows * cols; i++) {
    char cell;
    file >> cell;
    if (cell == '0') {
        game->storage[i] = 0;
    } else if (cell == '1') {
        game->storage[i] = 1;
    } else {
        std::cerr << "Unexpected character in file\n";
        return;  // or exit(-1), or throw an exception, etc.
    }
}

// Read survivor and birth rules
std::string survivor_rules, birth_rules;
file >> survivor_rules;
file >> birth_rules;

// Convert rules from string to array
for (size_t i = 0; i < survivor_rules.length(); i++) {
    char c = survivor_rules[i];
    if (isdigit(c)) {
        game->survivor_rules[c - '0'] = true;
    }else{
					 game->survivor_rules[i] = false; };
}
for (size_t i = 0; i < birth_rules.length(); i++) {
    char c = birth_rules[i];
    if (isdigit(c)) {
        game->birth_rules[c - '0'] = true;
    }
else{
					 game->survivor_rules[i] = false; };
}

file.close();

inf = 1e10;
sigma = 1; 

}
double mediator::ta(double t) {
return sigma;
}
void mediator::dint(double t) {
sigma = inf;
}
void mediator::dext(Event x, double t) {
//The input event is in the 'x' variable.
//where:
//     'x.value' is the value (pointer to void)
//     'x.port' is the port number
//     'e' is the time elapsed since last transition
int* cell_state = (int*)x.value;
game->storage[cell_state[CID]] = cell_state[LIFE_STATE];
sigma = 1;
}
Event mediator::lambda(double t) {
//This function returns an Event:
//     Event(%&Value%, %NroPort%)
//where:
//     %&Value% points to the variable which contains the value.
//     %NroPort% is the port number (from 0 to n-1)

char state;

printLog("MEDIATOR: Tablero\n");

for(int i=0; i<game->rows; i++) {
    for(int j=0; j<game->cols; j++) {
        // Change the indexing to 'i * game->cols + j'
        state = (game->storage[i*game->cols + j] == 1) ? 'V' : 'M';
        printLog("%c ", state);
    }
    printLog("\n");
}

return Event(game, 0);

}
void mediator::exit() {
//Code executed at the end of the simulation.

}
