# 💊 Píldora: Automatización de IA con Cronjob
**Inspiración:** El Experimento de Purdue (1979)

## 🎯 Objetivo de la Sesión
Aprender a delegar tareas repetitivas de IA (entrenamiento, limpieza de datos) al sistema operativo de forma segura y profesional.

## 📁 Estructura del Repositorio
- `main_entrenamiento.py`: Versión final con rutas absolutas.
- `demo_fallo.py`: Script para demostrar errores de entorno en Cron.
- `logs/`: Carpeta destinada a los registros de actividad.

## 🛠️ Configuración Recomendada
Para programar el entrenamiento diario a las 03:00 AM:
```bash
0 3 * * * /ruta/a/tu/venv/bin/python /ruta/a/Pildora-Cron-IA/main_entrenamiento.py >> /ruta/a/Pildora-Cron-IA/logs/cron_registro.log 2>&1