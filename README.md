🚀 Guia: Automatización con Cron y Resolución de Conflictos (Caso Autopsia)
Esta guía documenta el flujo de trabajo para automatizar procesos mediante Cron en entornos Linux. No es solo un manual de uso, sino una investigación sobre por qué los scripts suelen "desaparecer" en producción y cómo solucionarlo profesionalmente.
📋 1. Estructura de la Práctica: Dos Escenarios
Para entender el sistema, hemos diferenciado dos proyectos en este repositorio:
•	Proyecto prueba_cron (El Laboratorio): Donde reproducimos el fallo de rutas relativas y el archivo "fantasma".
•	Proyecto pildora-cron (La Solución): Donde aplicamos la lógica de rutas absolutas dinámicas y gestión de errores avanzada.
________________________________________
🛠 2. Preparación del Entorno (WSL y WebVM)
Opción A: Windows Subsystem for Linux (WSL)
1.	Instalación: Abre PowerShell (Administrador) y ejecuta: wsl --install. Es obligatorio reiniciar el ordenador.
2.	Ruta de trabajo: En la terminal de Ubuntu, tus archivos de Windows se encuentran en el punto de montaje /mnt/c/. Navega a tu carpeta de proyecto:
cd /mnt/c/Documents/projects/prueba_cron        <- es un ejemplo de ruta
3.	VS Code: Desde la terminal, escribe code . para abrir el editor con el kernel de Linux activo.
4.	Servicio: Cron no siempre arranca solo en WSL. Actívalo con: sudo service cron start.
Opción B: Alternativa Web (WebVM.io)
Si no puedes instalar WSL, usa webvm.io, un Linux virtual en el navegador.
•	Comando de inicio: Si service cron start falla, usa: /etc/init.d/cron start.
•	Simulación de error: Ejecuta cd /tmp && python3 /home/user/entrenamiento_modelo.py para ver cómo el archivo se crea en la carpeta temporal y no en la tuya.
________________________________________
💻 3. Análisis del Código: Entrenamiento de IA
Fase 1: El Script con "Trampa" (entrenamiento_modelo.py)
Este script falla al automatizarse porque confía en la ubicación del usuario:
Python
# --- ERROR DE RUTAS RELATIVAS ---
# Al automatizar con Cron, este script se ejecuta desde /home/usuario.
# El archivo 'modelo_ia.txt' NO se creará en esta carpeta, se irá al Home.
with open("modelo_ia.txt", "a") as f:
    f.write(log_entry)
Fase 2: El Script Corregido (entrenamiento_modelo_ok.py)
Utilizamos la librería os para obligar a Python a encontrar siempre la carpeta correcta:
Python
import os
import datetime

# --- SOLUCIÓN PROFESIONAL ---
# 1. Averiguamos la carpeta donde está este script automáticamente
ruta_del_script = os.path.dirname(os.path.abspath(__file__))

# 2. Creamos la ruta completa pegando la carpeta con el nombre del archivo
ruta_archivo_final = os.path.join(ruta_del_script, "modelo_ia.txt")

# 3. Registro del entrenamiento con marca de tiempo
log_entry = f"Modelo actualizado con éxito el: {datetime.datetime.now()}\n"

with open(ruta_archivo_final, "a") as f:
    f.write(log_entry)

print(f"ÉXITO: Guardado en {ruta_archivo_final}")
________________________________________
⚙️ 4. Configuración de la Tarea (Crontab)
Para programar la ejecución cada minuto:
1.	Ejecuta el comando: crontab -e.
2.	Si te pide elegir editor, selecciona Nano (el más sencillo).
3.	Pega esta línea al final del archivo (ajusta tu ruta de usuario):
* * * * * /usr/bin/python3 /mnt/c/Documents/projects/prueba_cron/entrenamiento_modelo_ok.py >> /mnt/c/Documents/projects/prueba_cron/cron.log 2>&1
¿Qué significa 2>&1?
Es fundamental para la "autopsia". Redirige los errores de Python al archivo cron.log. Si el script tiene un fallo de sintaxis, lo verás escrito ahí. Sin esto, el error desaparece.
________________________________________
🚨 5. Comandos de Emergencia y Monitoreo
•	Ver en tiempo real: tail -f cron.log (Úsalo en la demo para ver cómo aparece una línea nueva cada minuto).
•	Ver historial completo: cat cron.log.
•	Reiniciar motor: sudo service cron restart.
•	¿Está vivo?: ps aux | grep cron.
________________________________________
🧹 6. Protocolo de Limpieza Final (Obligatorio)
Para evitar que el sistema siga trabajando en segundo plano y consuma recursos innecesarios:
1.	Borrar tareas: crontab -r.
2.	Verificar: crontab -l (Debe decir "no crontab for user").
3.	Parar servicio: sudo service cron stop.
4.	Vaciar historial: > cron.log.
________________________________________
Documentación elaborada por el Equipo de Investigadores ☺
________________________________________
