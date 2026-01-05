import time
import sys

def training_demo():
    print("--- INICIANDO ENTRENAMIENTO DE MODELO IA (Purdue Exp. 1979) ---")
    tasks = ["Cargando datasets", "Optimizando neuronas", "Calculando pesos", "Guardando checkpoint"]
    
    for task in tasks:
        print(f"{task}...", end="", flush=True)
        for _ in range(10):
            time.sleep(0.2)
            print(".", end="", flush=True)
        print(" ¡OK!")
    
    print("--- ENTRENAMIENTO COMPLETADO CON ÉXITO ---")

if __name__ == "__main__":
    training_demo()