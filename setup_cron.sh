#!/bin/bash
crontab -r 2>/dev/null
echo "Instalando el Cronjob de la presentación (limpio)..."

# Aseguramos que el archivo existe para que tail no falle
touch /mnt/c/documents/projects/pildora-cron/logs/ejecucion.log

SCRIPT_PATH="/mnt/c/documents/projects/pildora-cron/main_ia.py"
echo "* * * * * /usr/bin/python3 $SCRIPT_PATH" | crontab -

echo "Cronjob configurado. Esperando al siguiente minuto..."
tail -f /mnt/c/documents/projects/pildora-cron/logs/ejecucion.log