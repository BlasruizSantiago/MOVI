# Directorio de Datos Generados

Este directorio contiene todos los archivos generados por el sistema de transporte.

## Propósito

Los archivos en este directorio contienen datos potencialmente confidenciales y **NO deben subirse al repositorio remoto**. El `.gitignore` está configurado para excluir todos los archivos excepto este README.

## Archivos que se generan automáticamente:

### Archivos de entrada (generados por el usuario):
- `pasajeros.csv` - Datos de pasajeros (ID, nombre, edad)
- `viajes.csv` - Registros de viajes realizados
- `tarifas.csv` - Tarifas por tipo de transporte y segmento de edad

### Archivos del sistema:
- `usuarios.txt` - Credenciales de usuarios registrados
- `logs.txt` - Registro de actividades del sistema

### Archivos de salida (reportes):
- `gastos_por_pasajero.txt` - Gastos totales por pasajero
- `estadisticas_transporte.txt` - Estadísticas por tipo de transporte
- `resumen_general.txt` - Resumen general del sistema
- `mayor_gasto.txt` - Información del pasajero con mayor gasto

## Nota importante

Este directorio debe existir para que el programa funcione correctamente. Si no existe, créelo manualmente:
- **Windows**: `md datos_generados`
- **Linux/Mac**: `mkdir datos_generados`
