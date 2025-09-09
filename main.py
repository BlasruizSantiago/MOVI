import random
from utils import crearMatriz, mostrarUsuarios, existeUsr  # Importa las funciones del módulo

transportes = ['Colectivo', 'Tren', 'Subte']
usuarios = ["Pedro pascal", "John Doe", "Brad Pitt"]
Pboleto = [60, 120, 250]

def main():
    # mColectivo = crearMatriz(usuarios, transportes, Pboleto[0])
    # mTren = crearMatriz(usuarios, transportes, Pboleto[1])
    # mSubte = crearMatriz(usuarios, transportes, Pboleto[2])
    mTransporte = crearMatriz(usuarios, transportes, Pboleto) # Matriz usuarios x transporte
    print(mTransporte)
    opciones_validas = [0, 1, 2, 3, 4]
    res = -1  # Inicializa con un valor inválido
    while res not in opciones_validas:
        print(
            "\n" + "="*50 + "\n"
            "MENÚ PRINCIPAL\n"
            "" + "-"*50 + "\n"
            "1. Mostrar listado de usuarios\n"
            "2. Mostrar precios por transporte\n"
            "3. Análisis estadísticas\n"
            "4. Registrar nuevos usuarios\n"
            "0. Salir del sistema\n"
            "" + "="*50 + "\n"
        )
        entrada = input("Ingrese una opción: ")
        if entrada.isdigit():
            res = int(entrada)
        else:
            print("\nError: debe ingresar un número. Intente nuevamente.\n")
            res = -1
        if res not in opciones_validas and res != -1:
            print("\nError: número inválido. Intente nuevamente.\n")
    
    if res == 1:
        mostrarUsuarios(usuarios)  # Muestra la lista de usuarios activos
    elif res == 2:
        mostrarPreciosTransporte()
    elif res == 3:
        menuEstadisticas(mTransporte, usuarios)  # Muestra el menú de estadísticas
    elif res == 4:
        registrarNuevoUsuario(usuarios)  # Función para registrar nuevos usuarios
    elif res == 0:
        print("\nSaliendo del sistema...")
        return
    main() # Vuelve al inicio del programa


def Register(usrActivos):
    print("\nRegistro de nuevo usuario")
    usr = input("Ingrese nombre completo del nuevo usuario: ")
    if(existeUsr(usr, usrActivos) == False): # Comprueba si el usuario ya existe en la lista de usuarios activos
        usrActivos.append(usr) # Agrega el nuevo usuario a la lista de usuarios activos
        print(f"\nUsuario {usr} registrado con éxito!")
    else:
        print(f"\nEl usuario {usr} ya existe en el sistema.")


# Procedimiento que muestra la matriz creada
def mostrarGastosxUsuario(mTransporte, usrActivos):    
    # Imprimir encabezado
    print("\n" + "-" * 60)
    print("GASTOS POR USUARIO Y TIPO DE TRANSPORTE".center(60))
    print("-" * 60)
    
    # Imprimir encabezados de columnas
    print("USUARIO".ljust(20), end="")
    for transporte in transportes:
        print(f"| {transporte.upper().center(10)} ", end="")
    print("\n" + "-" * 60)
    
    # Imprimir filas de datos
    for i in range(len(usrActivos)):
        # Imprimir nombre de usuario
        print(usrActivos[i].ljust(20), end="")
        
        # Imprimir gastos por tipo de transporte para este usuario
        for gastado in range(len(mTransporte[0])):
            # Calcular el total gastado por este usuario en este transporte
            print(f"| ${str(gastado).rjust(10)} ", end="")
        print()  # Nueva línea para el siguiente usuario
    
    print("-" * 60 + "\n")

def mostrarPreciosTransporte():
    print("\n" + "="*60)
    print("PRECIOS POR TIPO DE TRANSPORTE".center(60))
    print("="*60)
    print(f"{'Colectivo:':<15} ${Pboleto[0]}")
    print(f"{'Tren:':<15} ${Pboleto[1]}")
    print(f"{'Subte:':<15} ${Pboleto[2]}")
    print("="*60 + "\n")

def menuEstadisticas(mTransporte, usrActivos):
    while True:
        print(
            "\n" + "="*60 + "\n"
            "ANÁLISIS ESTADÍSTICOS\n"
            "" + "-"*60 + "\n"
            "1. Mostrar usuario con más gastos\n"
            "2. Mostrar transporte más y menos utilizado\n"
            "3. Mostrar promedio general de gastos por pasajero\n"
            "4. Mostrar gasto total de todos los pasajeros\n"
            "5. Mostrar monto total redistribuido (5%)\n"
            "0. Volver al menú principal\n"
            "" + "="*60 + "\n"
        )
        entrada = input("Ingrese una opción: ")
        if entrada.isdigit():
            res = int(entrada)
            if res == 0:
                print("\nVolviendo al menú principal...")
                break
            elif res == 1:
                usuario, total = usuarioMasGasto(mTransporte, usrActivos)
                print(f"\nEl usuario que más gastó en el mes fue {usuario} con un total de ${total}\n")
            elif res == 2:
                mas_utilizado, menos_utilizado = transporteMasMenosUtilizado(mTransporte)
                print(f"\nEl transporte más utilizado fue el {mas_utilizado} y el menos utilizado fue el {menos_utilizado}\n")
            elif res == 3:
                print(f"\nEl promedio general de lo gastado por los pasajeros es de: ${promedioGasto(mTransporte, usrActivos):.2f}\n")
            elif res == 4:
                print(f"\nEl gasto total de todos los pasajeros es de: ${gastoTotal(mTransporte)}\n")
            elif res == 5:
                beneficiarios = montoBeneficiarios(mTransporte)
                print("\nMontos recibidos por los beneficiarios:")
                # Aquí se puede agregar el código para mostrar los beneficiarios y sus montos
                for benef in beneficiarios:
                    print(f"- {benef}: ${beneficiarios[benef]:.2f}")
            else:
                print("\nOpción inválida!")
        else:
            print("\nError: Por favor ingrese un número válido.")

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

print("\nBienvenido a MOVI (Movilidad Optimizada Virtual e Integral)")
main()