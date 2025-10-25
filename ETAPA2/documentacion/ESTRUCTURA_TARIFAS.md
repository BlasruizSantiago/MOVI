# Estructura del Archivo de Tarifas

## Descripción General

El archivo `tarifas.csv` contiene las tarifas fijas del sistema de transporte público, organizadas por **código de transporte** y **segmento de edad**.

## Códigos de Transporte

| Código | Tipo de Transporte |
|--------|-------------------|
| 1      | Colectivo         |
| 2      | Tren              |
| 3      | Subte             |

## Códigos de Segmentos de Edad

| Código | Descripción | Rango de Edad |
|--------|-------------|---------------|
| 1      | Menores     | Menos de 18 años (<18) |
| 2      | Adultos     | Entre 18 y 64 años (18-64) |
| 3      | Adultos Mayores | 65 años o más (>=65) |

## Estructura del Archivo CSV

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

## Tarifas por Tipo de Transporte

### Colectivo (Código 1)
- **Segmento 1 - Menores (<18)**: $150.00
- **Segmento 2 - Adultos (18-64)**: $250.00
- **Segmento 3 - Adultos Mayores (≥65)**: $125.00

### Tren (Código 2)
- **Segmento 1 - Menores (<18)**: $120.00
- **Segmento 2 - Adultos (18-64)**: $200.00
- **Segmento 3 - Adultos Mayores (≥65)**: $100.00

### Subte (Código 3)
- **Segmento 1 - Menores (<18)**: $140.00
- **Segmento 2 - Adultos (18-64)**: $230.00
- **Segmento 3 - Adultos Mayores (≥65)**: $115.00

## Características

1. **Tarifas Fijas**: No varían aleatoriamente, son valores constantes
2. **Diferenciación por Edad**: Cada tipo de transporte tiene 3 tarifas según la edad del pasajero
3. **Total de Tarifas**: 9 tarifas (3 tipos × 3 segmentos)
4. **Descuentos Implícitos**: 
   - Menores: ~40% de descuento respecto a adultos
   - Adultos Mayores: ~50% de descuento respecto a adultos

## Uso en el Sistema

### Generación
La función `generar_archivo_tarifas()` en `generador_datos.py` crea este archivo con las tarifas predefinidas.

### Lectura
Aunque el sistema actual no utiliza directamente este archivo para validar gastos, está disponible como referencia para:
- Consultas de tarifas oficiales
- Validaciones futuras
- Análisis de cumplimiento tarifario

## Ejemplo de Uso

Para determinar la tarifa correcta:
1. Identificar el código de transporte (1, 2 o 3)
2. Determinar la edad del pasajero
3. Seleccionar el código de segmento correspondiente (1, 2 o 3)
4. Aplicar la tarifa correspondiente

### Ejemplo:
- Pasajero de 70 años viajando en colectivo (código transporte: 1)
- Código de segmento: 3 (>=65)
- Tarifa: $125.00

## Notas Técnicas

- El archivo se genera automáticamente al ejecutar la opción de generar datos aleatorios
- Las tarifas son valores fijos definidos en el código
- El formato es CSV estándar sin uso de la librería csv
- Cada línea representa una combinación única de código de transporte y segmento de edad
