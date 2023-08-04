# Simulación de Sistema Continuo: Masa-Resorte

Este proyecto forma parte de las actividades asignadas para la materia "Simulación". Su finalidad es simular el comportamiento de un sistema masa-resorte mediante el uso del método de Euler, que consiste en un procedimiento numérico para resolver ecuaciones diferenciales.


<img src="assets/friction_exp.gif" alt="nombre_alternativo" style="width: 100%; height: 300;"/>



## Preparación del Entorno / Dependencias

Para este proyecto se requieren las siguientes dependencias:

- [Python >= 3.7](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [ffmpeg](https://ffmpeg.org/download.html) (necesario para generar videos)

Para comprobar si tienes las versiones correctas de Python y pip instaladas, puedes usar los siguientes comandos en tu terminal:

```bash
python --version
pip --version
```
Puedes verificar si ffmpeg está instalado correctamente usando el siguiente comando:

```bash
ffmpeg -version
```

### Instalación de Dependencias del Proyecto:

El archivo `requirements.txt` contiene todas las dependencias específicas del proyecto. Para instalarlas, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

- `assets/`: imágenes y videos de las simulaciones. 
- `constants.py`: constantes utilizadas en el proyecto.
- `euler_mass_spring.py`: implementación del método de Euler para el sistema.
- `experiments.py`:  experimentos con diferentes parámetros y visualizaciones.
- `mass_spring_system.py`:  clase que modela el sistema de masa-resorte
- `parser.py`: procesamiento de los argumentos de la línea de comandos.
- `plotter.py`: clase que genera gráficas a partir de los datos de las simulaciones.
- `run.py`: script principal para ejecutar una simulación.  
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.

## Uso

Para correr una instancia de la simulación del sistema masa-resorte debes ejecutar el script `run.py` con los parámetros proporcionados a través de la línea de comandos. A continuación te explicamos cómo indicar estos parámetros y cómo ejecutar el script.

### Parámetros requeridos

- `-mass`: Masa del sistema.
- `-spring_resistance`: Resistencia del resorte.
- `-friction`: Coeficiente de fricción del sistema.
- `-force`: Fuerza aplicada al sistema.

### Parámetros opcionales

- `-dt`: Intervalo de tiempo para la simulación (por defecto es 0.001).
- `-t`: Tiempo total de simulación (por defecto es 100).
- `-x`: Posición inicial del sistema (por defecto es 0).
- `-v`: Velocidad inicial del sistema (por defecto es 0).

Si quieres saber más sobre cada parámetro y los valores que se usan por defecto, puedes ejecutar el siguiente comando para ver la ayuda del script:

```bash
python run.py -h
```

## Ejemplos de uso

A continuación, se presentan algunos ejemplos de cómo podrías usar el script `run.py`:

```bash
python run.py -mass 1.0 -spring_resistance 1.0 -friction 1.0 -force 1.0
```

Si deseas cambiar el intervalo de tiempo (paso) a 0.01 y el tiempo total de simulación a 200, mientras los demás parámetros se mantienen iguales, debes usar el siguiente comando:

```bash
python run.py -mass 1.0 -spring_resistance 1.0 -friction 1.0 -force 1.0 -dt 0.01 -t 200
```

## Reporte

En el archivo 'report.pdf' encontrarás un análisis detallado de los experimentos más interesantes llevados a cabo durante este proyecto, junto con sus respectivas conclusiones y contrastación con soluciones analíticas.

Por otro diferentes archivos multimedia (mp4,gif,png) basados en experimentos ya realizados se encuentran disponibles en la carpeta 'assets'. Algunos ejemplos de ellos son los siguientes:

![nombre_alternativo](assets/force_exp.gif)


