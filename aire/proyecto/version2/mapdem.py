import tkinter as tk
from tkinter import ttk
import tkintermapview
import pandas as pd
import geopandas as gpd # Importamos geopandas
from shapely.geometry import Polygon, MultiPolygon # Importamos los tipos de geometría

ruta_med=r'aire\proyecto\mdgeo\medellin.geojson'

def data_geojson(ruta_geojson):
    """Lee un archivo GeoJSON y devuelve un GeoDataFrame."""
    try:
        gdf = gpd.read_file(ruta_geojson)
        return gdf
    except Exception as e:
        print(f"Error al leer el archivo GeoJSON: {e}")
        return None

def poligono(geometria):
    """Extrae coordenadas (lat, lon) de Polygon o MultiPolygon."""
    coordenadas = []
    if geometria.geom_type == 'Polygon':
        exterior_coords = list(geometria.exterior.coords)
        coordenadas.append([(lat, lon) for lon, lat in exterior_coords])
        for interior in geometria.interiors:
            interior_coords = list(interior.coords)
            coordenadas.append([(lat, lon) for lon, lat in interior_coords])
    elif geometria.geom_type == 'MultiPolygon':
        for polygon in geometria.geoms:
            exterior_coords = list(polygon.exterior.coords)
            coordenadas.append([(lat, lon) for lon, lat in exterior_coords])
            for interior in polygon.interiors:
                interior_coords = list(interior.coords)
                coordenadas.append([(lat, lon) for lon, lat in interior_coords])
    return coordenadas
