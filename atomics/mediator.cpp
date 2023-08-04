#include "mediator.h"
void mediator::init(double t,...) {
va_list parameters;
va_start(parameters,t);
// I/O filename's
char* file_name_raw = va_arg(parameters, char*);
char* output_filename = va_arg(parameters,char*);
output_filename_str = std::string(output_filename) + ".log";
std::ifstream file;
std::string file_name = "../patterns/" + std::string(file_name_raw) + ".txt";


file.open(file_name.data());
if (!file.is_open()) {
    std::cerr << "Error openinggg file\n";
    return; 
}

int rows, cols;
file >> rows;
file >> cols;

//Initialization of GameState structure
game = (GameState*) malloc(sizeof(GameState));
game->board = (int *) malloc(sizeof(int) * (rows*cols + 1));
game->rows = rows;  
game->cols = cols;  

for (int i = 0; i < rows * cols; i++) {
    char cell;
    file >> cell;
    if (cell == '0') {
        game->board[i] = 0;
    } else if (cell == '1') {
        game->board[i] = 1;
    } else {
        std::cerr << "Unexpected character in file\n";
        return; 
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
					 game->survivor_rules[i] = false; 
		 };
}
for (size_t i = 0; i < birth_rules.length(); i++) {
    char c = birth_rules[i];
    if (isdigit(c)) {
        game->birth_rules[c - '0'] = true;
    }
		 else{
			 		 game->survivor_rules[i] = false;
		 };
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
int* cell_state = (int*)x.value;
game->board[cell_state[CID]] = cell_state[LIFE_STATE];
sigma = 1;
}
Event mediator::lambda(double t) {
char state;

std::ofstream log_file;
log_file.open(output_filename_str.c_str(), std::ios::app); 

if(!log_file) {
    std::cerr << "Could not open the log file" << output_filename_str << std::endl;
		 exit();
}

log_file << "MEDIATOR: Tablero\n";
printLog("MEDIATOR: Tablero\n");

for(int i=0; i<game->rows; i++) {
    for(int j=0; j<game->cols; j++) {
        state = (game->board[i*game->cols + j] == 1) ? 'V' : 'M';
        log_file << state << " ";
        printLog("%c ", state);
    }
    log_file << "\n";
    printLog("\n");
}

log_file.close();

return Event(game, 0);

}
void mediator::exit() {
//Code executed at the end of the simulation.

}
