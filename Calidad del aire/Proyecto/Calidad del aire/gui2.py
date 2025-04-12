import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys
from database_info import data
from all_stations import all
from all_stations import mostrar_dataframe
from per_station import mostrar_grafico_est
from per_station import mostrar_dataframe_est
from vent_all import ventana2
from vent_est import ventana3
from vent_lim import ventana4
from vent_ind import ventana5
from tema import apply_theme_to_titlebar_dinamico
from tema import windows_theme_dinamico
import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os

path=r'Calidad del aire\Proyecto\Bases'

frame2=data(path)

def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Análisis calidad del aire de Medellín")
    ventana.geometry("1126x634")

    fuente_titulo = ("Arial", 20, "bold")
    fuente_texto = ("Arial", 16, "bold")
    fuente_descripcion = ("Arial", 14)

    frame_derecho = ttk.Frame(ventana)
    frame_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    titulo = ttk.Label(frame_derecho, text="Calidad del aire", font=fuente_titulo)
    titulo.pack(pady=10)

    nombres = ttk.Label(
        frame_derecho,
        text="Juan Diego Suárez Agualimpia \nIngeniero Químico \nUniversidad Nacional de Colombia",
        font=fuente_texto,
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

    frame_izquierdo = ttk.Frame(ventana)
    frame_izquierdo.place(x=10, y=100, width=200, height=500)
    frame_izquierdo.pack_propagate(False)

    frame_izquierdo.place_forget()

    botones = [
        "Todas las estaciones",
        "Análisis por estación",
        "Valores límites diarios",
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
            frame_izquierdo.place(x=10, y=140, width=200, height=500)

    boton_menu = ttk.Button(ventana, text="Menú", command=toggle_menu)
    boton_menu.place(x=10, y=10)

    def manejar_evento(evento):
        if evento == "Cancelar":
            ventana.destroy()
        elif evento == "Todas las estaciones":
            ventana2(ventana,frame2)
        elif evento == "Análisis por estación":
            ventana3(ventana,frame2)
        elif evento == "Valores límites diarios":
            ventana4(ventana)
        elif evento == "Índice parcial y global horario":
            ventana5(ventana)

    windows_theme_dinamico(ventana)
    apply_theme_to_titlebar_dinamico(ventana)

    ventana.mainloop()

ventana_principal()