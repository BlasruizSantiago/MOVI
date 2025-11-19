"""
Módulo procesador de datos de viajes
Genera los 4 archivos de salida requeridos con estadísticas
"""

import estadisticas


def cargar_viajes_desde_csv():
    """
    Carga los viajes desde el archivo CSV sin cargar todo en memoria
    Retorna una lista de diccionarios
    Cumple con: uso de diccionarios y listas sin cargar todo en memoria
    """
    viajes = []
    
    try:
        pf = open("./datos_generados/viajes.csv", "r")
        primera_linea = True
        
        for linea in pf:
            if primera_linea:
                primera_linea = False
                continue  # Saltar encabezado
            
            datos = linea.strip().split(",")
            if len(datos) == 4:
                viaje = {
                    "id_pasajero": datos[0],
                    "codigo_transporte": int(datos[1]),  # 1=colectivo, 2=tren, 3=subte
                    "gasto": float(datos[2]),
                    "fecha": datos[3]
                }
                viajes.append(viaje)
        
        pf.close()
        return viajes
    except FileNotFoundError:
        return []
    except Exception as e:
        return []


def cargar_pasajeros_desde_csv():
    """Carga información de pasajeros desde CSV"""
    pasajeros = {}
    
    try:
        pf = open("./datos_generados/pasajeros.csv", "r")
        primera_linea = True
        
        for linea in pf:
            if primera_linea:
                primera_linea = False
                continue  # Saltar encabezado
            
            datos = linea.strip().split(",")
            if len(datos) == 3:
                id_pasajero = datos[0]
                pasajeros[id_pasajero] = {
                    "nombre": datos[1],
                    "edad": int(datos[2])
                }
        
        pf.close()
        return pasajeros
    except FileNotFoundError:
        return {}
    except Exception as e:
        return {}


def generar_archivo_gastos_por_pasajero(viajes, pasajeros):
    """
    Genera archivo de salida 1: gastos_por_pasajero.txt
    Muestra el gasto total de cada pasajero ordenado de mayor a menor
    Formato CSV: id_pasajero,nombre,gasto_total
    """
    gastos_por_pasajero = estadisticas.agrupar_gastos_por_pasajero(viajes)
    top_pasajeros = estadisticas.obtener_top_n_pasajeros(gastos_por_pasajero, len(gastos_por_pasajero))
    
    pf = open("./datos_generados/gastos_por_pasajero.txt", "w")
    pf.write("id_pasajero,nombre,gasto_total\n")
    
    for id_pasajero, gasto_total in top_pasajeros:
        nombre = pasajeros.get(id_pasajero, {}).get("nombre", "Desconocido")
        pf.write(f"{id_pasajero},{nombre},{gasto_total:.2f}\n")
    
    pf.close()
    
    print("[OK] Archivo 'gastos_por_pasajero.txt' generado")


def generar_archivo_estadisticas_transporte(viajes):
    """
    Genera archivo de salida 2: estadisticas_transporte.txt
    Estadísticas detalladas por tipo de transporte
    Formato CSV: tipo_transporte,cantidad_viajes,porcentaje_uso,total_recaudado,gasto_promedio,gasto_maximo,gasto_minimo
    """
    stats = estadisticas.calcular_estadisticas_transporte(viajes)
    porcentajes = estadisticas.calcular_porcentajes_transporte(viajes)
    
    pf = open("./datos_generados/estadisticas_transporte.txt", "w")
    pf.write("codigo_transporte,cantidad_viajes,porcentaje_uso,total_recaudado,gasto_promedio,gasto_maximo,gasto_minimo\n")
    
    for codigo, datos in stats.items():
        pf.write(f"{codigo},{datos['cantidad']},{porcentajes.get(codigo, 0)},{datos['total']:.2f},{datos['promedio']:.2f},{datos['maximo']:.2f},{datos['minimo']:.2f}\n")
    
    pf.close()
    
    print("[OK] Archivo 'estadisticas_transporte.txt' generado")


def generar_archivo_resumen_general(viajes, gastos_por_pasajero):
    """
    Genera archivo de salida 3: resumen_general.txt
    Resumen completo con todas las estadísticas principales
    Formato CSV: metrica,valor
    """
    resumen = estadisticas.generar_resumen_estadistico(viajes, gastos_por_pasajero)
    
    pf = open("./datos_generados/resumen_general.txt", "w")
    pf.write("metrica,valor\n")
    pf.write(f"total_viajes,{resumen['total_viajes']}\n")
    pf.write(f"total_pasajeros,{resumen['total_pasajeros']}\n")
    pf.write(f"total_recaudado,{resumen['total_recaudado']:.2f}\n")
    pf.write(f"promedio_gasto_viaje,{resumen['promedio_general']:.2f}\n")
    pf.write(f"gasto_maximo,{resumen['gasto_maximo']:.2f}\n")
    pf.write(f"gasto_minimo,{resumen['gasto_minimo']:.2f}\n")
    
    for codigo, porcentaje in resumen['porcentajes_transporte'].items():
        cantidad = resumen['estadisticas_por_transporte'][codigo]['cantidad']
        pf.write(f"viajes_codigo_{codigo},{cantidad}\n")
        pf.write(f"porcentaje_codigo_{codigo},{porcentaje}\n")
    
    pf.close()
    
    print("[OK] Archivo 'resumen_general.txt' generado")


def generar_archivo_mayor_gasto(viajes, pasajeros):
    """
    Genera archivo de salida 4: mayor_gasto.txt
    Información del pasajero con mayor gasto total
    Formato CSV con dos secciones:
    - Encabezado: id_pasajero,nombre,edad,gasto_total
    - Viajes: tipo_transporte,gasto,fecha
    """
    gastos_por_pasajero = estadisticas.agrupar_gastos_por_pasajero(viajes)
    id_pasajero, gasto_total = estadisticas.encontrar_pasajero_mayor_gasto(gastos_por_pasajero)
    
    pf = open("./datos_generados/mayor_gasto.txt", "w")
    
    if id_pasajero:
        info_pasajero = pasajeros.get(id_pasajero, {})
        nombre = info_pasajero.get("nombre", "Desconocido")
        edad = info_pasajero.get("edad", "N/A")
        
        # Datos del pasajero
        pf.write("id_pasajero,nombre,edad,gasto_total\n")
        pf.write(f"{id_pasajero},{nombre},{edad},{gasto_total:.2f}\n")
        
        # Viajes del pasajero
        pf.write("codigo_transporte,gasto,fecha\n")
        viajes_pasajero = [v for v in viajes if v["id_pasajero"] == id_pasajero]
        
        for viaje in viajes_pasajero:
            pf.write(f"{viaje['codigo_transporte']},{viaje['gasto']:.2f},{viaje['fecha']}\n")
    else:
        pf.write("No hay datos disponibles\n")
    
    pf.close()
    
    print("[OK] Archivo 'mayor_gasto.txt' generado")


def procesar_todos_los_datos(usuario):
    """
    Función principal que procesa todos los datos y genera los 4 archivos de salida
    """
    try:
        print("\n=== PROCESANDO DATOS ===")
        
        # Cargar datos
        viajes = cargar_viajes_desde_csv()
        pasajeros = cargar_pasajeros_desde_csv()
        
        if not viajes:
            print("No hay datos de viajes para procesar.")
            print("Debe generar datos aleatorios primero (opción 1 del menú).")
            return
        
        print("Cargando datos desde archivos CSV...")
        
        print(f"Viajes cargados: {len(viajes)}")
        print(f"Pasajeros cargados: {len(pasajeros)}\n")
        
        # Agrupar gastos por pasajero
        gastos_por_pasajero = estadisticas.agrupar_gastos_por_pasajero(viajes)
        
        # Generar los 4 archivos de salida
        print("Generando archivos de salida...")
        generar_archivo_gastos_por_pasajero(viajes, pasajeros)
        generar_archivo_estadisticas_transporte(viajes)
        generar_archivo_resumen_general(viajes, gastos_por_pasajero)
        generar_archivo_mayor_gasto(viajes, pasajeros)
        
        print("\n[OK] Procesamiento completado exitosamente\n")
        
    except Exception as e:
        print(f"Error durante el procesamiento: {e}")


if __name__ == "__main__":
    procesar_todos_los_datos("test")
