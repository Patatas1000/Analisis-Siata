import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys
from tema import apply_theme_to_titlebar_dinamico


def ventana5(parent):
    new_window = tk.Toplevel()
    new_window.title('Mapa de estaciones y fuentes de contaminacion')