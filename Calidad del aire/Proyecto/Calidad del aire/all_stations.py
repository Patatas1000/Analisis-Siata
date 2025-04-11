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
    tema_actual = [None]  # Usamos una lista mutable para almacenar el tema actual

    def actualizar_tema_y_grafico():
        nonlocal tema_actual
        if not frame_grafico.winfo_exists():
            return  # Detener la ejecución si el frame ha sido destruido

        # Detectar el tema del sistema
        nuevo_tema = darkdetect.theme()

        # Configurar el estilo de matplotlib si el tema ha cambiado
        if tema_actual[0] != nuevo_tema:
            tema_actual[0] = nuevo_tema
            if nuevo_tema == "Dark":
                plt.style.use("dark_background")
            else:
                plt.style.use("default")

            # Dibujar el gráfico nuevamente con el nuevo estilo
            dibujar_grafico()

        # Programar otra verificación en 1000 ms (1 segundo)
        frame_grafico.after(1000, actualizar_tema_y_grafico)

    def dibujar_grafico():
        # Limpiar el frame de gráfico antes de dibujar uno nuevo
        for widget in frame_grafico.winfo_children():
            widget.destroy()

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

    # Dibujar el gráfico inicial
    dibujar_grafico()

    # Iniciar el bucle de verificación del tema del sistema
    actualizar_tema_y_grafico()

def mostrar_dataframe(frame2, frame_grafico):
    tema_actual = [None]  # Para almacenar el tema actual del sistema

    def actualizar_tema():
        # Detectar el tema actual del sistema
        nuevo_tema = darkdetect.theme()

        # Si el tema cambió, actualizar estilos
        if tema_actual[0] != nuevo_tema:
            tema_actual[0] = nuevo_tema

            # Aplicar tema oscuro o claro al Treeview
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
        # Limpiar contenido previo en el frame_grafico
        for widget in frame_grafico.winfo_children():
            widget.destroy()

        # Crear un Treeview para mostrar el DataFrame
        tree = ttk.Treeview(frame_grafico)

        # Configurar las columnas, incluyendo la columna de índices
        tree["columns"] = ["Índice"] + list(frame2.columns)
        tree["show"] = "headings"  # Oculta la columna fantasma inicial

        # Configurar encabezados y ancho de las columnas
        tree.heading("Índice", text="Índice")
        tree.column("Índice", width=100, anchor="center")  # Índices centrados
        for column in frame2.columns:
            tree.heading(column, text=column)
            tree.column(column, width=100, anchor="center")

        # Insertar las primeras 20 filas del DataFrame, incluyendo los índices
        for index, row in frame2.head(30).iterrows():
            tree.insert("", "end", values=[index] + list(row))

        # Empaquetar el Treeview en el frame_grafico
        tree.pack(fill="both", expand=True)

        # Llamar a la función para actualizar el estilo del tema
        actualizar_tema()

    def bucle_actualizacion():
        actualizar_tema()  # Verificar y actualizar el estilo según el tema
        frame_grafico.after(1000, bucle_actualizacion)  # Repetir cada 1 segundo

    # Dibujar el DataFrame inicial
    dibujar_dataframe()

    # Iniciar la actualización dinámica del tema
    bucle_actualizacion()