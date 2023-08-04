//CPP:gol/cell.cpp
#if !defined cell_h
#define cell_h

#include "simulator.h"
#include "event.h"
#include "stdarg.h"

#include "gol/mediator.h"


class cell: public Simulator { 
double sigma;
float inf;
int state[2];
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
