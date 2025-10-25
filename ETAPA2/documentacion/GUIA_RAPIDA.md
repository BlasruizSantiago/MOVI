# Guía Rápida de Inicio

## Inicio Rápido (5 pasos)

### 1. Ejecutar el programa
```bash
python main.py
```

### 2. Crear un usuario
```
Menú Principal > Opción 1: Registrar usuario
- Ingrese usuario: admin
- Ingrese contraseña: 1234
```

### 3. Iniciar sesión
```
Menú Principal > Opción 2: Iniciar sesión
- Ingrese usuario: admin
- Ingrese contraseña: 1234
```

### 4. Generar datos de prueba
```
Menú Principal > Opción 3: Acceder al sistema
Sistema de Transporte > Opción 1: Generar datos aleatorios
```

### 5. Procesar y ver resultados
```
Sistema de Transporte > Opción 3: Procesar datos y generar estadísticas
Sistema de Transporte > Opción 4: Ver reportes
```

## Opciones del Sistema

### Menú Principal
- **Opción 1**: Registrar nuevo usuario
- **Opción 2**: Iniciar sesión
- **Opción 3**: Acceder al sistema (requiere login)
- **Opción 0**: Salir

### Sistema de Transporte (Requiere login)
- **Opción 1**: Generar archivos con datos aleatorios
  - Crea pasajeros.csv (50-100 pasajeros)
  - Crea viajes.csv (200-500 viajes con códigos 1, 2, 3)
  - Crea tarifas.csv (9 tarifas: 3 tipos × 3 segmentos de edad)

- **Opción 2**: Registrar viaje manual
  - ID del pasajero
  - Tipo de transporte (1=Colectivo, 2=Tren, 3=Subte)
  - Monto del gasto

- **Opción 3**: Procesar datos y generar estadísticas
  - Lee archivos CSV de entrada
  - Genera 4 archivos de salida con reportes

- **Opción 4**: Ver reportes
  - 1: Gastos por pasajero (ordenado)
  - 2: Estadísticas de transporte
  - 3: Resumen general
  - 4: Pasajero con mayor gasto

- **Opción 5**: Ver logs del sistema
  - Muestra últimos 20 registros de actividad

- **Opción 0**: Volver al menú principal

## Archivos Generados

### Archivos de Entrada (se generan automáticamente)
- `pasajeros.csv`: Datos de pasajeros (id, nombre, edad)
- `viajes.csv`: Registro de viajes (códigos: 1=colectivo, 2=tren, 3=subte)
- `tarifas.csv`: Tarifas con códigos (transporte: 1,2,3 | segmento: 1,2,3)

### Archivos de Salida (se generan al procesar)
- `gastos_por_pasajero.txt`: Lista de pasajeros ordenada por gasto
- `estadisticas_transporte.txt`: Stats por tipo de transporte
- `resumen_general.txt`: Resumen completo del sistema
- `mayor_gasto.txt`: Detalle del pasajero con más gasto

### Archivos del Sistema
- `usuarios.txt`: Base de datos de usuarios
- `logs.txt`: Registro de actividades (bitácora)

## Ejemplos de Uso

### Escenario 1: Primera vez usando el sistema
```
1. python main.py
2. Opción 1 → Crear usuario
3. Opción 2 → Login
4. Opción 3 → Entrar al sistema
5. Opción 1 → Generar datos
6. Opción 3 → Procesar
7. Opción 4 → Ver reportes
```

### Escenario 2: Agregar viajes manualmente
```
1. python main.py
2. Opción 2 → Login
3. Opción 3 → Entrar al sistema
4. Opción 2 → Registrar viaje
   - ID: P0001
   - Transporte: 1 (Colectivo)
   - Gasto: 250.50
5. Repetir paso 4 para más viajes
6. Opción 3 → Procesar datos
7. Opción 4 → Ver reportes
```

### Escenario 3: Ver estadísticas existentes
```
1. python main.py
2. Opción 2 → Login
3. Opción 3 → Entrar al sistema
4. Opción 4 → Ver reportes
   - Elegir reporte deseado (1-4)
```

## Solución de Problemas

### Error: "No hay usuarios registrados"
**Solución**: Primero debes registrar un usuario (Opción 1 del menú principal)

### Error: "Debe iniciar sesión primero"
**Solución**: Debes hacer login antes de acceder al sistema (Opción 2)

### Error: "No existe el archivo viajes.csv"
**Solución**: Genera datos aleatorios primero (Opción 1 del sistema de transporte)

### Error: "El archivo no existe. Debe procesar los datos primero"
**Solución**: Ejecuta "Procesar datos" (Opción 3) antes de ver reportes

### Error: "Usuario o contraseña incorrectos"
**Solución**: Verifica tus credenciales o registra un nuevo usuario

## Requisitos Técnicos

- Python 3.x instalado
- No requiere librerías externas
- Sistema operativo: Windows, Linux o macOS

## Notas Importantes

1. **Primer uso**: Siempre debes registrar un usuario antes de usar el sistema
2. **Datos de prueba**: Usa la opción de generar datos aleatorios para probar rápidamente
3. **Logs**: Todas las acciones quedan registradas en `logs.txt`
4. **Sobrescritura**: Generar datos aleatorios sobrescribe los archivos CSV existentes
5. **Acumulación de viajes**: Los viajes registrados manualmente se agregan al archivo

## Comandos Útiles

### Ejecutar el programa
```bash
python main.py
```

### Generar solo datos aleatorios (sin menú)
```bash
python generador_datos.py
```

### Procesar datos directamente (sin menú)
```bash
python procesador.py
```

## Flujo Recomendado para Demostración

1. **Preparación**: Registrar usuario y hacer login
2. **Generación**: Crear datos aleatorios
3. **Procesamiento**: Generar estadísticas
4. **Visualización**: Ver todos los reportes (1-4)
5. **Logs**: Revisar bitácora de acciones
6. **Manual**: Agregar algunos viajes manualmente
7. **Re-proceso**: Procesar nuevamente para actualizar estadísticas
8. **Comparación**: Ver reportes actualizados

## Contacto y Soporte

Para consultas sobre el proyecto, referirse a la documentación completa en `README.md`
