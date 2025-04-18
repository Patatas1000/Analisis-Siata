import tkinter as tk
import tkintermapview
import pandas as pd
from database_info import coord

# Obtener las coordenadas desde la base de datos
path2 = r'C:\Users\ivans\OneDrive\Desktop\Juan\Analisis-Siata\Calidad del aire\Proyecto\Estaciones'
coordenadas = coord(path2)

columnas = ['Estacion', 'Longitud', 'Latitud', 'Ciudad']
Cities = ['Medellin', 'Medellín']

# Crear ventana principal
root = tk.Tk()
root.title("Mapa con TkinterMapView")

# Crear widget de mapa
map_widget = tkintermapview.TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Establecer posición inicial del mapa
map_widget.set_position(6.25256, -75.56958)
map_widget.set_zoom(12)

# Agregar marcadores basados en los datos de la base
fr = {}
for city in Cities:
    coord2 = coordenadas.loc[coordenadas['Ciudad'] == city, columnas]
    fr[city] = coord2
    for i, row in coord2.iterrows():
        marker = map_widget.set_marker(row['Latitud'], row['Longitud'], text=row['Estacion'])

# Ejecutar la ventana
root.mainloop()

# import tkinter as tk
# import tkintermapview
# import pandas as pd
# from database_info import coord
# import math

# # Obtener coordenadas desde la base de datos
# path2 = r'C:\Users\ivans\OneDrive\Desktop\Juan\Analisis-Siata\Calidad del aire\Proyecto\Estaciones'
# coordenadas = coord(path2)

# columnas = ['Estacion', 'Longitud', 'Latitud', 'Ciudad']
# Cities = ['Medellin', 'Medellín']

# # Crear ventana principal
# root = tk.Tk()
# root.title("Mapa con TkinterMapView")

# # Crear widget de mapa
# map_widget = tkintermapview.TkinterMapView(root, width=800, height=600)
# map_widget.pack(fill="both", expand=True)

# # Establecer posición inicial
# map_widget.set_position(6.25256, -75.56958)
# map_widget.set_zoom(12)

# # Crear etiqueta para mostrar nombres al interactuar
# info_label = tk.Label(root, text="", font=("Arial", 12))
# info_label.pack()

# # Función para mostrar el nombre al interactuar con el marcador
# def mostrar_nombre(nombre):
#     info_label.config(text=nombre)

# # Función para dibujar un círculo (polígono) de 2 km de radio
# def dibujar_circulo(lat, lon, radio_km=2, puntos=40):
#     coords = []
#     radio_grados = radio_km / 111.32  # Aproximación para convertir km a grados
#     for i in range(puntos):
#         angulo = (2 * math.pi / puntos) * i
#         lat_p = lat + (radio_grados * math.cos(angulo))
#         lon_p = lon + (radio_grados * math.sin(angulo))
#         coords.append((lat_p, lon_p))
#     map_widget.set_polygon(coords, outline_color="blue", fill_color="blue")

# # Agregar marcadores y círculos
# fr = {}
# for city in Cities:
#     coord2 = coordenadas.loc[coordenadas['Ciudad'] == city, columnas]
#     fr[city] = coord2
#     for i, row in coord2.iterrows():
#         marker = map_widget.set_marker(row['Latitud'], row['Longitud'])
#         marker.command = lambda nombre=row['Estacion']: mostrar_nombre(nombre)  # Mostrar nombre al interactuar
#         dibujar_circulo(row['Latitud'], row['Longitud'])  # Dibujar el círculo de 2 km

# # Ejecutar ventana
# root.mainloop()