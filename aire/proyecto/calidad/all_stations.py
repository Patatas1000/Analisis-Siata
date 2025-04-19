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
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def mostrar_todo(frame2, frame_grafico):
    tema_actual = darkdetect.theme()

    if tema_actual == "Dark":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")

    dibujar_grafico(frame2, frame_grafico, tema_actual)

def dibujar_grafico(frame2, frame_grafico, tema_actual):
    for widget in frame_grafico.winfo_children():
        widget.destroy()

    columnas = ['pm25', 'pm10', 'no', 'no2', 'nox', 'ozono', 'so2']
    medias_dict = {}

    for columna in columnas:
        frame_filtrado = frame2[(frame2[columna] > 0) & (frame2[columna] < 1100)]
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

# def mostrar_dataframe(frame2, frame_grafico):
#     tema_actual = darkdetect.theme()

#     estilo = ttk.Style()
#     if tema_actual == "Dark":
#         estilo.theme_use("clam")
#         estilo.configure(
#             "Treeview",
#             background="#2d2d2d",
#             foreground="white",
#             fieldbackground="#2d2d2d",
#         )
#         estilo.configure(
#             "Treeview.Heading",
#             background="#3d3d3d",
#             foreground="white",
#         )
#     else:
#         estilo.theme_use("default")
#         estilo.configure(
#             "Treeview",
#             background="white",
#             foreground="black",
#             fieldbackground="white",
#         )
#         estilo.configure(
#             "Treeview.Heading",
#             background="#f0f0f0",
#             foreground="black",
#         )

#     for widget in frame_grafico.winfo_children():
#         widget.destroy()

#     tree = ttk.Treeview(frame_grafico)

#     tree["columns"] = ["Índice"] + list(frame2.columns)
#     tree["show"] = "headings"

#     tree.heading("Índice", text="Índice")
#     tree.column("Índice", width=100, anchor="center")
#     for column in frame2.columns:
#         tree.heading(column, text=column)
#         tree.column(column, width=100, anchor="center")

#     for index, row in frame2.head(40).iterrows():
#         tree.insert("", "end", values=[index] + list(row))

#     tree.pack(fill="both", expand=True)

# import numpy as np
# import pandas as pd
# import regex as rg
# import matplotlib.pyplot as plt
# from database_info import data
# import glob
# import os

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# import darkdetect
# import tkinter as tk
# from tkinter import ttk
# import sv_ttk
try:
    import ttkbootstrap as tb
    TTKBOOTSTRAP_AVAILABLE = True
except ImportError:
    TTKBOOTSTRAP_AVAILABLE = False
    print("ttkbootstrap no está instalado. Se usarán los temas de Tkinter por defecto.")

def mostrar_dataframe(frame2, frame_grafico):
    tema_actual = darkdetect.theme()

    estilo = tb.Style()

    if TTKBOOTSTRAP_AVAILABLE:
        if tema_actual == "Dark":
            try:
                estilo.theme_use("darkly")  # Un tema oscuro de ttkbootstrap
            except tk.TclError:
                print("El tema 'darkly' de ttkbootstrap no está disponible. Usando tema por defecto.")
                estilo.theme_use("clam") # Clam es más compatible con temas oscuros en Tkinter
                estilo.configure("Treeview", background="#2d2d2d", foreground="white", fieldbackground="#2d2d2d")
                estilo.configure("Treeview.Heading", background="#3d3d3d", foreground="white")
        else:
            try:
                estilo.theme_use("flatly") # Un tema claro de ttkbootstrap
            except tk.TclError:
                print("El tema 'flatly' de ttkbootstrap no está disponible. Usando tema por defecto.")
                estilo.theme_use("default")
                estilo.configure("Treeview", background="white", foreground="black", fieldbackground="white")
                estilo.configure("Treeview.Heading", background="#f0f0f0", foreground="black")
    else:
        # Código original para temas de Tkinter por defecto
        if tema_actual == "Dark":
            estilo.theme_use("clam")
            estilo.configure("Treeview", background="#2d2d2d", foreground="white", fieldbackground="#2d2d2d")
            estilo.configure("Treeview.Heading", background="#3d3d3d", foreground="white")
        else:
            estilo.theme_use("default")
            estilo.configure("Treeview", background="white", foreground="black", fieldbackground="white")
            estilo.configure("Treeview.Heading", background="#f0f0f0", foreground="black")

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