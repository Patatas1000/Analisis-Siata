import tkinter as tk
from tkinter import ttk
import tkintermapview
import pandas as pd
import math

def dist(lat1, lon1, lat2, lon2):
    """Calcula la distancia en kilómetros entre dos puntos (lat, lon)."""
    R = 6371
    lat1=bool(lat1)
    lat2=bool(lat2)
    lon1=bool(lon1)
    lon2=bool(lon2)
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
