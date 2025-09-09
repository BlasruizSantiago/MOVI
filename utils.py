"""
Módulo de utilidades genéricas para manejo de matrices.

Incluye:
- crear_matriz: Crea una matriz de tamaño filas x columnas con un valor inicial.
"""
import random

# Función que crea y devuelve una Matriz armada con parametros asignados
def crearMatriz(usuarios, transportes, Pboleto):
    filas = len(usuarios)
    columnas = len(transportes) 
    matriz = []
    for i in range(filas): # Crea una fila por cada usuario activo
        fila = []
        for j in range(columnas): # Crea una columna por cada tipo de transporte
            if (random.randint(0, 10) > 3): # Probabilidad de que el usuario use o no el servicio de transporte ese día
                num = random.randint(1, 15) # Cantidad de viajes realizados ese día
                fila.append(num * Pboleto)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

# Procedimiento que muestra la lista de usuarios activos en el sistema
def mostrarUsuarios(usrActivos):
    print("\nUsuarios activos en el sistema:\n")
    for i in range(len(usrActivos)):
        print(f"{i+1}. {usrActivos[i]}")
    print("")

# Función que comprueba la existencia del usuario en las listas creadas. 
def existeUsr(usr, usrActivos):
    res = False
    for i in usrActivos:
        if(usr == usrActivos[i]):
            res = True
        i += 1
    return res # Si la respuesta es True, el usuario existe en el sistema. Por el contrario, si devuelve false este no existe.
