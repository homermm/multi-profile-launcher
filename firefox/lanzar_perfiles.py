#!/usr/bin/env python3
import subprocess
import sys

# --- 1. Preguntar por la URL ---
url = input("Introduce la URL (ej: google.com): ")

# Asegurarse de que la URL tenga https:// para que Firefox la abra correctamente
if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url

# --- 2. Preguntar por el número de sesiones ---
try:
    num_sesiones_str = input("¿Cuántas sesiones (perfiles) quieres abrir? ")
    num_sesiones = int(num_sesiones_str)
    
    if num_sesiones <= 0:
        raise ValueError("El número debe ser mayor que cero")

except ValueError as e:
    print(f"Error: Entrada inválida. Debes escribir un número entero positivo.", file=sys.stderr)
    sys.exit(1) # Termina el script con un error

# --- 3. Lanzar los perfiles ---
print(f"\nAbriendo {num_sesiones} perfiles en '{url}'...")

for i in range(1, num_sesiones + 1):
    profile_name = f"{i:02d}"
    
    print(f"Lanzando {profile_name}...")
    
    # Comando para abrir una nueva instancia de Firefox con un perfil específico y una URL
    command = [
        "firefox",
        "--new-instance", # Asegura que sea una instancia nueva
        "-P",             # Flag para indicar el nombre del perfil
        profile_name,     # El nombre del perfil
        url               # La URL a abrir
    ]
    
    try:
        # Usamos Popen para que el script no se quede esperando a que cierres
        # una ventana de Firefox antes de abrir la siguiente. Lanza todas a la vez.
        subprocess.Popen(command)
    
    except FileNotFoundError:
        print(f"Error: No se encontró el comando 'firefox'. ¿Está instalado?", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"No se pudo lanzar {profile_name}. ¿Existe ese perfil? Error: {e}", file=sys.stderr)

print(f"\n¡Se han lanzado {num_sesiones} sesiones!")