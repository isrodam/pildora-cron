import os
import datetime

# Usamos rutas absolutas para que Cron no se pierda
ruta_directorio = os.path.dirname(os.path.abspath(__file__))
ruta_log = os.path.join(ruta_directorio, "logs", "cron_registro.log")

def entrenar_modelo():
    ahora = datetime.datetime.now()
    with open(ruta_log, "a") as f:
        f.write(f"IA Reentrenada con éxito - Timestamp: {ahora}\n")
    print("Proceso completado.")

if __name__ == "__main__":
    entrenar_modelo()