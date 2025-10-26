## 📌 Descripción

MOVI es un sistema de gestión de transportes desarrollado como proyecto académico para la materia Programación 1 de UADE. Aplica fundamentos de programación estructurada y manipulación de datos para simular la administración de viajes en una empresa de transporte, fortaleciendo competencias en lógica de programación, estructuras de datos y resolución de problemas.

## 🛠️ Tecnologías

- **Lenguaje**: Python 3.x
- **Paradigma**: Programación estructurada
- **Módulos**: Solo `random` y `datetime` (estándar)
- **Restricciones**: Sin módulos externos, sin POO, sin librería CSV

## 🚀 Funcionalidades

- **ABM de usuarios** → Alta, Baja y autenticación con login/contraseña
- **Generación de datos** → Archivos CSV aleatorios (pasajeros, viajes, tarifas)
- **Registro de viajes** → Ingreso manual de viajes individuales
- **Procesamiento y análisis** → Cálculo de estadísticas por pasajero y tipo de transporte
- **Reportes**:
  - Gastos por pasajero (ordenados)
  - Estadísticas por transporte (colectivo, tren, subte)
  - Resumen general del sistema
  - Pasajero con mayor gasto
- **Sistema de logs** → Auditoría completa con timestamps

## 📂 Estructura del Proyecto

```
MOVI/
├── ETAPA1/                    # Primera etapa del proyecto
├── ETAPA2/                    # Segunda etapa (actual)
│   ├── datos_generados/       # Directorio para archivos de datos
│   │   └── README.md         # Único archivo versionado en este directorio
│   ├── documentacion/         # Documentación técnica
│   ├── main.py               # Programa principal
│   ├── generador_datos.py    # Generador de datos aleatorios
│   ├── procesador.py         # Procesador de datos y reportes
│   ├── estadisticas.py       # Módulo de cálculos estadísticos
│   └── .gitignore            # Configuración de archivos a ignorar
└── README.md
```

## 🔒 Gestión de Datos Confidenciales

El directorio `ETAPA2/datos_generados/` contiene archivos con información potencialmente confidencial (usuarios, contraseñas, datos personales). Por seguridad:

- ✅ El directorio y su README.md **SÍ** están versionados
- ❌ Los archivos de datos **NO** se suben al repositorio remoto
- 📝 El `.gitignore` está configurado para excluir automáticamente:
  - Archivos de usuarios y logs
  - Archivos CSV de datos
  - Archivos de reportes generados

### Archivos excluidos del repositorio:
- `usuarios.txt` - Credenciales de usuarios
- `logs.txt` - Registro de actividades
- `pasajeros.csv`, `viajes.csv`, `tarifas.csv` - Datos de entrada
- `gastos_por_pasajero.txt`, `estadisticas_transporte.txt`, etc. - Reportes

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd MOVI/ETAPA2
   ```

2. **Verificar que existe el directorio de datos:**
   El directorio `datos_generados/` debe existir. Si no existe, créalo:
   ```bash
   # Windows
   md datos_generados
   
   # Linux/Mac
   mkdir datos_generados
   ```

3. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

## 📋 Requisitos

- Python 3.x
- Solo módulos estándar: `random` y `datetime`
- No requiere instalación de dependencias externas
