from funcModule import crearMatriz, mostrarUsuarios # Importa las funciones del módulo

TRANSPORTES = ['Colectivo', 'Tren', 'Subte']
PRECIO_BOLETO = [60, 120, 250]
usuarios = ["Pedro Pascal", "John Doe", "Brad Pitt"]

def main():
    mTransporte = crearMatriz(usuarios, TRANSPORTES, PRECIO_BOLETO) # Matriz usuarios x transporte
    opciones_validas = [0, 1, 2, 3]
    res = -1
    while res not in opciones_validas:
        print(
            "\n" + "="*50 + "\n"
            "MENÚ PRINCIPAL\n"
            "" + "-"*50 + "\n"
            "1. Mostrar listado de usuarios\n"
            "2. Mostrar precios por transporte\n"
            "3. Análisis estadísticas\n"
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
    elif res == 0:
        print("\nSaliendo del sistema...")
        return
    main() # Vuelve al inicio del programa

# Procedimiento que muestra la matriz creada
def mostrarGastosxUsuario(mTransporte, usrActivos):
    # Imprimir encabezado
    print("\n" + "-" * 60)
    print("GASTOS POR USUARIO Y TIPO DE TRANSPORTE".center(60))
    print("-" * 60)
    
    # Imprimir encabezados de columnas
    print("USUARIO".ljust(20), end="")
    for transporte in TRANSPORTES:
        print(f"| {transporte.upper().center(10)} ", end="")
    print("\n" + "-" * 60)
    
    # Imprimir filas de datos
    for i in range(len(usrActivos)):
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
    print(f"{'Colectivo:':<15} ${PRECIO_BOLETO[0]}")
    print(f"{'Tren:':<15} ${PRECIO_BOLETO[1]}")
    print(f"{'Subte:':<15} ${PRECIO_BOLETO[2]}")
    print("="*60 + "\n")

def menuEstadisticas(mTransporte, usuarios):
    estadisticas = True
    while estadisticas == True:
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
                estadisticas = False
            elif res == 1:
                usuario, total = usuarioMasGasto(mTransporte, usuarios)
                print(f"\nEl usuario que más gastó en el mes fue {usuario} con un total de ${total}\n")
            elif res == 2:
                mas_utilizado, menos_utilizado = transporteMasMenosUtilizado(mTransporte)
                print(f"\nEl transporte más utilizado fue el {mas_utilizado} y el menos utilizado fue el {menos_utilizado}\n")
            elif res == 3:
                print(f"\nEl promedio general de lo gastado por los pasajeros es de: ${promedioGasto(mTransporte, usuarios):.2f}\n")
            elif res == 4:
                print(f"\nEl gasto total de todos los pasajeros es de: ${gastoTotal(mTransporte)}\n")
            elif res == 5:
                beneficiarios, monto = montoBeneficiarios(mTransporte, usuarios)
                print("\nMontos recibidos por los beneficiarios:")
                for benef in beneficiarios:
                    print(f"- {benef}: ${monto}")
            else:
                print("\nOpción inválida!")
        else:
            print("\nError: Por favor ingrese un número válido.")

def usuarioMasGasto(mTransporte, usrActivos):
    gastosTotales = [sum(mTransporte[i]) for i in range(len(usrActivos))]
    maxGasto = max(gastosTotales)
    usuarioMaxGasto = usrActivos[gastosTotales.index(maxGasto)] # Encuentra el usuario correspondiente al gasto máximo
    return usuarioMaxGasto, maxGasto

def transporteMasMenosUtilizado(mTransporte):
    totalViajesPorTransporte = [0, 0, 0]
    for h in range(len(mTransporte)):
        for i in range(3):
            # Calcula la cantidad de viajes como monto gastado / precio del boleto
            viajes = mTransporte[h][i] // PRECIO_BOLETO[i]
            totalViajesPorTransporte[i] += viajes
    transporteMasUtilizado = TRANSPORTES[totalViajesPorTransporte.index(max(totalViajesPorTransporte))]
    transporteMenosUtilizado = TRANSPORTES[totalViajesPorTransporte.index(min(totalViajesPorTransporte))]
    return transporteMasUtilizado, transporteMenosUtilizado

def promedioGasto(mTransporte, usrActivos):
    totalGasto = 0
    totalUsuarios = len(usrActivos)
    for h in range(totalUsuarios):
        for i in range(3):
            totalGasto += mTransporte[i][h] # Suma los gastos de cada usuario en la matriz actual
    promedio = totalGasto / totalUsuarios if totalUsuarios > 0 else 0 # Calcula el promedio de gasto por usuario
    return promedio

def gastoTotal(mTransporte):
    totalGasto = 0
    for fila in mTransporte:
        for gasto in fila:
            totalGasto += gasto
    return totalGasto

def topUsuariosMasGasto(mTransporte, usrActivos, podio=3):
    gastosTotales = [sum(mTransporte[i]) for i in range(len(usrActivos))]
    # Selecciona los top_n usuarios con más gasto usando solo estructuras básicas
    top_usuarios = []
    gastos_copia = gastosTotales[:]
    max_iter = min(podio, len(usrActivos))  # Asegura no exceder la cantidad de usuarios
    for _ in range(max_iter):
        max_gasto = max(gastos_copia)
        idx = gastos_copia.index(max_gasto)
        top_usuarios.append(usrActivos[idx])
        gastos_copia[idx] = float('-inf')  # Evita volver a elegir el mismo usuario
    return top_usuarios

def montoBeneficiarios(mTransporte, usrActivos):
    montoRedistribucion = gastoTotal(mTransporte) * 0.05  # 5% del total
    top3 = topUsuariosMasGasto(mTransporte, usrActivos, 3)
    montoPorBeneficiario = montoRedistribucion / 3
    return top3, montoPorBeneficiario

print("\nBienvenido a MOVI (Movilidad Optimizada Virtual e Integral)")
main()