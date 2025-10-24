#!/usr/bin/env python3
import subprocess
import sys

# --- 1. Preguntar cuántos perfiles crear ---
try:
    num_crear_str = input("¿Cuántos perfiles de Firefox NUEVOS quieres crear? (ej: 5): ")
    num_crear = int(num_crear_str)
    
    if num_crear <= 0:
        raise ValueError("El número debe ser mayor que cero")

except ValueError as e:
    print(f"Error: Entrada inválida. Debes escribir un número entero positivo.", file=sys.stderr)
    sys.exit(1)

print(f"\nCreando {num_crear} perfiles nuevos...")

# --- 2. Crear los perfiles en un bucle ---
for i in range(1, num_crear + 1):
    
    profile_name = f"{i:02d}" # Nombres como "01", "02", etc.
    
    print(f"Creando '{profile_name}'...")
    
    # Comando para crear un perfil de Firefox sin abrir una ventana
    command = [
        "firefox",
        "--no-remote",
        "--headless",
        "-CreateProfile",
        profile_name
    ]
    
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        
    except FileNotFoundError:
        print("Error: No se encontró el comando 'firefox'. ¿Está instalado?", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        # Revisa si el error es porque el perfil ya existe
        if "already exists" in e.stderr:
            print(f"Advertencia: El perfil '{profile_name}' ya existe. Saltando...")
        else:
            print(f"Error al crear {profile_name}. Error: {e.stderr}", file=sys.stderr)

print(f"\n¡Listo! Se crearon (o verificaron) {num_crear} perfiles (desde 01 hasta {num_crear:02d}).")
print("Ahora puedes usar el script 'lanzar_perfiles.py'.")