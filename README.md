🚀 Guía Maestra: Automatización con Cron y Diagnóstico de Sistemas (Caso Autopsia)
Este repositorio ha sido diseñado para enseñar cómo programar tareas automáticas en Linux utilizando Cron. A diferencia de una guía convencional, aquí aplicaremos una "autopsia" técnica para entender por qué fallan los scripts cuando se automatizan y cómo solucionarlo profesionalmente.
________________________________________
📂 1. Estructura de la Investigación: Dos Proyectos
Para que el aprendizaje sea real, hemos dividido el trabajo en dos carpetas/proyectos que veréis en el repositorio:
1.	prueba_cron (El Laboratorio de Errores): * Objetivo: Experimentar con el fallo. Aquí usamos rutas relativas para demostrar cómo Cron "pierde" los archivos.
o	Resultado: El archivo no aparece en la carpeta del proyecto, sino en la carpeta raíz del usuario (/home/usuario).
2.	pildora-cron (La Solución Final):
o	Objetivo: Implementar un código robusto.
o	Resultado: Uso de rutas absolutas y gestión de logs de errores (2>&1), garantizando que el sistema sea estable y transparente.
________________________________________
🛠 2. Configuración del Entorno de Trabajo
A. Opción Preferida: Windows Subsystem for Linux (WSL)
Cron es una herramienta nativa de Linux. Si usas Windows, debes habilitar WSL:
1.	Instalación: Abre PowerShell como administrador y ejecuta: wsl --install.
2.	Reinicio: Es obligatorio reiniciar el PC para que Windows active las funciones de virtualización.
3.	Vincular carpetas: En la terminal de Ubuntu, tus archivos de Windows están en /mnt/c/. Navega a tu carpeta así:
cd /mnt/c/Documents/projects/prueba_cron
4.	VS Code: Desde esa misma terminal, escribe code . para abrir el editor vinculado al entorno Linux.
B. Opción Alternativa: WebVM.io (Sin Instalación)
Si no puedes instalar WSL, usa webvm.io, un Linux que corre en el navegador.
•	Limitación Crítica: Al ser un entorno "sandbox", no tienes permisos de administrador (sudo).
•	Comando de emergencia: Si el servicio no arranca, intenta: /etc/init.d/cron start.
•	Simulación: Para ver el efecto de las rutas, ejecuta: cd /tmp && python3 /home/user/entrenamiento_modelo.py. Verás que el archivo se crea en tmp y no en tu carpeta.
________________________________________
💻 3. Análisis Detallado del Código (entrenamiento_modelo.py)
Vamos a explicar el código de la "Solución Final". Este script simula el entrenamiento de una IA y guarda un registro del éxito.
Python
import datetime
import os

# --- PASO 1: LOCALIZACIÓN AUTOMÁTICA ---
# Cron no sabe en qué carpeta estás trabajando. 
# 'os.path.abspath(__file__)' obtiene la ruta completa de este script.
# 'os.path.dirname' nos da la carpeta que lo contiene.
ruta_del_script = os.path.dirname(os.path.abspath(__file__))

# --- PASO 2: CONSTRUCCIÓN DE LA RUTA ---
# Unimos la carpeta del script con el nombre del archivo deseado.
# Esto asegura que el log se guarde AQUÍ y no en /home/usuario.
ruta_archivo_final = os.path.join(ruta_del_script, "modelo_ia.txt")

# --- PASO 3: LÓGICA DE REGISTRO ---
# Creamos un mensaje con la fecha y hora exacta del "entrenamiento".
log_entry = f"Modelo actualizado con éxito el: {datetime.datetime.now()}\n"

# --- PASO 4: ESCRITURA SEGURA ---
# 'with open' cierra el archivo automáticamente al terminar, evitando bloqueos.
# 'a' (append) significa que añade información al final sin borrar lo anterior.
with open(ruta_archivo_final, "a") as f:
    f.write(log_entry)

print(f"ÉXITO: Archivo guardado en {ruta_archivo_final}")
________________________________________
⚙️ 4. Configuración de Cron (La "Agenda" de Linux)
Para que el script se ejecute solo, debemos configurar el archivo Crontab:
1.	Abrir el editor: Ejecuta crontab -e. (Si te pregunta, elige nano).
2.	La línea de ejecución: Ve al final del archivo y pega esto exactamente:
Bash
* * * * * /usr/bin/python3 /mnt/c/Documents/projects/prueba_cron/entrenamiento_modelo.py >> /mnt/c/Documents/projects/prueba_cron/cron.log 2>&1
3.	Desglose de la línea:
o	* * * * *: Significa "Ejecutar cada minuto, de cada hora, de cada día".
o	/usr/bin/python3: Ruta absoluta al intérprete de Python (Cron necesita saber dónde está el programa).
o	>> cron.log: Guarda el historial de lo que imprime el script.
o	2>&1: El Buzón de Errores. Envía cualquier fallo técnico al mismo archivo cron.log. Sin esto, estaríamos a ciegas.
o	⚠️ NOTA VITAL: Debes pulsar ENTER después de esta línea para dejar una línea en blanco al final del archivo. Si no lo haces, Linux ignorará la instrucción.
________________________________________
🚨 5. Comandos de Emergencia y Monitoreo
•	Ver en tiempo real: tail -f cron.log
o	Uso: Es fundamental para la presentación. Permite ver cómo aparece una línea nueva cada minuto sin tocar nada.
•	Reiniciar el motor: sudo service cron restart
o	Uso: Si tras configurar todo no pasa nada, el motor de Cron puede estar "dormido".
•	Ver historial completo: cat cron.log
•	Comprobar si Cron vive: ps aux | grep cron
________________________________________
🧹 6. Protocolo de Limpieza Final (Importante)
Al terminar la práctica, es responsabilidad del desarrollador dejar el sistema limpio:
1.	Eliminar tareas: Ejecuta crontab -r. Esto borra todas tus automatizaciones para que el PC no siga trabajando innecesariamente.
2.	Verificar: Ejecuta crontab -l. Debe salir el mensaje: no crontab for [tu_usuario].
3.	Parar motor: sudo service cron stop.
4.	Limpiar logs: Si el archivo de log es muy grande, vacíalo con > cron.log.
________________________________________
Documentación elaborada por el Equipo de Investigadores ☺


