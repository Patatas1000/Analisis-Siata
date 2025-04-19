import tkinter as tk
import ttkbootstrap as tb
# from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage
from tkinter import font
import sv_ttk
import darkdetect
import pywinstyles, sys
from .database_info import data
from .database_info import coord
from .all_stations import all
from .all_stations import mostrar_dataframe
from .per_station import mostrar_grafico_est
from .per_station import mostrar_dataframe_est
from .adj_ven import centro
from .tema import apply_theme_to_titlebar_dinamico
from .tema import windows_theme_dinamico
import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os

class maestro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ventana_principal()
        self.marcos()
        self.top()

    def ventana_principal(self):

        path=r'aire\proyecto\bases'
        path2=r'aire\proyecto\estaciones'

        frame2=data(path)
        coordenadas = coord(path2)

        # ventana = tk.Tk()
        self.title("Análisis calidad del aire de Medellín")
        # ventana.geometry("1126x634")

        w , h = 1126 , 634

        centro(self, w, h)

        apply_theme_to_titlebar_dinamico(self)
        if darkdetect.theme().lower() == "dark":
            tb.Window(themename="darkly")
        else:
            tb.Window(themename="flatly")
        
        # windows_theme_dinamico(self)  
        # sv_ttk.set_theme(darkdetect.theme())

    def marcos(self):

        self.frame1 = tk.Frame(self, height=50)
        self.frame1.pack(side=tk.TOP, fill='both')

        self.frame2 = tk.Frame(self)
        self.frame2.pack(side=tk.RIGHT, fill='both', expand=True)

        # self.frame3 = ttk.Frame(self, width=200)
        # self.frame3.pack(side=tk.LEFT, fill='both', expand=False)

        self.menu_frame = tb.Frame(self, bootstyle="dark", width=0, height=600)
        self.menu_frame.place(x=0, y=0)

        # self.frame4 = tk.Frame(self.frame2, bg="#000080")
        # self.frame4.pack(side=tk.TOP, fill='both', expand=True)

        # self.frame5 = tk.Frame(self.frame2, bg="#00ff00", height=40)
        # self.frame5.pack(side=tk.BOTTOM, fill='both', expand=False)

    def top(self):

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)
        font_awesome=font.Font(family='FontAwesome', size=12)

        self.frame4 = tk.Frame(self.frame1, width=10)
        self.frame4.pack(side=tk.LEFT, fill='both', expand=False)

        self.frame5 = tk.Frame(self.frame1)
        self.frame5.pack(side=tk.RIGHT, fill='both', expand=True)

        self.titulo = tk.Label(self.frame5,text="Análsis de los datos provenientes del SIATA",font=fuente_texto)
        self.titulo.pack()

        # self.menu = tk.Button(self.frame4, text="Menú", width=8)
        # self.menu.pack()

        self.menu_visible = False
        self.menu_width = 200

        self.toggle_btn = tk.Button(self, text="☰", font=("Arial", 16), command=self.toggle_menu)
        self.toggle_btn.place(x=10, y=10)

    def menu(self):
        self.frames = {"Inicio",
                       "Perfil",
                       "Configuración",
                       "Salir"
                       }

        # Botones del menú
        opciones = list(self.frames)
        for i, texto in enumerate(opciones):
            btn = tb.Button(self.menu_frame, text=texto, bootstyle="secondary", width=20,
                            command=lambda name=texto: self.mostrar_frame(name))
            btn.place(x=10, y=60 + i * 60, height=40)

    def toggle_menu(self):
        if self.menu_visible:
            self.ocultar_menu()
        else:
            self.mostrar_menu()

    def mostrar_menu(self):
        for w in range(0, self.menu_width + 1, 20):
            self.menu_frame.config(width=w)
            self.menu_frame.update()
        self.menu_visible = True

    def ocultar_menu(self):
        for w in range(self.menu_width, -1, -20):
            self.menu_frame.config(width=w)
            self.menu_frame.update()
        self.menu_visible = False