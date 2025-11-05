# Lanzador de Perfiles de Firefox

Este proyecto contiene un conjunto de scripts de Python para crear y lanzar múltiples perfiles de Firefox de forma masiva. Es ideal para tareas que requieren sesiones de usuario separadas, como testing de aplicaciones web, gestión de múltiples cuentas sociales, o cualquier actividad que se beneficie del aislamiento de perfiles.

## Características

* **Creación masiva:** `crear_perfiles.py` te permite crear una cantidad específica de perfiles de Firefox (nombrados `01`, `02`, `03`, ...).
* **Lanzador interactivo:** `lanzar_perfiles.py` te pregunta:
    1.  La URL que deseas abrir.
    2.  Cuántos perfiles (sesiones) deseas lanzar.
* **Instancias separadas:** Cada perfil se lanza como una nueva instancia de Firefox, asegurando que las sesiones no se mezclen.

## Requisitos

* Un sistema operativo basado en Linux (Probado en Fedora).
* Python 3 (generalmente preinstalado).
* Firefox instalado.

## Instalación y Configuración

1.  **Clona o descarga este repositorio:**
2.  **Dar permisos de ejecución:**
    Es fundamental dar permisos a los scripts para que el sistema operativo te permita ejecutarlos como programas.
    ```bash
    chmod +x crear_perfiles.py
    chmod +x lanzar_perfiles.py
    ```

## Modo de Uso

El flujo de trabajo es simple: primero creas los perfiles (solo una vez) y luego los lanzas cuantas veces quieras.

### 1. Crear Perfiles (Ejecutar solo una vez)

Antes de lanzar sesiones, necesitas crear los perfiles.

```bash
./crear_perfiles.py