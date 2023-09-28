# Informe de Trabajo Parcial

## Carátula
Universidad Peruana de Ciencias Aplicadas
Carrera: Ingeniería de Software

Ciclo: 2023-02

Curso: Complejidad Algorítmica

Sección: WX73

Profesor: Luis Martin Carnaval Sánchez

Tema: Optimización de Redes de Fibra Óptica de Internet

Integrantes
- Salvador Antonio Salinas Torres (U20221B127)
- Jorge Suin Yum Gonzales (U202210838)
- Daniel Elias Ruiz Huisa (U202210764)

Septiembre 2023

## Descripción del Problema

En la era digital actual, la conectividad es el tejido que une a nuestro mundo interconectado. Las redes de comunicación son la columna vertebral que sostiene nuestras vidas cotidianas y nuestras economías globales. Entre las tecnologías que han revolucionado nuestra capacidad de comunicarnos y acceder a información de manera instantánea, la fibra óptica se destaca como una innovación fundamental. La fibra óptica, con su capacidad para transmitir datos a grandes velocidades, distancias y sin pérdidas, se ha convertido en el medio de elección para la transmisión de datos en redes de telecomunicaciones.

La fibra óptica no solo facilita la comunicación entre personas, sino también la automatización industrial, la educación en línea, comercio electrónico, entre otras aplicaciones importantes. Además, las redes de fibra óptica son esenciales para el funcionamiento eficiente de la infraestructura de Internet, el acceso a servicios en la nube y el respaldo de la creciente demanda de transmisión de datos de alta calidad.

Sin embargo, el verdadero potencial de la fibra óptica se realiza a través de la optimización continua. La optimización de las redes de fibra óptica es crucial para garantizar que los datos se transmitan de manera eficiente, segura y sin demoras en su recorrido desde el origen hasta el destino. De este modo, la latencia, capacidad y fiabilidad son factores críticos que deben ser considerados y mejorados constantemente.

## Descripción y Visualización del Conjunto de Datos

Para llevar a cabo el análisis, los datos utilizados para este análisis serán generados de forma artificial. El conjunto de datos contiene información detallada sobre la topología de la red de fibra óptica, la capacidad de ancho de banda, latencia. Igualmente, el objetivo es que el programa final sea eficiente y capaz de optimizar las redes de una fibra óptica real, con datos reales, por lo que se procurará que estos datos no se alejen mucho de la realidad.

Al tratarse de un análisis que requiere del estudio de un grafo, se tomarán en cuenta 1500 nodos de fibra óptica en la infraestructura de Internet. Cada nodo tendrá los siguientes datos:
| Dato | Descripción |
|----------|----------|
| ID | Identificador único del switch |
| Marca | Marca del switch |
| Modelo | Modelo del switch |
| Puertos | Cantidad de puertos del switch
| Ubicación | Coordenadas (latitud y longitud)
| Capacidad de ancho de banda | Capacidad que tiene para enviar datos y recibir datos en un tiempo dado

Para las aristas, se considerará la latencia que hay desde un nodo hacia otro, lo cual es importante para determinar la latencia mínima en la red.

| Dato | Descripción |
|----------|----------|
| Nodo1 | Index del primer switch |
| Nodo2 | Index del segundo switch |
| Latencia | Latencia entre ambos switches (en microsegundos) |

Una muestra de datos para un nodo.
| Dato | Ejemplo |
|----------|----------|
| ID | 76505 |
| Marca | Juniper Networks |
| Modelo | V6SV1K |
| Puertos | 12 |
| Ubicación | (89.49640570453458, 65.97759746460487) |
| Ancho de banda | 210 |

Una muestra de datos para una arista.
| Dato | Ejemplo |
|----------|----------|
| Nodo1 | 401 |
| Nodo2 | 1023 |
| Latencia | 75 |




