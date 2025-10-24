import subprocess
import os

# --- Configuración ---
# Define cuántos perfiles quieres crear
CANTIDAD_A_CREAR = 40
# ---------------------

print(f"Creando {CANTIDAD_A_CREAR} perfiles de Firefox (01, 02, ...)")

firefox_path = "/usr/bin/firefox"

if not os.path.exists(firefox_path):
    print(f"Error: No se encontró Firefox en {firefox_path}")
else:
    # El bucle ahora usa la variable
    for i in range(1, CANTIDAD_A_CREAR + 1):
        profile_name = f"{i:02d}"
        
        command = [firefox_path, '-CreateProfile', profile_name]
        
        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"Perfil '{profile_name}' creado exitosamente.")
        
        except subprocess.CalledProcessError as e:
            if "already exists" in e.stderr:
                print(f"Perfil '{profile_name}' ya existe.")
            else:
                print(f"Error creando perfil '{profile_name}': {e.stderr}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    print(f"\nCreación de {CANTIDAD_A_CREAR} perfiles completada.")