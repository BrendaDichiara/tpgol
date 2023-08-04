# Simulación del Juego de la Vida en PowerDEVS

Este proyecto fue desarrollado en el marco de la entrega final para la materia "Simulación". Consiste en la implementación del famoso "Juego de la Vida" de Conway utilizando PowerDEVS, un entorno de simulación de eventos discretos. 

![nombre_alternativo](assets/collage.png)

## Preparación del Entorno / Dependencias

Para este proyecto, se requiere lo siguiente:

- [Python >= 3.7](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [PillowWriter](https://pypi.org/project/PillowWriter/) (necesario para generar gifs)
Para verificar las versiones de Python y pip instaladas, se pueden usar los siguientes comandos en la terminal:
- [PowerDEVS](https://sourceforge.net/projects/powerdevs/)
```bash
python --version
pip --version
```

## Instalación de Dependencias del Proyecto:

El archivo `requirements.txt` contiene todas las dependencias específicas del proyecto. Para instalarlas, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

- `assets/`: imágenes y videos de las simulaciones.
- `atomics/`: modelos atómicos de PowerDEVS para el proyecto.
- `examples/`: modelos PDM de diferentes tableros y configuraciones.
- `lib/`: archivo.dpl y assets que representan la librería del proyecto para PowerDEVS.
- `patterns/` archivos .txt que representan diferentes patrones para el juego.
- `docs/`: documentación del proyecto y guía de uso de 'Settings GoL' herramienta de ayuda para la configuración del proyecto basado en GUI (Graphical User Interface).
- `gen_pdm.py`: script que permite generar un esquema PDM de tamaño NxM listo para ser ejecutado, evitando tener que crearlo manualmente.
- `gui.py` script que permite configurar el proyecto de manera gráfica, se aconseja leer la guía de uso disponible en `docs/guía_de_uso_settings_gol`. ya que entre otras funciones, permite la creación de archivos de configuración de manera visual, asi como también la creación de patrones personalizados y esquemas PDM.
- `build.sh` script que permite construir el proyecto de manera automática, más abajo se explica, otra opción para buildear el proyecto es utilizar la interfaz gráfica gui.py
- `restore.sh` script que permite volver PowerDEVS a su versión previa a la instalación del proyecto, esto es útil en caso de que se quiera desinstalar el proyecto.



## Configuración del Entorno

El primer paso es clonar este proyecto en su directorio raiz de PowerDevs 
    
    ```bash
    git clone
    ```

Para configurar PowerDEVS y poder hacer uso de este proyecto así como sus ejemplos,librerías y modelos se necesita configurarlo, afortunadamente se provee un script que facilita este proceso por usted `build.sh`. Asegúrate de tener los permisos necesarios para ejecutar este script. Si no es así, puedes cambiar los permisos con el siguiente comando:

```bash
chmod +x build.sh
```
El script realiza por usted (entre otras cosas) las siguientes configuraciones:
- Incorpora la libreria del proyecto a PowerDEVS, la misma tiene el nombre de "Game of Life" en la misma se encuentran los modelos atómicos, asi como también ejemplos de tableros de tamaños NxM (3x3),(5x5),(8x8),(25x38) listos para ser ejecutados.
- Incorpora los modelos atómicos cell, mediator así como utilidades necesarias.
- Incorpora una carpeta patterns que contiene patrones de ejemplo listos para ser cargados en la simulación que usted desee.
- Incorpora una carpeta examples que contiene modelos PDM de ejemplo listos para ser ejecutados.

Si por algun motivo desea desinstalar el proyecto, se provee un script que permite volver PowerDEVS a su estado previo a la instalación del proyecto, para ello:

```bash
chmod +x restore.sh
```
Este proceso también puede ser realizado de manera gráfica utilizando el script `gui.py`

![nombre_alternativo](report/readme_imgs/build.png)
---


## Uso 

El estado inicial se obtiene de un archivo.txt, una vez seteado el proyecto, encontrará en su raiz del directorio de PowerDEVS una carpeta llamada "patterns", dentro de la misma diferentes patrones/archivos.txt, el Mediator recibe como 1er parámetro el nombre del archivo/input el cuál tiene el siguiente formato:

```
<cantidad de filas>
<cantidad de columnas>
<tablero inicial (0 muerto, 1 vivo)>
<reglas de supervivencia>
<reglas de nacimiento>
```

Por ejemplo, un blinker en un 3x3 se vería de la siguiente manera:

```
3
3
0 1 0
0 1 0
0 1 0
23
3
```

Puesto que la creación de patrones en este formato puede ser un proceso laborioso, especialmente para tableros de grandes dimensiones, proveemos una pestaña dentro de la herramienta de ayuda "settings GoL' que permite la creación de patrones de manera visual,






