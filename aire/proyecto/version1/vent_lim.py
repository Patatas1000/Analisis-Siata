import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys
from per_station import mostrar_grafico_est
from per_station import mostrar_dataframe_est
from tema import apply_theme_to_titlebar

def ventana5(parent):
    new_window = tk.Toplevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')
