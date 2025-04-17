# Análisis de la base de datos del SIATA

Este es un proyecto personal que tiene como fin usar diversas herramientas de Python, para realizar el análisis de los datos de calidad del aire provenientes del SIATA en la ciudad de Medellín.

## Requisitos previos

Para utilizar adecuadamente este programa debe instalar Python, a continuación se muestra en enlace de descarga.

https://www.python.org/downloads/

Luego de instalar la última versión de Python, debe instalar las librerías necesarias, esto se puede hacer en Windows siguiendo los pasos descritos a continuación.

- Presiona la tecla Win+R para abrir la ventana de ejecutar.
- En esta ventana escribe "cmd", sin comillas, y luego presiona Enter.
  Nota: Si está usando Visual Studio Code, use la consola de comandos dentro de Visual Studio.
- En la ventana del símbolo del sistema pega lo siguiente:

```
pip install sv-ttk
pip install darkdetect
pip install pywinstyles
pip install pandas
pip install numpy
pip install regex
pip install matplotlib
```
## Resumen

Este programa permite una fácil visualización de la información, además detecta anomalías entre los datos y se encarga de eliminarlas de manera automática, viéndose reflejado en los resultados.

Para facilitar la revisión de la información de hace uso de una interfaz diseñada que permite interactuar fácilmente con el programa y cada uno de los análisis que puede hacer, iniciando por la ventana principal.

![Ventana Principal](https://github.com/Patatas1000/Analisis-Siata/blob/Patatas1000-patch-1/Calidad%20del%20aire/Proyecto/Images/MainWindow.png)

Permitiendo realizar análisis al conjunto de datos completo, mostrando un gráfico de los promedios diarios de todos los datos válidos para los contaminantes, y mostrando una parte del conjunto de datos luego del procesamiento inicial.

![Gráfico del conjunto de datos completo](https://github.com/Patatas1000/Analisis-Siata/blob/Patatas1000-patch-1/Calidad%20del%20aire/Proyecto/Images/GraphAll.png)

![Conjunto de datos](https://github.com/Patatas1000/Analisis-Siata/blob/Patatas1000-patch-1/Calidad%20del%20aire/Proyecto/Images/DataAll.png)

Además, también permite realizar el análisis para cada una de las estaciones de manera individual, permitiendo elegir la estación acorde al código con el que se encuentre registrada, considerando que no en todas las estaciones se realizan los mismos análsis, el código filtra de manera automática para cada estación los contaminantes de los cuáles no se tiene registro y realiza la gráfica de los datos válidos, también en forma de promedios diarios de concentración de los contaminantes, adicionalmente, también se puede mostrar una parte de los datos utilizados para el análisis de cada estación.

![Gráfico realizado para una estación particular del SIATA](https://github.com/Patatas1000/Analisis-Siata/blob/Patatas1000-patch-1/Calidad%20del%20aire/Proyecto/Images/GraphEst2.png)
![Conjunto de datos para una estación particular del SIATA](https://github.com/Patatas1000/Analisis-Siata/blob/Patatas1000-patch-1/Calidad%20del%20aire/Proyecto/Images/DataEst.png)

Se pretende añadir más funciones a futuro, este es un trabajo en progreso.

