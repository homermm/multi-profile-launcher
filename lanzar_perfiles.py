import subprocess
import os
import time

# --- Configuración ---
# Define cuántas instancias quieres lanzar
CANTIDAD_A_LANZAR = 40 

# URL de ejemplo para demostración
url_generica = "https://bocasocios.bocajuniors.com.ar/home"

# Ruta al ejecutable de Firefox en Fedora
firefox_path = "/usr/bin/firefox"
# ---------------------

if not os.path.exists(firefox_path):
    print(f"Error: No se encontró Firefox en {firefox_path}")
else:
    print(f"Lanzando {CANTIDAD_A_LANZAR} instancias de Firefox hacia: {url_generica}")

    # El bucle ahora usa la variable
    for i in range(1, CANTIDAD_A_LANZAR + 1):
        profile_name = f"{i:02d}"
        
        command = [firefox_path, '--new-instance', '-P', profile_name, url_generica]
        
        try:
            subprocess.Popen(command)
            print(f"Lanzando perfil '{profile_name}'...")
            
            # (Opcional) Pausa para no saturar el sistema
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error al lanzar el perfil '{profile_name}': {e}")

    print(f"\nLanzamiento de {CANTIDAD_A_LANZAR} instancias completado.")