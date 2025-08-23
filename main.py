# Listas con DNI, nombre de usuario y contraseña de los usuarios ya existentes en el sistema
# Migrar a un JSON.

import random # Importa la librería random para generar números aleatorios
import time # Importa la librería time para usar la función sleep

def main():
    time.sleep(0.75)
    Pboleto = [60, 120, 250] # Precios de los boletos (Colectivo, Tren, Subte)
    usrActivos = ["Pedro pascal", "John Doe", "Brad Pitt"] # Carga de lista de usuarios activos
    mTren = crearMatriz(usrActivos, Pboleto[0]) # Crea una matriz con los usuarios activos y el total gastodo por cada uno en Colectivos a lo largo del mes.
    mSubte = crearMatriz(usrActivos, Pboleto[1]) # Crea una matriz con los usuarios activos y el total gastado por cada uno en Trenes a lo largo del mes.
    mColectivo = crearMatriz(usrActivos, Pboleto[2]) # Crea una matriz con los usuarios activos y el total gastado por cada uno en Subtes a lo largo del mes.
    mTransporte = [mColectivo, mTren, mSubte] # Lista que contiene las 3 matrices creadas
    print("\n-------------------\n\nMenú Principal: \n  1. Registrar un nuevo usuario \n  2. Mostrar Usuarios existentes \n  3. Mostrar Matrices Creadas \n  0. Salir del sistema \n\n-------------------\n")
    time.sleep(0.75)
    res = int(input("Ingrese una opción: "))
    if(res == 1):
        print("\nFunción de registro de nuevos usuarios deshabilitada temporalmente.")
        time.sleep(1)
        print("\nVolviendo al inicio...")
        time.sleep(1)
        # Register(usrActivos) # FUNCION NO VALIDA, YA QUE SE REQUIERE DE VARIABLES GLOBALES PARA SU FUNCIONAMIENTO. 
                               # Hay que guardar el estado en variables que se pasen entre llamadas a la función
    elif(res == 2):
        mostrarUsuarios(usrActivos) # Muestra la lista de usuarios activos
    elif(res == 3):
        mostrarMatriz(mTransporte, usrActivos) # Muestra la matriz creada con los usuarios activos y el total de lo gastado por cada uno a lo largo del mes.
        menuEstadisticas(mTransporte, usrActivos) # Muestra el menú de estadísticas
    main() # Vuelve al inicio del programa


def Register(usrActivos):
    print("\nRegistro de nuevo usuario")
    time.sleep(0.5)
    usr = input("Ingrese nombre completo del nuevo usuario: ")
    if(existeUsr(usr, usrActivos) == False): # Comprueba si el usuario ya existe en la lista de usuarios activos
        usrActivos.append(usr) # Agrega el nuevo usuario a la lista de usuarios activos
        print(f"\nUsuario {usr} registrado con éxito!")
    else:
        print(f"\nEl usuario {usr} ya existe en el sistema.")

# Función que comprueba la existencia del usuario en las listas creadas. 
def existeUsr(usr, usrActivos):
    res = False
    i = 0
    while (i+1 <= int(len(usrActivos))):
        if(usr == usrActivos[i]):
            res = True
        i += 1
    return res # Si la respuesta es True, el usuario existe en el sistema. Por el contrario, si devuelve false este no existe.

# Procedimiento que muestra la lista de usuarios activos en el sistema
def mostrarUsuarios(usrActivos):
    print("\nUsuarios activos en el sistema:\n")
    time.sleep(0.5)
    for i in range(len(usrActivos)):
        print(f"{i+1}. {usrActivos[i]}")
        time.sleep(0.5) # Pausa de 0.25 segundos entre cada usuario mostrado
    print("")

# Función que crea y devuelve una Matriz armada con paarametros asignados
def crearMatriz(usrActivos, Pboleto):
    filas = len(usrActivos)
    columnas = 30 # Días del mes 
    matriz = []
    for h in range(3): # Crear 3 matrices, una por cada tipo de boleto (Tren, Subte, Colectivo)
        for i in range(filas): # Crea una fila por cada usuario activo
            fila = []
            for j in range(columnas): # Crea una columna por cada día del mes
                if (random.randint(0, 10) > 3): # Probabilidad de que el usuario use o no el servicio de transporte  ese día
                    num = random.randint(1, 15) # Cantidad de viajes realizados ese día
                    fila.append(num * Pboleto)
                else:
                    fila.append(0)
            matriz.append(fila)
    return matriz

# Procedimiento que muestra la matriz creada
def mostrarMatriz(mTransporte, usrActivos):
    for h in range(3): # Mostrar las 3 matrices, una por cada tipo de boleto (Colectivo, Tren, Subte)
        print("\n-------------------\n")
        print(f"Datos de ingresos en {'Colectivo' if h==0 else 'Tren' if h==1 else 'Subte'}:") # Título dinámico según la matriz que se esté mostrando
        time.sleep(0.5)
        for i in range(len(usrActivos)):
            print(f"\nUsuario: {usrActivos[i]}")
            time.sleep(0.5)
            k = 1
            for j in range(len(mTransporte[h][i])): # Recorre las columnas de la matriz
                print(f"día {k}: ${mTransporte[h][i][j]}", end=" | ")
                k += 1
            print("")
            time.sleep(0.5)

def menuEstadisticas(mTransporte, usrActivos):
    print(f"-------------------\n\nDatos de transporte del mes: \n  1. El usuarios con más gastos \n  2. El transporte más y el menos utilizado. \n  3. El promedio general de lo gastado por los pasajeros. \n  4. El gasto total de todos los pasajeros. \n  5. El monto recibido de los 3 beneficiarios. \n  0. Volver al inicio \n\n-------------------\n")
    res = int(input("Ingrese una opción: "))
    while(res > 0 or res <= 5):
        if (res == 1): 
            usuarioMasGasto(mTransporte, usrActivos)
            print(f"\nEl usuario que más gastó en el mes fue {usuarioMasGasto(mTransporte, usrActivos)[0]} con un total de ${usuarioMasGasto(mTransporte, usrActivos)[1]}\n")
        elif(res == 2):
            transporteMasMenosUtilizado(mTransporte)
            print(f"\nEl transporte más utilizado fue el {transporteMasMenosUtilizado(mTransporte)[0]} y el menos utilizado fue el {transporteMasMenosUtilizado(mTransporte)[1]}\n")
        elif(res == 3):
            print(f"\nEl promedio general de lo gastado por los pasajeros es de: ${promedioGasto(mTransporte, usrActivos):.2f}\n")
        elif(res == 4):
            print(f"\nEl gasto total de todos los pasajeros es de: ${gastoTotal(mTransporte)}\n")
        elif(res == 5):
            beneficiarios = montoBeneficiarios(mTransporte)
            print("\nMontos recibidos por los beneficiarios:")
            # Crear funcion para mostrar los beneficiarios y sus montos
        elif(res == 0):
            print("\nVolviendo al inicio...")
            time.sleep(1)
        else:
            print("\nOpción inválida!")
        print(f"-------------------\n\nDatos de transporte del mes: \n  1. El usuarios con más gastos \n  2. El transporte más y el menos utilizado. \n  3. El promedio general de lo gastado por los pasajeros. \n  4. El gasto total de todos los pasajeros. \n  5. El monto recibido de los 3 beneficiarios. \n  0. Volver al inicio \n\n-------------------\n")
        res = int(input("Ingrese una opción: "))
    main() # Vuelve al inicio del programa

def usuarioMasGasto(mTransporte, usrActivos):
    gastosTotales = [0 for _ in range(len(usrActivos))] # Inicializa una lista para almacenar los gastos totales de cada usuario
    for h in range(3): # Recorre las 3 matrices (Colectivo, Tren, Subte)
        for i in range(len(usrActivos)): # Recorre cada usuario
            gastosTotales[i] += sum(mTransporte[h][i]) # Suma los gastos de cada usuario en la matriz actual
    maxGasto = max(gastosTotales) # Encuentra el gasto máximo
    usuarioMaxGasto = usrActivos[gastosTotales.index(maxGasto)] # Encuentra el usuario correspondiente al gasto máximo
    return usuarioMaxGasto, maxGasto

def transporteMasMenosUtilizado(mTransporte):
    totalViajes = [0, 0, 0] # Inicializa una lista para almacenar el total de viajes por tipo de transporte
    for h in range(3): # Recorre las 3 matrices (Colectivo, Tren, Subte)
        for i in range(len(mTransporte[h])): # Recorre cada usuario
            totalViajes[h] += sum(1 for gasto in mTransporte[h][i] if gasto > 0) # Cuenta los días con gastos (viajes realizados)
    transporteMasUtilizado = ["Colectivo", "Tren", "Subte"][totalViajes.index(max(totalViajes))] # Encuentra el transporte más utilizado
    transporteMenosUtilizado = ["Colectivo", "Tren", "Subte"][totalViajes.index(min(totalViajes))] # Encuentra el transporte menos utilizado
    return transporteMasUtilizado, transporteMenosUtilizado

def promedioGasto(mTransporte, usrActivos):
    totalGasto = 0
    totalUsuarios = len(usrActivos)
    for h in range(3): # Recorre las 3 matrices (Colectivo, Tren, Subte)
        for i in range(totalUsuarios): # Recorre cada usuario
            totalGasto += sum(mTransporte[h][i]) # Suma los gastos de cada usuario en la matriz actual
    promedio = totalGasto / totalUsuarios if totalUsuarios > 0 else 0 # Calcula el promedio de gasto por usuario
    return promedio

def gastoTotal(mTransporte):
    totalGasto = 0
    for h in range(3): # Recorre las 3 matrices (Colectivo, Tren, Subte)
        for i in range(len(mTransporte[h])): # Recorre cada usuario
            totalGasto += sum(mTransporte[h][i]) # Suma los gastos de cada usuario en la matriz actual
    return totalGasto

def montoBeneficiarios(mTransporte):
    totalGasto = gastoTotal(mTransporte)
    beneficiarios = {
        "Gobierno": totalGasto * 0.5,
        "Empresas de Transporte": totalGasto * 0.3,
        "Mantenimiento y Operación": totalGasto * 0.2
    }
    return beneficiarios

# Punto de entrada del programa
if __name__=="__main__":
    print("\nBienvenido a MOVI (Movilidad Optimizada Virtual e Integral)")
    main()