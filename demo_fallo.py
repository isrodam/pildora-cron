import datetime

# Este script fallará en Cron porque no sabe dónde guardar el archivo
with open("error_cron.txt", "a") as f:
    f.write(f"Intento de ejecución: {datetime.datetime.now()}\n")