#!/usr/bin/env python3
import shutil
import os
import sys
import json
import time

# --- Cerrar Brave si está abierto ---
print("Cerrando Brave...")
os.system("taskkill /F /IM brave.exe 2>nul")
time.sleep(1)  # Esperar a que se cierre

# --- Ruta a los perfiles de Brave ---
brave_profiles_path = os.path.expandvars(r"%APPDATA%\..\Local\BraveSoftware\Brave-Browser\User Data")

# Verificar que la ruta existe
if not os.path.exists(brave_profiles_path):
    print(f"Error: No se encontró la carpeta de perfiles de Brave en:", file=sys.stderr)
    print(f"{brave_profiles_path}", file=sys.stderr)
    sys.exit(1)

print(f"Carpeta de perfiles: {brave_profiles_path}\n")

# Listar carpetas de perfiles
perfiles = [d for d in os.listdir(brave_profiles_path) 
            if os.path.isdir(os.path.join(brave_profiles_path, d)) and d.startswith("Profile")]

if not perfiles:
    print("No hay perfiles para borrar (solo existe el perfil 'Default').")
    sys.exit(0)

print(f"Se encontraron {len(perfiles)} perfil(es) a borrar:")
for perfil in sorted(perfiles):
    ruta_perfil = os.path.join(brave_profiles_path, perfil)
    tamaño = sum(f.stat().st_size for f in os.scandir(ruta_perfil) 
                 if f.is_file()) / (1024 * 1024)  # Convertir a MB
    print(f"  - {perfil} (~{tamaño:.2f} MB)")

# Confirmar antes de borrar
print("\n¿Deseas borrar estos perfiles? (s/n): ", end="")
respuesta = input().strip().lower()

if respuesta != 's':
    print("Operación cancelada.")
    sys.exit(0)

# Borrar los perfiles
print("\nBorrando perfiles...")
for perfil in perfiles:
    ruta_perfil = os.path.join(brave_profiles_path, perfil)
    try:
        shutil.rmtree(ruta_perfil)
        print(f"✓ Borrado: {perfil}")
    except Exception as e:
        print(f"✗ Error al borrar {perfil}: {e}", file=sys.stderr)

# --- Limpiar el archivo de preferencias (Local State) ---
print("\nLimpiando metadatos de perfiles...")
local_state_path = os.path.join(brave_profiles_path, "Local State")

if os.path.exists(local_state_path):
    try:
        with open(local_state_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Eliminar información de perfiles en la configuración
        if "profile" in data:
            if "info_cache" in data["profile"]:
                # Guardar solo el Default
                new_info_cache = {}
                for key, value in data["profile"]["info_cache"].items():
                    if key == "Default":
                        new_info_cache[key] = value
                data["profile"]["info_cache"] = new_info_cache
                print(f"✓ Limpiado: Referencia de perfiles en Local State")
        
        # Guardar el archivo actualizado
        with open(local_state_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    except Exception as e:
        print(f"✗ Error al limpiar Local State: {e}", file=sys.stderr)

print("\n¡Limpieza completada! Los perfiles no deberían aparecer al iniciar Brave.")
