"""
Módulo de estadísticas con funciones recursivas y lambdas
Cumple con: recursividad, funciones lambda, listas por comprensión
"""


def sumar_lista_recursiva(lista, indice=0):
    """
    Suma los elementos de una lista de forma recursiva
    Cumple con: RECURSIVIDAD obligatoria
    """
    if indice >= len(lista):
        return 0
    return lista[indice] + sumar_lista_recursiva(lista, indice + 1)


def contar_elementos_recursivo(lista, elemento, indice=0):
    """Cuenta cuántas veces aparece un elemento en una lista (recursivo)"""
    if indice >= len(lista):
        return 0
    
    contador = 1 if lista[indice] == elemento else 0
    return contador + contar_elementos_recursivo(lista, elemento, indice + 1)


def maximo_recursivo(lista, indice=0, max_actual=None):
    """Encuentra el máximo de una lista de forma recursiva"""
    if indice >= len(lista):
        return max_actual
    
    if max_actual is None or lista[indice] > max_actual:
        max_actual = lista[indice]
    
    return maximo_recursivo(lista, indice + 1, max_actual)


def minimo_recursivo(lista, indice=0, min_actual=None):
    """Encuentra el mínimo de una lista de forma recursiva"""
    if indice >= len(lista):
        return min_actual
    
    if min_actual is None or lista[indice] < min_actual:
        min_actual = lista[indice]
    
    return minimo_recursivo(lista, indice + 1, min_actual)


def calcular_promedio(lista):
    """Calcula el promedio de una lista usando función recursiva"""
    if not lista:
        return 0
    
    total = sumar_lista_recursiva(lista)
    return total / len(lista)


def filtrar_por_transporte(viajes, codigo_transporte):
    """
    Filtra viajes por código de transporte usando lambda
    Cumple con: FUNCIONES LAMBDA obligatorias
    Códigos: 1=colectivo, 2=tren, 3=subte
    """
    # Lambda para verificar si el viaje es del código especificado
    es_del_codigo = lambda viaje: viaje["codigo_transporte"] == codigo_transporte
    return list(filter(es_del_codigo, viajes))


def obtener_gastos(viajes):
    """Extrae solo los gastos de una lista de viajes usando lambda"""
    # Lambda para extraer el campo 'gasto'
    obtener_gasto = lambda viaje: viaje["gasto"]
    return list(map(obtener_gasto, viajes))


def calcular_estadisticas_transporte(viajes):
    """
    Calcula estadísticas por código de transporte
    Retorna un diccionario con las estadísticas
    Códigos: 1=colectivo, 2=tren, 3=subte
    """
    codigos = [1, 2, 3]  # 1=colectivo, 2=tren, 3=subte
    estadisticas = {}
    
    for codigo in codigos:
        # Filtrar viajes por código usando lambda
        viajes_codigo = filtrar_por_transporte(viajes, codigo)
        
        if viajes_codigo:
            gastos = obtener_gastos(viajes_codigo)
            
            estadisticas[codigo] = {
                "cantidad": len(viajes_codigo),
                "total": sumar_lista_recursiva(gastos),
                "promedio": calcular_promedio(gastos),
                "maximo": maximo_recursivo(gastos),
                "minimo": minimo_recursivo(gastos)
            }
        else:
            estadisticas[codigo] = {
                "cantidad": 0,
                "total": 0,
                "promedio": 0,
                "maximo": 0,
                "minimo": 0
            }
    
    return estadisticas


def agrupar_gastos_por_pasajero(viajes):
    """
    Agrupa los gastos totales por pasajero usando diccionarios
    Cumple con: DICCIONARIOS obligatorios
    """
    gastos_por_pasajero = {}
    
    for viaje in viajes:
        id_pasajero = viaje["id_pasajero"]
        gasto = viaje["gasto"]
        
        if id_pasajero in gastos_por_pasajero:
            gastos_por_pasajero[id_pasajero] += gasto
        else:
            gastos_por_pasajero[id_pasajero] = gasto
    
    return gastos_por_pasajero


def encontrar_pasajero_mayor_gasto(gastos_por_pasajero):
    """
    Encuentra el pasajero con mayor gasto usando lambda
    Retorna tupla (id_pasajero, gasto_total)
    """
    if not gastos_por_pasajero:
        return None, 0
    
    # Lambda para obtener el valor (gasto) de cada item
    obtener_gasto = lambda item: item[1]
    
    # Convertir diccionario a lista de tuplas y encontrar el máximo
    items = list(gastos_por_pasajero.items())
    pasajero_max = max(items, key=obtener_gasto)
    
    return pasajero_max


def calcular_porcentajes_transporte(viajes):
    """
    Calcula el porcentaje de uso de cada código de transporte
    Códigos: 1=colectivo, 2=tren, 3=subte
    """
    total_viajes = len(viajes)
    
    if total_viajes == 0:
        return {}
    
    codigos = [1, 2, 3]  # 1=colectivo, 2=tren, 3=subte
    porcentajes = {}
    
    for codigo in codigos:
        cantidad = contar_elementos_recursivo(
            [v["codigo_transporte"] for v in viajes], 
            codigo
        )
        porcentajes[codigo] = round((cantidad / total_viajes) * 100, 2)
    
    return porcentajes


def ordenar_por_gasto_recursivo(lista_tuplas, indice=0):
    """
    Ordena una lista de tuplas (pasajero, gasto) por gasto usando recursión
    Implementación de bubble sort recursivo
    """
    if indice >= len(lista_tuplas) - 1:
        return lista_tuplas
    
    # Una pasada del bubble sort
    for i in range(len(lista_tuplas) - 1 - indice):
        if lista_tuplas[i][1] < lista_tuplas[i + 1][1]:
            # Intercambiar
            lista_tuplas[i], lista_tuplas[i + 1] = lista_tuplas[i + 1], lista_tuplas[i]
    
    return ordenar_por_gasto_recursivo(lista_tuplas, indice + 1)


def obtener_top_n_pasajeros(gastos_por_pasajero, n=10):
    """
    Obtiene los N pasajeros con mayor gasto
    Usa slicing para obtener solo los primeros N
    Cumple con: SLICING obligatorio
    """
    lista_tuplas = list(gastos_por_pasajero.items())
    lista_ordenada = ordenar_por_gasto_recursivo(lista_tuplas)
    
    # Slicing para obtener solo los primeros N
    return lista_ordenada[:n]


def generar_resumen_estadistico(viajes, gastos_por_pasajero):
    """
    Genera un diccionario con resumen completo de estadísticas
    """
    total_viajes = len(viajes)
    todos_gastos = obtener_gastos(viajes)
    
    resumen = {
        "total_viajes": total_viajes,
        "total_recaudado": sumar_lista_recursiva(todos_gastos),
        "promedio_general": calcular_promedio(todos_gastos),
        "gasto_maximo": maximo_recursivo(todos_gastos) if todos_gastos else 0,
        "gasto_minimo": minimo_recursivo(todos_gastos) if todos_gastos else 0,
        "total_pasajeros": len(gastos_por_pasajero),
        "porcentajes_transporte": calcular_porcentajes_transporte(viajes),
        "estadisticas_por_transporte": calcular_estadisticas_transporte(viajes)
    }
    
    return resumen
