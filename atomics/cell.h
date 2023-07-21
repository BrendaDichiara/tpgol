//CPP:random/cell.cpp
#if !defined cell_h
#define cell_h

#include "simulator.h"
#include "event.h"
#include "stdarg.h"



class cell: public Simulator { 
// Declare the state,
// output variables
// and parameters
double sigma;
float inf;
int state[2];

int CID;
typedef struct {
    int* storage;
    int rows;
    int cols;
} GameState;

GameState* game;

public:
	cell(const char *n): Simulator(n) {};
	void init(double, ...);
	double ta(double t);
	void dint(double);
	void dext(Event , double );
	Event lambda(double);
	void exit();
};
#endif
