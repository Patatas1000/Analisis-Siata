import tkintermapview
import pandas as pd
from database_info import coord
from tema import apply_theme_to_titlebar_dinamico
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


def ventana4(parent,coordenadas):

    # path2 = r'Calidad del aire\Proyecto\Estaciones'
    # coordenadas = coord(path2)

    columnas = ['Estacion', 'Longitud', 'Latitud', 'Ciudad']
    Cities = ['Medellin', 'Medellín']

    vent_map = tk.Toplevel()
    vent_map.title("Mapa de estaciones y fuentes de contaminacion")

    map = tkintermapview.TkinterMapView(vent_map, width=800, height=600)
    map.pack(fill="both", expand=True)

    map.set_position(6.25256, -75.56958)
    map.set_zoom(12)

    fr = {}
    for city in Cities:
        coord2 = coordenadas.loc[coordenadas['Ciudad'] == city, columnas]
        fr[city] = coord2
        for i, row in coord2.iterrows():
            marker = map.set_marker(row['Latitud'], row['Longitud'], text=row['Estacion'], marker_color_circle="black", marker_color_outside="darkblue",)
    apply_theme_to_titlebar_dinamico(vent_map)
    vent_map.mainloop()