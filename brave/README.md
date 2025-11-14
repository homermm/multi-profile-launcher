# Lanzador de Perfiles de Brave (Windows)

Este script de Python (lanzar_perfiles.py) te permite lanzar múltiples instancias de perfiles de Brave en Windows, cada una con una URL específica.

A diferencia de la versión de Firefox, Brave (basado en Chromium) no requiere un script de "creación" separado. Los perfiles se crean automáticamente si no existen la primera vez que se lanzan.

##  ¡Configuración Obligatoria!

Antes de ejecutar el script, debes **editar el archivo lanzar_perfiles.py** y actualizar la variable path_brave para que coincida con tu instalación.

1. Busca el ícono de Brave (en el escritorio o menú de inicio).
2. Haz clic derecho sobre él y selecciona **"Propiedades"**.
3. En la pestaña "Acceso directo", copia la ruta completa del campo **"Destino"** (Target).
4. Pega esa ruta completa dentro de las comillas "..." en el script.

*Ejemplo de la variable en el script:*
```python
# ¡¡MUY IMPORTANTE!!
# Esta es la ruta estándar. Verifícala en tu PC.
path_brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
```

## Scripts Disponibles

### lanzar_perfiles.py
Lanza múltiples perfiles de Brave con una URL específica.

**Uso:**
```powershell
python lanzar_perfiles.py
```

Te pedirá:
- La URL a abrir (ej: google.com)
- El número de sesiones/perfiles a lanzar

### limpiar_perfiles.py
Elimina automáticamente todos los perfiles de Brave creados, liberando espacio en disco.

**Características:**
- Cierra automáticamente Brave antes de borrar
- Muestra el tamaño de cada perfil
- Elimina tanto las carpetas como los metadatos (Local State)
- Solicita confirmación antes de borrar

**Uso:**
```powershell
python limpiar_perfiles.py
```

 **Nota:** Este script borra todos los perfiles excepto el "Default". Responde "s" para confirmar la eliminación.
