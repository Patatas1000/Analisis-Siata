# Esta función permite graficar los promedios diarios de las estaciones de calidad del aire

import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
from database_info import data
import glob
import os

def all(frame2):
    columnas = ['pm25', 'no', 'no2', 'nox', 'ozono', 'so2']  # Lista de columnas a procesar
    medias_dict = {}  # Diccionario para almacenar las series de medias

    for columna in columnas:
        frame_filtrado = frame2[(frame2[columna] > 0) & (frame2[columna] < 700)]
        medias = frame_filtrado.groupby([frame_filtrado.index.year,
                                         frame_filtrado.index.month,
                                         frame_filtrado.index.day])[columna].mean()
        medias.index.names = ["Año", "Mes", "Día"]
        # Convertir la serie a DataFrame y ajustar el índice
        medias_df = medias.to_frame(name=columna)
        medias_df.index = pd.to_datetime(frame_filtrado.groupby(
            [frame_filtrado.index.year, frame_filtrado.index.month, frame_filtrado.index.day]
        ).apply(lambda x: x.index[0]).values)
        medias_dict[columna] = medias_df  # Almacenar el DataFrame en el diccionario

    # Graficar los promedios para todas las columnas
    plt.figure(figsize=(10, 6))
    colores = ['b', 'r', 'g', 'purple', 'y', 'orange']  # Colores para las gráficas
    for i, columna in enumerate(columnas):
        plt.plot(medias_dict[columna].index, medias_dict[columna][columna],
                 marker='.', linestyle='-', color=colores[i], label=f'Promedio {columna.capitalize()}')
    plt.title('Promedio Diario de concentración', fontsize=14)
    plt.xlabel('Fecha', fontsize=12)
    plt.ylabel('Concentración contaminante (µg/m³)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    return plt.show()