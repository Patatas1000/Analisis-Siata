import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys
from database_info import data
from database_info import coord
from all_stations import all
from all_stations import mostrar_dataframe
from per_station import mostrar_grafico_est
from per_station import mostrar_dataframe_est
from vent_all import ventana2
from vent_est import ventana3
from vent_lim import ventana5
from vent_map import ventana4
from adj_ven import centro
from tema import apply_theme_to_titlebar_dinamico
from tema import windows_theme_dinamico
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

    # def data(path):

    #     all_files = glob.glob(os.path.join(path + "/*.csv"))

    #     data = []

    #     for filename in all_files:
    #         df = pd.read_csv(filename, index_col=None, header=0)
    #         data.append(df)

    #     frame = pd.concat(data, axis=0, ignore_index=True)
    #     frame[['Fecha', 'Hora']] = frame['Fecha_Hora'].str.split(' ', n=1, expand=True)
    #     frame.insert(0, 'Fecha', frame.pop('Fecha'))
    #     frame.insert(1, 'Hora', frame.pop('Hora'))
    #     frame.pop('Fecha_Hora')
    #     frame.set_index('Fecha', inplace=True)
    #     frame.index = pd.to_datetime(frame.index, format='%Y-%m-%d')
    #     drop=['calidad_pm1', 'pm1', 'calidad_pm10', 'calidad_pm25', 'calidad_no',
    #         'calidad_no2', 'calidad_nox','calidad_ozono', 'co','calidad_co', 'calidad_so2', 'pst', 'calidad_pst',
    #         'dviento_ssr', 'calidad_dviento_ssr', 'haire10_ssr', 'calidad_haire10_ssr', 'p_ssr', 'calidad_p_ssr',
    #         'pliquida_ssr', 'calidad_pliquida_ssr', 'rglobal_ssr', 'calidad_rglobal_ssr', 'taire10_ssr', 'calidad_taire10_ssr', 'vviento_ssr', 'calidad_vviento_ssr']
    #     frame2=frame.drop(columns=drop, axis=1)
    #     return(frame2)

    # # path2 = r'Calidad del aire\Proyecto\Estaciones'
    # # path2= r'C:\Users\ivans\OneDrive\Desktop\Juan\Analisis-Siata\Calidad del aire\Proyecto\Estaciones'
    # def coord(path2):

    #     estaciones = pd.read_csv(path2 + '/Estaciones_CalidadAire.txt', sep=";")
    #     estaciones.set_index('Codigo', inplace=True)
    #     return(estaciones)

    def ventana_principal(self):

        path=r'Calidad del aire\Proyecto\Bases'
        path2=r'Calidad del aire\Proyecto\Estaciones'

        frame2=data(path)
        coordenadas = coord(path2)

        # ventana = tk.Tk()
        self.title("Análisis calidad del aire de Medellín")
        # ventana.geometry("1126x634")

        w , h = 1126 , 634

        centro(self, w, h)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame_derecho = ttk.Frame(self)
        frame_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        titulo = ttk.Label(frame_derecho, text="Calidad del aire", font=fuente_titulo)
        titulo.pack(pady=10)

        nombres = ttk.Label(
            frame_derecho,
            text="Juan Diego Suárez Agualimpia \nIngeniero Químico \nUniversidad Nacional de Colombia",
            font=fuente_texto,justify="center"
        )
        nombres.pack(pady=10)

        titulo_desc = ttk.Label(
            frame_derecho,
            text="Análsis de los datos provenientes del SIATA",
            font=fuente_texto,
        )
        titulo_desc.pack(pady=10)

        descripcion = ttk.Label(
            frame_derecho,
            text=(
                "El Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA) es un sistema que busca prevenir y mitigar los efectos de la contaminación del aire en la región. Este análisis se centra en los datos recopilados por el SIATA, que incluyen información sobre la calidad del aire, las condiciones meteorológicas y otros factores relevantes. El objetivo es proporcionar una visión general de la calidad del aire en Medellín y su evolución a lo largo del tiempo."
            ),
            font=fuente_descripcion,
            wraplength=700,
            justify="left",
        )
        descripcion.pack(pady=20)

        frame_izquierdo = ttk.Frame(self)
        frame_izquierdo.place(x=10, y=100, width=200, height=500)
        frame_izquierdo.pack_propagate(False)

        frame_izquierdo.place_forget()

        botones = [
            "Todas las estaciones",
            "Análisis por estación",
            "Mapa estaciones",
            "Índice parcial y global horario",
            "Cancelar",
        ]

        for texto in botones:
            boton = ttk.Button(
                frame_izquierdo,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento(t),
            )
            boton.pack(pady=10)

        def toggle_menu():
            if frame_izquierdo.winfo_ismapped():
                frame_izquierdo.place_forget()
            else:
                frame_izquierdo.place(x=0, y=140, width=200, height=1080)

        boton_menu = ttk.Button(self, text="Menú", command=toggle_menu)
        boton_menu.place(x=10, y=10)

        def manejar_evento(evento):
            if evento == "Cancelar":
                self.destroy()
            elif evento == "Todas las estaciones":
                ventana2(self,frame2)
            elif evento == "Análisis por estación":
                ventana3(self,frame2,coordenadas)
            elif evento == "Mapa estaciones":
                ventana4(self,coordenadas)
            elif evento == "Índice de calidad del aire":
                ventana5(self)

        windows_theme_dinamico(self)
        apply_theme_to_titlebar_dinamico(self)