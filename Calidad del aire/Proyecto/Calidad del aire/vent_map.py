import tkintermapview
import pandas as pd
from database_info import coord
from tema import apply_theme_to_titlebar_dinamico
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


def ventana4(parent, coordenadas):

    columnas = ['Estacion', 'Longitud', 'Latitud', 'Ciudad']
    Cities = ['Medellin', 'Medellín']

    vent_map = tk.Toplevel()
    vent_map.title("Mapa de estaciones y fuentes de contaminacion")

    map_widget = tkintermapview.TkinterMapView(vent_map, width=1126, height=634)
    map_widget.pack(fill="both", expand=True)

    map_widget.set_position(6.25256, -75.56958)
    map_widget.set_zoom(14)

    markers = {}

    def marker_clicked(marker):
        if marker.text == "":
            estacion_nombre = markers[marker]
            marker.set_text(estacion_nombre)
        else:
            marker.set_text("")

    fr = {}
    for city in Cities:
        coord2 = coordenadas.loc[coordenadas['Ciudad'] == city, columnas]
        fr[city] = coord2
        for i, row in coord2.iterrows():
            marker = map_widget.set_marker(
                row['Latitud'],
                row['Longitud'],
                text="",
                marker_color_circle="black",
                marker_color_outside="darkblue",
                command=marker_clicked
            )
            markers[marker] = row['Estacion']

    apply_theme_to_titlebar_dinamico(vent_map)
    # vent_map.mainloop()