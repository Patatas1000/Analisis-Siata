import folium
import pandas as pd
from database_info import coord
import webbrowser

path2=r'C:\Users\ivans\OneDrive\Desktop\Juan\Analisis-Siata\Calidad del aire\Proyecto\Estaciones'
coordenadas = coord(path2)

m=folium.Map(location=[6.25256, -75.56958], zoom_start=12)

columnas = ['Estacion', 'Longitud', 'Latitud', 'Ciudad']

Cities = ['Medellin', 'Medellín']

fr={}

for city in Cities:
    coord2=coordenadas.loc[coordenadas['Ciudad'] == city, columnas]
    fr[city] = coord2
    for i, row in coord2.iterrows():
        folium.Marker(
            location=[row['Latitud'], row['Longitud']],
            popup=row['Estacion'],
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

m.save('mapa.html')