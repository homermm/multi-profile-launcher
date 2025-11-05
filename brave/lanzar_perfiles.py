#!/usr/bin/env python3
import subprocess
import sys
import os

# --- 1. Definir la ruta a Brave ---
# ¡¡MUY IMPORTANTE!!
# Esta es la ruta estándar. Verifícala en tu PC.
# Puede estar en "Program Files (x86)" si tienes una versión de 32 bits.
# Haz clic derecho en el ícono de Brave -> Propiedades -> Copia la ruta de "Destino".

path_brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Verificar si el archivo existe antes de continuar
if not os.path.exists(path_brave):
    print(f"Error: No se encontró 'brave.exe' en la ruta:", file=sys.stderr)
    print(f"{path_brave}", file=sys.stderr)
    print("Por favor, edita el script y corrige la variable 'path_brave'.", file=sys.stderr)
    sys.exit(1)


# --- 2. Preguntar por la URL ---
url = input("Introduce la URL (ej: google.com): ")

# Asegurarse de que la URL tenga https://
if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url

# --- 3. Preguntar por el número de sesiones ---
try:
    num_sesiones_str = input("¿Cuántas sesiones (perfiles) quieres abrir? ")
    num_sesiones = int(num_sesiones_str)
    
    if num_sesiones <= 0:
        raise ValueError("El número debe ser mayor que cero")

except ValueError as e:
    print(f"Error: Entrada inválida. Debes escribir un número entero positivo.", file=sys.stderr)
    sys.exit(1) # Termina el script con un error

# --- 4. Lanzar los perfiles ---
print(f"\nAbriendo {num_sesiones} perfiles de Brave en '{url}'...")

for i in range(1, num_sesiones + 1):
    # Brave usa nombres como "Profile 1", "Profile 2" por defecto.
    # (El perfil principal se llama "Default")
    profile_name = f"Profile {i}" 
    
    print(f"Lanzando {profile_name}...")
    
    # Comando para abrir una nueva instancia de Brave con un perfil específico y una URL
    # --profile-directory="Nombre" es la clave.
    command = [
        path_brave,
        f"--profile-directory={profile_name}",
        url
    ]
    
    try:
        # Usamos Popen para que el script no se quede esperando a que cierres
        # una ventana antes de abrir la siguiente.
        subprocess.Popen(command)
    
    except Exception as e:
        # Este error ahora es más genérico, ya que FileNotFoundError
        # se captura arriba.
        print(f"No se pudo lanzar {profile_name}. Error: {e}", file=sys.stderr)

print(f"\n¡Se han lanzado {num_sesiones} sesiones!")