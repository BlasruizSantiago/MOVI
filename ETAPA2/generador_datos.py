"""
Módulo para generar datos aleatorios de pasajeros y viajes
Cumple con: random, listas, strings, archivos CSV
"""

from random import randint
from datetime import datetime, timedelta


def generar_ids_pasajeros(cantidad):
    """Genera una lista de IDs únicos de pasajeros usando list comprehension"""
    return [f"P{str(i).zfill(4)}" for i in range(1, cantidad + 1)]


def generar_nombres_aleatorios(cantidad):
    """Genera nombres aleatorios para pasajeros"""
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Laura", "Pedro", "Sofia", 
               "Diego", "Carmen", "Roberto", "Elena", "Miguel", "Patricia", "Jorge"]
    apellidos = ["García", "Rodríguez", "González", "Fernández", "López", "Martínez",
                 "Sánchez", "Pérez", "Gómez", "Martín", "Ruiz", "Díaz", "Torres"]
    
    # Usar lambda para combinar nombres y apellidos
    generar_nombre = lambda: f"{nombres[randint(0, len(nombres)-1)]} {apellidos[randint(0, len(apellidos)-1)]}"
    
    return [generar_nombre() for _ in range(cantidad)]


def generar_fechas_aleatorias(cantidad, dias_atras=30):
    """Genera fechas aleatorias en los últimos N días"""
    fechas = []
    hoy = datetime.now()
    
    for _ in range(cantidad):
        dias_random = randint(0, dias_atras)
        fecha = hoy - timedelta(days=dias_random)
        fechas.append(fecha.strftime("%Y-%m-%d"))
    
    return fechas


def generar_archivo_pasajeros():
    """Genera archivo CSV con datos de pasajeros (Archivo 1 de entrada)"""
    cantidad_pasajeros = randint(50, 100)
    ids = generar_ids_pasajeros(cantidad_pasajeros)
    nombres = generar_nombres_aleatorios(cantidad_pasajeros)
    
    # Edades aleatorias entre 18 y 70
    edades = [randint(18, 70) for _ in range(cantidad_pasajeros)]
    
    pf = open("datos_generados/pasajeros.csv", "w")
    pf.write("id_pasajero,nombre,edad\n")
    
    for i in range(cantidad_pasajeros):
        pf.write(f"{ids[i]},{nombres[i]},{edades[i]}\n")
    
    pf.close()
    print(f"✓ Archivo 'pasajeros.csv' generado con {cantidad_pasajeros} registros")


def generar_archivo_viajes():
    """Genera archivo CSV con viajes aleatorios (Archivo 2 de entrada)
    Usa códigos: 1=colectivo, 2=tren, 3=subte
    """
    try:
        # Leer IDs de pasajeros existentes
        pf = open("datos_generados/pasajeros.csv", "r")
        lineas = pf.readlines()[1:]  # Saltar encabezado
        pf.close()
        
        ids_pasajeros = [linea.split(",")[0] for linea in lineas]
    except FileNotFoundError:
        print("Error: Primero debe generar el archivo de pasajeros")
        return
    
    cantidad_viajes = randint(200, 500)
    codigos_transporte = [1, 2, 3]  # 1=colectivo, 2=tren, 3=subte
    
    # Rangos de precios por código de transporte
    precios = {
        1: (150, 300),  # colectivo
        2: (100, 250),  # tren
        3: (120, 280)   # subte
    }
    
    pf = open("datos_generados/viajes.csv", "w")
    pf.write("id_pasajero,codigo_transporte,gasto,fecha\n")
    
    fechas = generar_fechas_aleatorias(cantidad_viajes)
    
    for i in range(cantidad_viajes):
        id_pasajero = ids_pasajeros[randint(0, len(ids_pasajeros)-1)]
        codigo_transporte = codigos_transporte[randint(0, len(codigos_transporte)-1)]
        min_precio, max_precio = precios[codigo_transporte]
        gasto = randint(min_precio * 100, max_precio * 100) / 100.0
        
        pf.write(f"{id_pasajero},{codigo_transporte},{gasto},{fechas[i]}\n")
    
    pf.close()
    print(f"✓ Archivo 'viajes.csv' generado con {cantidad_viajes} registros")


def generar_archivo_tarifas():
    """Genera archivo CSV con tarifas por tipo de transporte (Archivo 3 de entrada)
    Códigos de transporte: 1=colectivo, 2=tren, 3=subte
    Códigos de segmento: 1=<18, 2=18-64, 3=>=65
    """
    # Tarifas fijas por tipo de transporte y segmento de edad
    # Estructura: codigo_transporte, codigo_segmento, tarifa
    tarifas = [
        # Colectivo (código 1)
        (1, 1, 150.00),  # menores
        (1, 2, 250.00),  # adultos
        (1, 3, 125.00),  # adultos mayores
        # Tren (código 2)
        (2, 1, 120.00),  # menores
        (2, 2, 200.00),  # adultos
        (2, 3, 100.00),  # adultos mayores
        # Subte (código 3)
        (3, 1, 140.00),  # menores
        (3, 2, 230.00),  # adultos
        (3, 3, 115.00)   # adultos mayores
    ]
    
    pf = open("datos_generados/tarifas.csv", "w")
    pf.write("codigo_transporte,codigo_segmento,tarifa\n")
    
    for codigo_trans, codigo_seg, tarifa in tarifas:
        pf.write(f"{codigo_trans},{codigo_seg},{tarifa:.2f}\n")
    
    pf.close()
    print(f"✓ Archivo 'tarifas.csv' generado con {len(tarifas)} tarifas (3 tipos × 3 segmentos)")


def generar_archivos_aleatorios():
    """Función principal que genera los 3 archivos de entrada requeridos"""
    try:
        print("\n=== GENERANDO ARCHIVOS ALEATORIOS ===")
        generar_archivo_pasajeros()
        generar_archivo_viajes()
        generar_archivo_tarifas()
        print("\n✓ Todos los archivos fueron generados exitosamente\n")
    except Exception as e:
        print(f"Error al generar archivos: {e}")


if __name__ == "__main__":
    generar_archivos_aleatorios()
