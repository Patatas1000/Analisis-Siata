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

def mostrar_grafico_est(frame_filtrado, frame_contenido):
    tema_actual = [None]

    def actualizar_tema_y_grafico():
        nonlocal tema_actual
        if not frame_contenido.winfo_exists():
            return

        nuevo_tema = darkdetect.theme()
        if tema_actual[0] != nuevo_tema:
            tema_actual[0] = nuevo_tema
            if nuevo_tema == "Dark":
                plt.style.use("dark_background")
            else:
                plt.style.use("default")
            dibujar_grafico_est()

        frame_contenido.after(1000, actualizar_tema_y_grafico)

    def dibujar_grafico_est():
        for widget in frame_contenido.winfo_children():
            widget.destroy()

        columnas = ['pm25','pm10', 'no', 'no2', 'nox', 'ozono','so2']
        medias_dict = {}

        for columna in columnas:
            frame_validado = frame_filtrado[(frame_filtrado[columna] > 0) & (frame_filtrado[columna] < 700)]

            if frame_validado.empty:
                # print(f"No hay datos válidos para la columna '{columna}'.")
                continue

            medias = frame_validado.groupby([frame_validado.index.year,
                                             frame_validado.index.month,
                                             frame_validado.index.day])[columna].mean()
            medias.index.names = ["Año", "Mes", "Día"]

            fechas_validas = frame_validado.groupby(
                [frame_validado.index.year, frame_validado.index.month, frame_validado.index.day]
            ).apply(lambda x: x.index[0])

            if fechas_validas.empty:
                # print(f"No hay fechas válidas para la columna '{columna}'.")
                continue

            medias_df = medias.to_frame(name=columna)
            medias_df.index = pd.to_datetime(fechas_validas.values, errors='coerce')
            medias_dict[columna] = medias_df

        if not medias_dict:
            label = ttk.Label(frame_contenido, text="No hay datos válidos para graficar.", font=("Arial", 14))
            label.pack(fill="both", expand=True)
            return

        fig, ax = plt.subplots(figsize=(10, 6))
        colores = ['b', 'r', 'g', 'purple', 'y', 'orange', 'c']
        for i, columna in enumerate(columnas):
            if columna in medias_dict:
                ax.plot(medias_dict[columna].index, medias_dict[columna][columna],
                        marker='.', linestyle='-', color=colores[i], label=f'Promedio {columna.capitalize()}')
        ax.set_title('Promedio Diario de Concentración', fontsize=14)
        ax.set_xlabel('Fecha', fontsize=12)
        ax.set_ylabel('Concentración contaminante (µg/m³)', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=frame_contenido)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    dibujar_grafico_est()
    actualizar_tema_y_grafico()

def mostrar_dataframe_est(frame_filtrado, frame_contenido):
    def actualizar_tema():
        nuevo_tema = darkdetect.theme()
        estilo = ttk.Style()
        if nuevo_tema == "Dark":
            estilo.theme_use("clam")
            estilo.configure("Treeview", background="#2d2d2d", foreground="white", fieldbackground="#2d2d2d")
            estilo.configure("Treeview.Heading", background="#3d3d3d", foreground="white")
        else:
            estilo.theme_use("default")
            estilo.configure("Treeview", background="white", foreground="black", fieldbackground="white")
            estilo.configure("Treeview.Heading", background="#f0f0f0", foreground="black")

    def dibujar_dataframe_est():
        for widget in frame_contenido.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(frame_contenido)
        columnas = ["Índice"] + list(frame_filtrado.columns)
        tree["columns"] = columnas
        tree["show"] = "headings"

        for columna in columnas:
            tree.heading(columna, text=columna)
            tree.column(columna, width=100, anchor="center")

        for index, row in frame_filtrado.head(40).iterrows():
            tree.insert("", "end", values=[index] + list(row))

        tree.pack(fill="both", expand=True)
        actualizar_tema()

    dibujar_dataframe_est()