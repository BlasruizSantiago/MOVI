from datetime import datetime
import generador_datos
import procesador

def registrar_usuarios():
    """Registra un nuevo usuario en el archivo usuarios.txt"""
    while True:
        try:
            print("\n=== REGISTRAR USUARIO ===")
            
            nombre_usuario = input("Ingrese nombre de usuario: ").strip()
            
            if not nombre_usuario:
                print("Error: El nombre de usuario no puede estar vacío.")
                continue
            
            # Verificar si el usuario ya existe
            try:
                pf = open("datos_generados/usuarios.txt", "r")
                for linea in pf:
                    usuario_existente = linea.strip().split(",")[0]
                    if usuario_existente == nombre_usuario:
                        print("Error: El usuario ya existe.")
                        pf.close()
                        raise ValueError("Usuario duplicado")
                pf.close()
            except FileNotFoundError:
                # Si el archivo no existe, es el primer usuario
                pass
            except ValueError:
                # Usuario duplicado, reintentar
                continue
        
            contraseña = input("Ingrese contraseña: ").strip()
            
            if not contraseña:
                print("Error: La contraseña no puede estar vacía.")
                continue
            
            # Guardar el usuario en el archivo
            pf = open("datos_generados/usuarios.txt", "a")
            pf.write(f"{nombre_usuario},{contraseña}\n")
            pf.close()
            
            print("¡Usuario registrado exitosamente!")
            break
            
        except Exception as e:
            print(f"Error inesperado: {e}")
            break


def realizar_login():
    """Realiza el login de un usuario y retorna el nombre de usuario si es exitoso"""
    while True:
        try:
            print("\n=== INICIAR SESIÓN ===")
            
            nombre_usuario = input("Ingrese nombre de usuario: ").strip()
            
            if not nombre_usuario:
                print("Error: El nombre de usuario no puede estar vacío.")
                continue
            
            # Verificar si el usuario existe antes de pedir la contraseña
            try:
                pf = open("datos_generados/usuarios.txt", "r")
                usuarios_existentes = {}
                
                for linea in pf:
                    datos = linea.strip().split(",")
                    if len(datos) == 2:
                        usuarios_existentes[datos[0]] = datos[1]
                
                pf.close()
                
                # Validar si el usuario existe
                if nombre_usuario not in usuarios_existentes:
                    print(f"Error: El usuario '{nombre_usuario}' no existe.")
                    continue
                
            except FileNotFoundError:
                print("Error: No hay usuarios registrados.")
                print("Debe registrar un usuario primero (opción 1 del menú principal).")
                return None
            
            # Si el usuario existe, pedir contraseña
            contraseña = input("Ingrese contraseña: ").strip()
            
            if not contraseña:
                print("Error: La contraseña no puede estar vacía.")
                continue
            
            # Verificar contraseña
            if usuarios_existentes[nombre_usuario] == contraseña:
                print(f"¡Bienvenido, {nombre_usuario}!")
                registrar_log(nombre_usuario, f"Usuario {nombre_usuario} inició sesión")
                return nombre_usuario
            else:
                print("Error: Contraseña incorrecta.")
                continue
                
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None


def registrar_log(usuario, mensaje):
    """Registra la actividad del usuario en un archivo de logs"""
    if usuario:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        # Ejemplo de valor obtenido: 2023-05-10 14:30:00
        
        pf = open("datos_generados/logs.txt", "a")
        pf.write(f"[{timestamp}] {usuario}: {mensaje}\n")
        pf.close()


def mostrar_menu(usuario):
    """Muestra el menú principal del sistema de transporte"""
    if not usuario:
        print("\nError: Debe iniciar sesión primero.")
        return
    
    while True:
        try:
            print(f"\n=== SISTEMA DE TRANSPORTE - Usuario: {usuario} ===")
            print("1. Generar datos aleatorios de pasajeros")
            print("2. Registrar viaje de pasajero")
            print("3. Procesar datos y generar estadísticas")
            print("4. Ver reportes")
            print("5. Ver logs del sistema")
            print("0. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                generador_datos.generar_archivos_aleatorios()
                registrar_log(usuario, "Generó archivos de datos aleatorios")
            elif opcion == "2":
                registrar_viaje(usuario)
            elif opcion == "3":
                procesador.procesar_todos_los_datos(usuario)
                registrar_log(usuario, "Procesó datos y generó estadísticas")
            elif opcion == "4":
                mostrar_reportes(usuario)
            elif opcion == "5":
                ver_logs(usuario)
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError as e:
            print(f"Error de valor: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
            registrar_log(usuario, f"Error en menú: {e}")


def registrar_viaje(usuario):
    """Registra un viaje individual de un pasajero"""
    while True:
        try:
            print("\n=== REGISTRAR VIAJE ===")
            
            id_pasajero = input("ID del pasajero: ").strip()
            if not id_pasajero:
                print("Error: El ID no puede estar vacío.")
                continue
            
            print("\nTipo de transporte:")
            print("1. Colectivo")
            print("2. Tren")
            print("3. Subte")
            tipo_opcion = input("Seleccione (1-3): ").strip()
            
            if tipo_opcion not in ["1", "2", "3"]:
                print("Error: Opción inválida.")
                continue
            codigo_transporte = int(tipo_opcion)
            
            gasto = input("Monto del gasto: ").strip()
            try:
                gasto_float = float(gasto)
                if gasto_float <= 0:
                    print("Error: El gasto debe ser mayor a 0.")
                    continue
            except ValueError:
                print("Error: Ingrese un número válido.")
                continue
            
            # Guardar en archivo de viajes
            from datetime import datetime
            fecha = datetime.now().strftime("%Y-%m-%d")
            
            pf = open("datos_generados/viajes.csv", "a")
            pf.write(f"{id_pasajero},{codigo_transporte},{gasto_float},{fecha}\n")
            pf.close()
            
            nombres_transporte = {1: "colectivo", 2: "tren", 3: "subte"}
            print(f"✓ Viaje registrado exitosamente")
            registrar_log(usuario, f"Registró viaje: pasajero {id_pasajero}, {nombres_transporte[codigo_transporte]}, ${gasto_float}")
            break
            
        except Exception as e:
            print(f"Error: {e}")
            break


def mostrar_reportes(usuario):
    """Muestra los reportes generados"""
    try:
        print("\n=== REPORTES DISPONIBLES ===")
        print("1. Gastos por pasajero")
        print("2. Estadísticas de transporte")
        print("3. Resumen general")
        print("4. Pasajero con mayor gasto")
        print("0. Volver")
        
        opcion = input("\nSeleccione un reporte: ").strip()
        
        archivos = {
            "1": "gastos_por_pasajero.txt",
            "2": "estadisticas_transporte.txt",
            "3": "resumen_general.txt",
            "4": "mayor_gasto.txt"
        }
        
        if opcion in archivos:
            try:
                pf = open(f"datos_generados/{archivos[opcion]}", "r")
                contenido = pf.read()
                pf.close()
                print(f"\n{'='*60}")
                print(contenido)
                print(f"{'='*60}")
                registrar_log(usuario, f"Visualizó reporte: {archivos[opcion]}")
            except FileNotFoundError:
                print("Error: El archivo no existe. Debe procesar los datos primero.")
        elif opcion != "0":
            print("Opción inválida.")
            
    except Exception as e:
        print(f"Error al mostrar reportes: {e}")


def ver_logs(usuario):
    """Muestra los últimos registros del log"""
    try:
        pf = open("datos_generados/logs.txt", "r")
        lineas = pf.readlines()
        pf.close()
        
        print(f"\n=== ÚLTIMOS 20 REGISTROS DEL LOG ===")
        ultimas = lineas[-20:] if len(lineas) > 20 else lineas
        for linea in ultimas:
            print(linea.strip())
        
        registrar_log(usuario, "Visualizó logs del sistema")
    except FileNotFoundError:
        print("No hay logs disponibles.")
    except Exception as e:
        print(f"Error al leer logs: {e}")


def main():
    """Función principal del programa"""
    usuario_logueado = None
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Acceder al sistema")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            registrar_usuarios()
        elif opcion == "2":
            usuario_logueado = realizar_login()
        elif opcion == "3":
            mostrar_menu(usuario_logueado)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()