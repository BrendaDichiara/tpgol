//CPP:random/mediator.cpp
#if !defined mediator_h
#define mediator_h

#include "simulator.h"
#include "event.h"
#include "stdarg.h"

#include "fstream"
#include "string"
#include "iostream"


class mediator: public Simulator { 
// Declare the state,
// output variables
// and parameters
int* storage;
double sigma;
float inf;
typedef struct {
    int* storage;
    int rows;
    int cols;
} GameState;

GameState* game;

public:
	mediator(const char *n): Simulator(n) {};
	void init(double, ...);
	double ta(double t);
	void dint(double);
	void dext(Event , double );
	Event lambda(double);
	void exit();
};
#endif
