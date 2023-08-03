#if !defined UTILIT
#define UTILIT
#define CID 0
#define LIFE_STATE 1
#define ALIVE 1
#define DEAD 0

int suma(int a, int b);
int count_alives(int rows, int cols, int cell_id, int *board);

typedef struct
{
    int *storage;
    int rows;
    int cols;
    int survivor_rules[9];
    int birth_rules[9];
} GameState;

#endif