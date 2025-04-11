# Esta función permite graficar los promedios diarios de las estaciones de calidad del aire

import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
from database_info import data
import glob
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sv_ttk
import darkdetect
import pywinstyles, sys

def all(frame2, frame_grafico):
    # Detectar el tema del sistema usando darkdetect
    tema_actual = darkdetect.theme()

    # Configurar el estilo de matplotlib según el tema
    if tema_actual == "Dark":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")

    columnas = ['pm25', 'no', 'no2', 'nox', 'ozono', 'so2']  # Lista de columnas a procesar
    medias_dict = {}

    for columna in columnas:
        frame_filtrado = frame2[(frame2[columna] > 0) & (frame2[columna] < 700)]
        medias = frame_filtrado.groupby([frame_filtrado.index.year,
                                         frame_filtrado.index.month,
                                         frame_filtrado.index.day])[columna].mean()
        medias.index.names = ["Año", "Mes", "Día"]
        medias_df = medias.to_frame(name=columna)
        medias_df.index = pd.to_datetime(frame_filtrado.groupby(
            [frame_filtrado.index.year, frame_filtrado.index.month, frame_filtrado.index.day]
        ).apply(lambda x: x.index[0]).values)
        medias_dict[columna] = medias_df

    # Limpiar el frame de gráfico antes de dibujar uno nuevo
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    # Crear figura de matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    colores = ['b', 'r', 'g', 'purple', 'y', 'orange']
    for i, columna in enumerate(columnas):
        ax.plot(medias_dict[columna].index, medias_dict[columna][columna],
                marker='.', linestyle='-', color=colores[i], label=f'Promedio {columna.capitalize()}')
    ax.set_title('Promedio Diario de concentración', fontsize=14)
    ax.set_xlabel('Fecha', fontsize=12)
    ax.set_ylabel('Concentración contaminante (µg/m³)', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    fig.tight_layout()

    # Incrustar el gráfico en el frame_grafico
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)