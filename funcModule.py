"""
Módulo de utilidades genéricas para manejo de matrices.

Incluye:
- crearMatriz: Crea una matriz de tamaño filas x columnas con un valor inicial.
- mostrarUsuarios: Lista los usuarios activos en el sistema
"""
import random

def crearMatriz(usuarios, transportes, Pboleto):
    matriz = []
    for i in range(len(usuarios)):
        fila = []
        for j in range(len(transportes)):
            if (random.randint(0, 10) > 3): # Probabilidad de que el usuario use o no el servicio de transporte
                viajes = random.randint(1, 15)
                fila.append(viajes * Pboleto[j])
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

def mostrarUsuarios(usuarios):
    print("\nUsuarios activos en el sistema:\n")
    for i in range(len(usuarios)):
        print(f"{i+1}. {usuarios[i]}")
    print("")
