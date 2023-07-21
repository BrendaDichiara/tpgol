#include "mediator.h"
void mediator::init(double t,...) {
//The 'parameters' variable contains the parameters transferred from the editor.
va_list parameters;
va_start(parameters,t);

//To get a parameter: %Name% = va_arg(parameters,%Type%)
//where:
//      %Name% is the parameter name
//	%Type% is the parameter type

char* file_name_raw = va_arg(parameters, char*);

std::ifstream file;
std::string file_name = "../tpgol/patterns/" + std::string(file_name_raw) + ".txt";
//printLog("nombre %s", file_name.c_str());

file.open(file_name.data());
if (!file.is_open()) {
    std::cerr << "Error openinggg file\n";
    return;  // or exit(-1), or throw an exception, etc.
}

int rows, cols;
file >> rows;
file >> cols;

// Inicialización de la estructura GameState
game = (GameState*) malloc(sizeof(GameState));
game->storage = (int *) malloc(sizeof(int) * (rows*cols + 1));
game->rows = rows;  // Supongo que las filas son igual al size
game->cols = cols;  // Supongo que las columnas son igual al size



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
file.close();


inf = 1e10;
sigma = 1; 
}
double mediator::ta(double t) {
//This function returns a double.
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
game->storage[cell_state[0]] = cell_state[1];
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
        state = (game->storage[i*game->rows + j] == 1) ? 'V' : 'M';
        printLog("%c ", state);
    }
    printLog("\n");
}


return Event(game, 0);
}
void mediator::exit() {
//Code executed at the end of the simulation.

}
