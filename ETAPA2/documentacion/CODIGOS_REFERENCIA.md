# Archivos de Referencia de Códigos

## Descripción

El sistema utiliza códigos numéricos para representar tipos de transporte y segmentos de edad. Estos códigos están documentados en archivos CSV de referencia.

## Archivos de Referencia

### 1. codigos_transporte.csv

Contiene el mapeo entre códigos numéricos y tipos de transporte.

**Ubicación**: `ETAPA2/codigos_transporte.csv`

**Estructura**:
```csv
codigo,nombre
1,colectivo
2,tren
3,subte
```

**Uso**: Consultar el nombre del transporte a partir de su código.

### 2. codigos_segmentos.csv

Contiene el mapeo entre códigos numéricos y segmentos de edad.

**Ubicación**: `ETAPA2/codigos_segmentos.csv`

**Estructura**:
```csv
codigo,descripcion,rango_edad
1,menores,<18
2,adultos,18-64
3,adultos_mayores,>=65
```

**Uso**: Consultar la descripción y rango de edad a partir del código de segmento.

## Códigos de Transporte

| Código | Nombre    | Descripción |
|--------|-----------|-------------|
| 1      | colectivo | Autobús urbano |
| 2      | tren      | Tren de pasajeros |
| 3      | subte     | Metro/Subterráneo |

## Códigos de Segmentos de Edad

| Código | Descripción     | Rango de Edad | Criterio |
|--------|-----------------|---------------|----------|
| 1      | menores         | < 18 años     | edad < 18 |
| 2      | adultos         | 18-64 años    | 18 <= edad <= 64 |
| 3      | adultos_mayores | >= 65 años    | edad >= 65 |

## Uso en el Sistema

### En el archivo tarifas.csv

El archivo `tarifas.csv` utiliza ambos códigos:

```csv
codigo_transporte,codigo_segmento,tarifa
1,1,150.00
1,2,250.00
1,3,125.00
```

**Interpretación**:
- Primera fila: Colectivo (1) para menores (1) = $150.00
- Segunda fila: Colectivo (1) para adultos (2) = $250.00
- Tercera fila: Colectivo (1) para adultos mayores (3) = $125.00

### En el archivo viajes.csv

El archivo `viajes.csv` utiliza el código de transporte:

```csv
id_pasajero,codigo_transporte,gasto,fecha
P0001,1,245.50,2024-10-10
P0002,3,180.25,2024-10-12
```

**Interpretación**:
- Primera fila: Pasajero P0001 viajó en colectivo (1)
- Segunda fila: Pasajero P0002 viajó en subte (3)

## Ventajas del Sistema de Códigos

1. **Eficiencia**: Los números ocupan menos espacio que strings
2. **Velocidad**: Comparaciones numéricas son más rápidas
3. **Consistencia**: Evita errores de tipeo en nombres
4. **Escalabilidad**: Fácil agregar nuevos tipos sin modificar estructura
5. **Internacionalización**: Los códigos son independientes del idioma

## Función de Utilidad (Ejemplo)

Para convertir códigos a nombres en tus reportes:

```python
def obtener_nombre_transporte(codigo):
    """Retorna el nombre del transporte según su código"""
    nombres = {1: "colectivo", 2: "tren", 3: "subte"}
    return nombres.get(codigo, "desconocido")

def obtener_descripcion_segmento(codigo):
    """Retorna la descripción del segmento según su código"""
    segmentos = {1: "menores", 2: "adultos", 3: "adultos_mayores"}
    return segmentos.get(codigo, "desconocido")
```

## Lectura de Archivos de Referencia

Si necesitas leer los archivos de referencia dinámicamente:

```python
def cargar_codigos_transporte():
    """Carga el diccionario de códigos de transporte desde CSV"""
    codigos = {}
    pf = open("codigos_transporte.csv", "r")
    lineas = pf.readlines()[1:]  # Saltar encabezado
    pf.close()
    
    for linea in lineas:
        codigo, nombre = linea.strip().split(",")
        codigos[int(codigo)] = nombre
    
    return codigos

def cargar_codigos_segmentos():
    """Carga el diccionario de códigos de segmentos desde CSV"""
    segmentos = {}
    pf = open("codigos_segmentos.csv", "r")
    lineas = pf.readlines()[1:]  # Saltar encabezado
    pf.close()
    
    for linea in lineas:
        datos = linea.strip().split(",")
        codigo = int(datos[0])
        segmentos[codigo] = {
            "descripcion": datos[1],
            "rango_edad": datos[2]
        }
    
    return segmentos
```

## Notas Importantes

1. Los archivos de referencia son **estáticos** y no se modifican durante la ejecución
2. Están ubicados en la raíz del proyecto ETAPA2
3. No están en la carpeta `datos_generados/` porque son archivos de configuración
4. Pueden ser consultados manualmente o programáticamente
5. Sirven como documentación viva del sistema de códigos

## Mantenimiento

Si necesitas agregar un nuevo tipo de transporte o segmento:

1. Edita el archivo CSV correspondiente
2. Agrega una nueva línea con el siguiente código disponible
3. Actualiza la documentación
4. Regenera los datos de prueba si es necesario

### Ejemplo: Agregar "metrobus"

En `codigos_transporte.csv`:
```csv
codigo,nombre
1,colectivo
2,tren
3,subte
4,metrobus
```

Luego actualiza el generador de datos para incluir el código 4.
