# Sistema de Registro y Supervisión de Pasajeros de Transporte Privado

## Descripción del Proyecto

Sistema digital que permite registrar y supervisar la actividad de los pasajeros de transporte privado, contemplando sus gastos diarios y el tipo de transporte utilizado (colectivo, tren, subte). El sistema automatiza el cálculo del gasto total, el promedio de consumo por pasajero y la identificación del usuario con mayores gastos, además de determinar cuál es el transporte más y menos utilizado.

## Características Principales

- **Gestión de Usuarios**: Sistema de registro y login con credenciales almacenadas en archivo de texto
- **Generación de Datos Aleatorios**: Creación automática de datos de prueba (pasajeros, viajes, tarifas)
- **Registro de Viajes**: Interfaz para registrar viajes individuales de pasajeros
- **Procesamiento de Datos**: Análisis completo de información con generación de estadísticas
- **Reportes Detallados**: Múltiples informes con análisis estadísticos
- **Sistema de Logs**: Bitácora completa de todas las operaciones del sistema

## Estructura del Proyecto

```
ETAPA2/
│
├── main.py                           # Programa principal con menús y login
├── generador_datos.py                # Módulo de generación de datos aleatorios
├── procesador.py                     # Módulo de procesamiento de datos
├── estadisticas.py                   # Módulo de cálculos estadísticos
├── README.md                         # Documentación del proyecto
│
├── usuarios.txt                      # Base de datos de usuarios (generado)
├── logs.txt                          # Archivo de logs del sistema (generado)
│
├── pasajeros.csv                     # Archivo de entrada 1 (generado)
├── viajes.csv                        # Archivo de entrada 2 (generado)
├── tarifas.csv                       # Archivo de entrada 3 (generado)
│
├── gastos_por_pasajero.txt          # Archivo de salida 1 (generado)
├── estadisticas_transporte.txt      # Archivo de salida 2 (generado)
├── resumen_general.txt              # Archivo de salida 3 (generado)
└── mayor_gasto.txt                  # Archivo de salida 4 (generado)
```

## Requisitos Técnicos Implementados

### Bloque 1 - Conceptos Previos

- ✅ **Control de versiones con GIT/GitHub**: Proyecto versionado
- ✅ **Estructuras de datos - Listas**: Usadas extensivamente en todos los módulos
- ✅ **Funciones lambda**: Implementadas en `estadisticas.py`
  - Filtrado de viajes por tipo de transporte
  - Extracción de gastos
  - Búsqueda de máximos/mínimos
- ✅ **Listas por comprensión**: 
  - `generador_datos.py`: Generación de IDs y nombres
  - `estadisticas.py`: Procesamiento de datos
- ✅ **Slicing**: `estadisticas.py` - función `obtener_top_n_pasajeros()`
- ✅ **Programación modular**: 3 módulos propios (generador_datos, procesador, estadisticas)
- ✅ **Random**: `generador_datos.py` - generación de datos aleatorios
- ✅ **Strings**: Manipulación extensiva en todo el proyecto

### Bloque 2 - Nuevos Conceptos

- ✅ **Manejo de excepciones**: Try-except en todas las funciones críticas
- ✅ **Archivos de texto plano/CSV**: Sin uso de librería csv
  - 3 archivos de entrada generados
  - 4 archivos de salida con resultados
  - Archivo de logs
  - Base de datos de usuarios
- ✅ **Diccionarios**: 
  - Agrupación de gastos por pasajero
  - Almacenamiento de estadísticas
  - Información de pasajeros
- ✅ **Recursividad**: `estadisticas.py`
  - `sumar_lista_recursiva()`
  - `contar_elementos_recursivo()`
  - `maximo_recursivo()`
  - `minimo_recursivo()`
  - `ordenar_por_gasto_recursivo()`

## Requisitos Funcionales

### 1. Sistema de Autenticación
- **Registro de usuarios**: Almacenamiento en `usuarios.txt`
- **Login**: Verificación de credenciales
- **Validación**: Usuarios únicos, campos no vacíos

### 2. Menú Principal
- Interfaz de consola con validación de excepciones
- Opciones claras y numeradas
- Manejo de errores de entrada

### 3. Archivos de Entrada (Generados Aleatoriamente)

#### pasajeros.csv
```csv
id_pasajero,nombre,edad
P0001,Juan García,45
P0002,María López,32
...
```
- 50-100 pasajeros aleatorios
- IDs únicos
- Nombres y edades aleatorias

#### viajes.csv
```csv
id_pasajero,codigo_transporte,gasto,fecha
P0001,1,245.50,2024-10-10
P0002,3,180.25,2024-10-12
...
```
- 200-500 viajes aleatorios
- Códigos de transporte: 1=colectivo, 2=tren, 3=subte
- Gastos variables según tipo
- Fechas de los últimos 30 días

#### tarifas.csv
```csv
codigo_transporte,codigo_segmento,tarifa
1,1,150.00
1,2,250.00
1,3,125.00
2,1,120.00
2,2,200.00
2,3,100.00
3,1,140.00
3,2,230.00
3,3,115.00
```
- Códigos de transporte: 1=colectivo, 2=tren, 3=subte
- Códigos de segmento: 1=<18 (menores), 2=18-64 (adultos), 3=>=65 (adultos mayores)
- Tarifas fijas por tipo de transporte y segmento de edad

### 4. Archivos de Salida (Procesados)

#### 1. gastos_por_pasajero.txt
- Lista completa de pasajeros con sus gastos totales
- Ordenado de mayor a menor gasto
- Incluye nombre y datos del pasajero

#### 2. estadisticas_transporte.txt
- Estadísticas detalladas por tipo de transporte
- Cantidad de viajes y porcentaje de uso
- Total recaudado, promedios, máximos y mínimos
- Identificación de transporte más y menos utilizado

#### 3. resumen_general.txt
- Resumen completo del sistema
- Total de viajes y pasajeros
- Recaudación total
- Promedios generales
- Distribución por tipo de transporte

#### 4. mayor_gasto.txt
- Información detallada del pasajero con mayor gasto
- Listado de todos sus viajes
- Estadísticas personalizadas por tipo de transporte

### 5. Sistema de Logs
- Archivo `logs.txt` con registro de todas las operaciones
- Formato: `[fecha hora] usuario: acción`
- Registro de login, generación de datos, procesamiento, visualización

## Instalación y Uso

### Requisitos
- Python 3.x
- No requiere librerías externas (solo módulos estándar)

### Ejecución

1. **Iniciar el sistema**:
```bash
python main.py
```

2. **Primer uso**:
   - Seleccionar opción 1: Registrar usuario
   - Crear credenciales (usuario y contraseña)
   - Seleccionar opción 2: Iniciar sesión
   - Ingresar credenciales creadas

3. **Flujo recomendado**:
   1. Iniciar sesión
   2. Acceder al sistema (opción 3)
   3. Generar datos aleatorios (opción 1)
   4. Procesar datos y generar estadísticas (opción 3)
   5. Ver reportes (opción 4)

### Funciones del Menú Principal

```
=== SISTEMA DE TRANSPORTE ===
1. Generar datos aleatorios de pasajeros
2. Registrar viaje de pasajero
3. Procesar datos y generar estadísticas
4. Ver reportes
5. Ver logs del sistema
0. Volver al menú principal
```

## Módulos del Sistema

### main.py
**Funciones principales**:
- `registrar_usuarios()`: ABM de usuarios
- `realizar_login()`: Autenticación
- `registrar_log(usuario, mensaje)`: Sistema de bitácora
- `mostrar_menu(usuario)`: Menú principal del sistema
- `registrar_viaje(usuario)`: Registro manual de viajes
- `mostrar_reportes(usuario)`: Visualización de informes
- `ver_logs(usuario)`: Consulta de bitácora
- `main()`: Función principal

### generador_datos.py
**Funciones**:
- `generar_ids_pasajeros(cantidad)`: List comprehension para IDs
- `generar_nombres_aleatorios(cantidad)`: Lambda para nombres
- `generar_fechas_aleatorias(cantidad, dias_atras)`: Fechas random
- `generar_archivo_pasajeros()`: CSV de pasajeros
- `generar_archivo_viajes()`: CSV de viajes
- `generar_archivo_tarifas()`: CSV de tarifas
- `generar_archivos_aleatorios()`: Función orquestadora

### estadisticas.py
**Funciones recursivas**:
- `sumar_lista_recursiva(lista, indice)`: Suma recursiva
- `contar_elementos_recursivo(lista, elemento, indice)`: Conteo recursivo
- `maximo_recursivo(lista, indice, max_actual)`: Máximo recursivo
- `minimo_recursivo(lista, indice, min_actual)`: Mínimo recursivo
- `ordenar_por_gasto_recursivo(lista_tuplas, indice)`: Bubble sort recursivo

**Funciones con lambda**:
- `filtrar_por_transporte(viajes, codigo_transporte)`: Filter con lambda (códigos 1, 2, 3)
- `obtener_gastos(viajes)`: Map con lambda
- `encontrar_pasajero_mayor_gasto(gastos_por_pasajero)`: Max con lambda

**Funciones estadísticas**:
- `calcular_promedio(lista)`: Promedio
- `calcular_estadisticas_transporte(viajes)`: Stats por transporte
- `agrupar_gastos_por_pasajero(viajes)`: Diccionarios
- `calcular_porcentajes_transporte(viajes)`: Porcentajes
- `obtener_top_n_pasajeros(gastos_por_pasajero, n)`: Slicing
- `generar_resumen_estadistico(viajes, gastos_por_pasajero)`: Resumen completo

### procesador.py
**Funciones**:
- `cargar_viajes_desde_csv()`: Lectura sin cargar todo en memoria
- `cargar_pasajeros_desde_csv()`: Carga de pasajeros
- `generar_archivo_gastos_por_pasajero(viajes, pasajeros)`: Salida 1
- `generar_archivo_estadisticas_transporte(viajes)`: Salida 2
- `generar_archivo_resumen_general(viajes, gastos_por_pasajero)`: Salida 3
- `generar_archivo_mayor_gasto(viajes, pasajeros)`: Salida 4
- `procesar_todos_los_datos(usuario)`: Función principal

## Análisis Estadístico

### Métricas Calculadas

1. **Por Pasajero**:
   - Gasto total
   - Cantidad de viajes
   - Ranking de gastos

2. **Por Tipo de Transporte**:
   - Cantidad de viajes
   - Porcentaje de uso
   - Total recaudado
   - Promedio de gasto
   - Gasto máximo/mínimo

3. **Generales**:
   - Total de viajes
   - Total de pasajeros únicos
   - Recaudación total
   - Promedio general
   - Transporte más/menos utilizado

## Validaciones Implementadas

- **Entrada de datos**: Validación de campos vacíos
- **Tipos de datos**: Conversión y validación numérica
- **Archivos**: Manejo de archivos no encontrados
- **Login**: Verificación de credenciales
- **Menús**: Opciones válidas con manejo de excepciones
- **Datos numéricos**: Validación de montos positivos

## Manejo de Errores

Todos los módulos implementan manejo robusto de excepciones:
- `FileNotFoundError`: Archivos no existentes
- `ValueError`: Conversiones y validaciones
- `Exception`: Errores generales

## Restricciones Cumplidas

- ✅ No se usa programación orientada a objetos
- ✅ No se usan librerías externas (solo random y datetime del estándar)
- ✅ No se usa la librería csv (lectura/escritura manual)
- ✅ Módulos propios con funciones modulares

## Ejemplos de Uso

### Generar Datos de Prueba
```python
import generador_datos
generador_datos.generar_archivos_aleatorios()
```

### Procesar Datos
```python
import procesador
procesador.procesar_todos_los_datos("usuario_admin")
```

### Calcular Estadísticas
```python
import estadisticas
viajes = [...]  # Lista de viajes
stats = estadisticas.calcular_estadisticas_transporte(viajes)
```

## Notas Técnicas

1. **Sin carga completa en memoria**: Los archivos se procesan línea por línea cuando es posible
2. **Recursividad real**: Todas las funciones recursivas son genuinas (no simuladas)
3. **Lambda funcionales**: Se usan lambdas donde aportan claridad y concisión
4. **Modularidad**: Separación clara de responsabilidades entre módulos
5. **Logs automáticos**: Todas las acciones importantes se registran

## Autor

Proyecto desarrollado para UADE - Programación 1
Sistema de Gestión de Transporte Público [MOVI - GRUPO 2] - ETAPA 2

## Licencia

Proyecto académico - Uso educativo
