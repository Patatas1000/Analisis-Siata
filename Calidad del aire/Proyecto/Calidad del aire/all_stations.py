# Esta función permite graficar los promedios diarios de las estaciones de calidad del aire

import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
from database_info import data
import glob
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import darkdetect
import tkinter as tk
from tkinter import ttk
import sv_ttk

def all(frame2, frame_grafico):
    tema_actual = [None]

    def actualizar_tema_y_grafico():
        nonlocal tema_actual
        if not frame_grafico.winfo_exists():
            return

        nuevo_tema = darkdetect.theme()

        if tema_actual[0] != nuevo_tema:
            tema_actual[0] = nuevo_tema
            if nuevo_tema == "Dark":
                plt.style.use("dark_background")
            else:
                plt.style.use("default")

            dibujar_grafico()

        frame_grafico.after(1000, actualizar_tema_y_grafico)

    def dibujar_grafico():
        for widget in frame_grafico.winfo_children():
            widget.destroy()

        columnas = ['pm25', 'pm10', 'no', 'no2', 'nox', 'ozono', 'so2']
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

        fig, ax = plt.subplots(figsize=(10, 6))
        colores = ['b', 'r', 'g', 'purple', 'y', 'orange', 'c']
        for i, columna in enumerate(columnas):
            ax.plot(medias_dict[columna].index, medias_dict[columna][columna],
                    marker='.', linestyle='-', color=colores[i], label=f'Promedio {columna.capitalize()}')
        ax.set_title('Promedio Diario de concentración', fontsize=14)
        ax.set_xlabel('Fecha', fontsize=12)
        ax.set_ylabel('Concentración contaminante (µg/m³)', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    dibujar_grafico()

    actualizar_tema_y_grafico()

def mostrar_dataframe(frame2, frame_grafico):
    tema_actual = [None]

    def actualizar_tema():
        nuevo_tema = darkdetect.theme()

        if tema_actual[0] != nuevo_tema:
            tema_actual[0] = nuevo_tema

            estilo = ttk.Style()
            if nuevo_tema == "Dark":
                estilo.theme_use("clam")
                estilo.configure(
                    "Treeview",
                    background="#2d2d2d",
                    foreground="white",
                    fieldbackground="#2d2d2d",
                )
                estilo.configure(
                    "Treeview.Heading",
                    background="#3d3d3d",
                    foreground="white",
                )
            else:
                estilo.theme_use("default")
                estilo.configure(
                    "Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="white",
                )
                estilo.configure(
                    "Treeview.Heading",
                    background="#f0f0f0",
                    foreground="black",
                )

    def dibujar_dataframe():
        for widget in frame_grafico.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(frame_grafico)

        tree["columns"] = ["Índice"] + list(frame2.columns)
        tree["show"] = "headings"

        tree.heading("Índice", text="Índice")
        tree.column("Índice", width=100, anchor="center")
        for column in frame2.columns:
            tree.heading(column, text=column)
            tree.column(column, width=100, anchor="center")

        for index, row in frame2.head(40).iterrows():
            tree.insert("", "end", values=[index] + list(row))

        tree.pack(fill="both", expand=True)

        actualizar_tema()

    def bucle_actualizacion():
        actualizar_tema()
        frame_grafico.after(1000, bucle_actualizacion)

    dibujar_dataframe()

    bucle_actualizacion()