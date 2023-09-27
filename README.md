# Informe de Trabajo Parcial

## Universidad Peruana de Ciencias Aplicadas

## Carrera
Ingeniería de Software

## Ciclo
2023-02

## Curso
Complejidad Algorítmica

## Sección
WX73

## Profesor
Luis Martin Carnaval Sánchez

## Tema
Optimización de Redes de Fibra Óptica de Internet

## Integrantes
- Salvador Antonio Salinas Torres (U20221B127)
- Jorge Suin Yum Gonzales (U202210838)
- Daniel Elias Ruiz Huisa (U202210764)

## Septiembre 2023

## Descripción del Problema

En la era digital actual, la conectividad es el tejido que une a nuestro mundo interconectado. Las redes de comunicación son la columna vertebral que sostiene nuestras vidas cotidianas y nuestras economías globales. Entre las tecnologías que han revolucionado nuestra capacidad de comunicarnos y acceder a información de manera instantánea, la fibra óptica se destaca como una innovación fundamental. La fibra óptica, con su capacidad para transmitir datos a grandes velocidades, distancias y sin pérdidas, se ha convertido en el medio de elección para la transmisión de datos en redes de telecomunicaciones.

La fibra óptica no solo facilita la comunicación entre personas, sino también la automatización industrial, la educación en línea, comercio electrónico, entre otras aplicaciones importantes. Además, las redes de fibra óptica son esenciales para el funcionamiento eficiente de la infraestructura de Internet, el acceso a servicios en la nube y el respaldo de la creciente demanda de transmisión de datos de alta calidad.

Sin embargo, el verdadero potencial de la fibra óptica se realiza a través de la optimización continua. La optimización de las redes de fibra óptica es crucial para garantizar que los datos se transmitan de manera eficiente, segura y sin demoras en su recorrido desde el origen hasta el destino. De este modo, la latencia, capacidad y fiabilidad son factores críticos que deben ser considerados y mejorados constantemente.

Así es como el problema a abordar en este trabajo se enfoca en la optimización de redes de fibra óptica de Internet, con el objetivo de mejorar la calidad del servicio, eficiencia y velocidad de conexión para los usuarios. Las redes de fibra óptica cumplen un rol muy importante en la infraestructura de Internet, por lo que su optimización es esencial para garantizar que tenga un rendimiento óptimo.

## Descripción y Visualización del Conjunto de Datos

Para llevar a cabo el análisis, los datos utilizados para este análisis serán generados de forma artificial. El conjunto de datos contiene información detallada sobre la topología de la red de fibra óptica, la capacidad de ancho de banda, latencia. Igualmente, el objetivo es que el programa final sea eficiente y capaz de optimizar las redes de una fibra óptica real, con datos reales, por lo que se procurará que estos datos no se alejen mucho de la realidad.

Al tratarse de un análisis que requiere del estudio de un grafo, se tomarán en cuenta 1500 nodos de fibra óptica en la infraestructura de Internet. Cada nodo tendrá los siguientes datos:
| Dato | Descripción |
|----------|----------|
| ID | Identificador único para poder hacerle seguimiento   |
| Dirección IP | Identificador que usa para el envío de datos
| Ubicación geográfica | Coordenadas (latitud y longitud)
| Capacidad de ancho de banda | Capacidad que tiene para enviar datos y recibir datos en un tiempo dado
| Tipo de equipo | Dispositivo que representa el nodo

Para las aristas, se considerará la latencia que hay desde un nodo hacia otro, lo cual es importante para determinar la latencia mínima en la red.
