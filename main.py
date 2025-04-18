from aire.proyecto.calidad.master import maestro
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys
from aire.proyecto.calidad.database_info import data
from aire.proyecto.calidad.database_info import coord
from aire.proyecto.calidad.all_stations import all
from aire.proyecto.calidad.all_stations import mostrar_dataframe
from aire.proyecto.calidad.per_station import mostrar_grafico_est
from aire.proyecto.calidad.per_station import mostrar_dataframe_est
from aire.proyecto.calidad.vent_all import ventana2
from aire.proyecto.calidad.vent_est import ventana3
from aire.proyecto.calidad.vent_lim import ventana5
from aire.proyecto.calidad.vent_map import ventana4
from aire.proyecto.calidad.adj_ven import centro
from aire.proyecto.calidad.tema import apply_theme_to_titlebar_dinamico
from aire.proyecto.calidad.tema import windows_theme_dinamico
import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os

app = maestro()
app.mainloop()