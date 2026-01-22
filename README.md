# 🕵️‍♂️ El Misterio de la Autopsia (Automatización con Cron)

Esta guía documenta la investigación técnica sobre un script de IA que "desapareció" al ser automatizado. **Vamos a aprender** a usar el motor de Linux (Cron) para que nuestros procesos cobren vida propia.

## 📋 1. Preparación del Laboratorio (Setup)

### Paso 1: Ubicación en el sistema

Primero, **necesitamos entrar** en la carpeta donde están las pruebas. En tu terminal de Ubuntu (WSL), escribe:

```bash
cd /mnt/c/documents/projects/pildora-cron
code .

```

* **¿Qué estamos haciendo?** Viajamos a la carpeta del proyecto y abrimos VS Code. Es vital usar `/mnt/c/` para que los archivos sean visibles tanto en Windows como en Linux.

### Paso 2: Activar el motor

Cron es un "demonio" (un proceso que corre de fondo). En WSL suele estar apagado. **Vamos a encenderlo**:

```bash
sudo service cron start

```

* **¿Por qué `sudo`?** Porque estamos dando una orden al núcleo del sistema operativo.

---

## 💻 2. Fase 1: El Incidente (`demo_fallo.py`)

**Vamos a ver** qué pasa cuando un script usa **rutas relativas**.

```python
# demo_fallo.py
with open("modelo_ia.txt", "a") as f:
    f.write("Entrenamiento fantasma...")

```

### El misterio del Crontab

Programamos el fallo entrando en la "agenda" de Linux:

1. Ejecuta: `crontab -e`.
2. Añade esta línea al final:
`* * * * * /usr/bin/python3 /mnt/c/documents/projects/pildora-cron/demo_fallo.py`

**¿Qué ocurre?** Pasa el minuto... y el archivo `modelo_ia.txt` **NO** aparece en tu carpeta. Cron lo ha creado en su carpeta interna porque no le dijiste exactamente dónde guardarlo.

---

## 🩺 3. Fase 2: La Solución Profesional (`main_ia.py`)

Para que el servidor no se pierda, **tenemos que usar** rutas absolutas. **Vamos a ver** el código de `main_ia.py`:

```python
import os, datetime
# Detectamos la carpeta real del script
ruta_base = os.path.dirname(os.path.abspath(__file__))
# Creamos el camino exacto hacia el log
log_path = os.path.join(ruta_base, "logs", "ejecucion.log")

with open(log_path, "a") as f:
    f.write(f"¡Servidor vivo! - {datetime.datetime.now()}\n")

```

---

## 🚀 4. Despliegue Automatizado (`setup_cron.sh`)

Para evitar errores de escritura, **usaremos nuestro script estrella**.

**Ejecuta:** `bash setup_cron.sh`

**¿Qué hace este script?**

1. `crontab -r`: Limpia la agenda de tareas anteriores.
2. `touch .../ejecucion.log`: Asegura que el archivo de log existe.
3. `echo "... | crontab -`: Inscribe el nuevo script en la agenda automáticamente.
4. `tail -f .../ejecucion.log`: Abre un monitor en tiempo real. **¡En cuanto pase un minuto, verás la magia en tu pantalla!**

---

## 🚨 5. Caja de Herramientas (Comandos de Emergencia)

Si algo falla, **tenemos estos comandos** para arreglarlo:

* `crontab -l`: **Listar.** Mira qué tareas tienes activas ahora mismo.
* `crontab -r`: **Reset.** Borra todo si te has equivocado de ruta.
* `sudo service cron status`: **Check.** Verifica que el motor está `active`.
* `2>&1`: **Buzón de errores.** Si lo pones al final del cron, los fallos de Python se guardarán en el log para que puedas leerlos.

---

## 🧹 6. Protocolo de Limpieza

Al terminar, **debemos dejar** el sistema descansando:

```bash
crontab -r
sudo service cron stop

```

**Nota final:** El archivo `ejecucion.log` es tu prueba de éxito. Si se llena de texto, ¡has dominado el tiempo!

