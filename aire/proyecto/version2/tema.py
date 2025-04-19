import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import ttkbootstrap as tb
import sv_ttk
import darkdetect
import pywinstyles, sys

def apply_theme_to_titlebar(ventana):
    tema_actual = darkdetect.theme().lower()

    version = sys.getwindowsversion()
    if version.major == 10 and version.build >= 22000:
        try:
            pywinstyles.change_header_color(ventana, "#1c1c1c" if tema_actual == "dark" else "#fafafa")
        except Exception as e:
            print(f"Error al cambiar el color del encabezado (Windows 11+): {e}")
    elif version.major == 10:
        try:
            pywinstyles.apply_style(ventana, "dark" if tema_actual == "dark" else "normal")
            ventana.wm_attributes("-alpha", 0.99)
            ventana.wm_attributes("-alpha", 1)
        except Exception as e:
            print(f"Error al aplicar estilo a la ventana (Windows 10): {e}")

def window_theme(ventana):
    
    if darkdetect.theme().lower() == "dark":
        tb.Style("darkly")
    else:
        tb.Style("flatly")