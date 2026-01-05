from datetime import datetime
import os

# Ruta del archivo de log (usando la ruta de Linux/WSL)
log_path = "/mnt/c/documents/projects/pildora-cron/logs/ejecucion.log"

# Crear la carpeta logs si no existe
os.makedirs(os.path.dirname(log_path), exist_ok=True)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_path, "a") as f:
    f.write(f"¡El servidor de IA está vivo! Ejecutado por Cron a las: {now}\n")

print(f"Log actualizado a las {now}")