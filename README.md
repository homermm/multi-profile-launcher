# Lanzador Múltiple de Perfiles de Firefox

Este proyecto contiene dos scripts de Python diseñados para crear y lanzar múltiples perfiles de Firefox de forma automatizada en un sistema Linux (específicamente probado en Fedora).

Es útil para desarrolladores web o testers que necesitan probar un sitio web en múltiples sesiones limpias y aisladas.

## Scripts

El proyecto se compone de dos scripts:

1.  `crear_perfiles.py`
2.  `lanzar_perfiles.py`

## Requisitos

* Python 3
* Firefox (instalado en la ruta `/usr/bin/firefox`)
* Sistema operativo Linux (Fedora, Ubuntu, etc.)

## 1. `crear_perfiles.py`

Este script crea una cantidad definida de perfiles nuevos de Firefox. Los perfiles se nombran numéricamente (`01`, `02`, `03`, ...).

### Uso

1.  Abre el archivo `crear_perfiles.py` con un editor de texto.
2.  Modifica la variable `CANTIDAD_A_CREAR` al número de perfiles que deseas generar.
    ```python
    # Define cuántos perfiles quieres crear
    CANTIDAD_A_CREAR = 5 
    ```
3.  Ejecuta el script desde tu terminal:
    ```bash
    python3 crear_perfiles.py
    ```
4.  El script te informará si los perfiles se crearon o si ya existían.

## 2. `lanzar_perfiles.py`

Este script lanza una nueva instancia de Firefox por cada perfil creado, abriendo una URL específica.

### Uso

**Importante:** Debes haber ejecutado `crear_perfiles.py` al menos una vez para que los perfiles (`01`, `02`, etc.) existan.

1.  Abre el archivo `lanzar_perfiles.py` con un editor de texto.
2.  Modifica la variable `CANTIDAD_A_LANZAR` para que coincida con el número de perfiles que quieres abrir.
3.  (Opcional) Modifica la variable `url_generica` para apuntar al sitio web que deseas probar.
    ```python
    # Define cuántas instancias quieres lanzar
    CANTIDAD_A_LANZAR = 5 

    # URL de ejemplo para demostración
    url_generica = "[http://example.com](http://example.com)"
    ```
4.  Ejecuta el script desde tu terminal:
    ```bash
    python3 lanzar_perfiles.py
    ```

### Advertencia de Recursos

Lanzar una gran cantidad de instancias de Firefox (ej. 10, 20, 30...) consumirá una cantidad significativa de RAM y CPU. Asegúrate de que tu sistema pueda manejar la carga antes de definir un número alto.