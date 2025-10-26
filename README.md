📌 Descripción
MOVI es un sistema simple de gestión de transportes desarrollado como parte de la materia Programación 1 de la universidad UADE
El objetivo del proyecto es aplicar los fundamentos de la programación estructurada y la manipulación de datos para simular la administración de viajes en una empresa de transporte.

🛠️ Tecnologías utilizadas
- Lenguaje: Python
- Paradigma: Programación estructurada
- IDE recomendado: VS Code

🚀 funcionalidades principales de tu proyecto serían:

- Alta y baja de usuarios → permite registrar nuevos pasajeros o eliminar los existentes.
- Registro de gastos diarios → cada pasajero tiene asociados sus viajes y montos según el transporte utilizado (colectivo, tren, subte).
- Cálculo del usuario con mayor gasto → identifica quién gastó más en el período analizado.
- Determinación del transporte más y menos utilizado → analiza la frecuencia de uso de colectivo, tren y subte.
- Promedio general de gastos → obtiene cuánto gastan en promedio los pasajeros.
- Gasto total de todos los pasajeros → muestra la suma global de los consumos.
- Distribución del 5% de las ganancias a los 3 usuarios más frecuentes → calcula cuánto recibe cada beneficiario.

🎯 Objetivo académico

Este proyecto tiene como finalidad aplicar los conocimientos adquiridos en la materia Programación I, desarrollando un sistema que permita gestionar de forma eficiente los datos de usuarios, sus gastos y el uso de distintos medios de transporte.
Además de fortalecer las competencias en lógica de programación, estructuras de datos y resolución de problemas, integrando conceptos teóricos en una implementación práctica que simula un caso real.

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
