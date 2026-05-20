# Análisis de Resultados Deportivos
## Trabajo Práctico — Organización Empresarial — UTN TUP 2026

## Integrantes
| Rol | Nombre | Responsabilidad |
|---|---|---|
| P1 - Hugo | [Matias Rojas] | Repositorio y estructura |
| P2 - Paco | [Lorenzo Tibaldi] | Script de análisis |
| P3 - Luis | [Matias Rojas] | Revisión y documentación |

## Escenario elegido
**Escenario D — Estadísticas de Resultados Deportivos**

## Dataset utilizado
Archivo: `datos/resultados_torneo.csv`  
Contenido: 10 partidos de un torneo con 5 equipos.  
Columnas: partido_id, fecha, equipo_local, equipo_visitante, goles_local, goles_visitante.

## Estructura del repositorio
celula-deportes-tup/
├── datos/
│   └── resultados_torneo.csv
├── scripts/
│   └── analisis_deportivo.py
├── resultados/
│   └── grafico_rendimiento.png
├── README.md
└── .gitignore
## Resultados del análisis
- Tabla de posiciones con puntos, victorias, empates y derrotas
- Promedio de goles por partido
- Gráfico comparativo de rendimiento entre equipos

## Instrucciones para ejecutar
1. Abrir Google Colab
2. Clonar el repositorio:
   `git clone https://github.com/matirojas07/celula-deportes-tup.git`
3. Ejecutar el script:
   `scripts/analisis_deportivo.py`
4. Los resultados se guardan en `/resultados`

## Gestión del proyecto
Tareas gestionadas en Jira bajo los IDs: CDTUP-2, CDTUP-3, CDTUP-4
