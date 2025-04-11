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
import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os

path=r'Calidad del aire\Proyecto\Bases'

frame2=data(path)

def apply_theme_to_titlebar_dinamico(ventana):
    timer_id = None

    def actualizar_titulo():
        nonlocal timer_id
        if not ventana.winfo_exists():
            return

        tema_actual = darkdetect.theme().lower()

        version = sys.getwindowsversion()
        if version.major == 10 and version.build >= 22000:
            pywinstyles.change_header_color(ventana, "#1c1c1c" if tema_actual == "dark" else "#fafafa")
        elif version.major == 10:
            pywinstyles.apply_style(ventana, "dark" if tema_actual == "dark" else "normal")
            
            ventana.wm_attributes("-alpha", 0.99)
            ventana.wm_attributes("-alpha", 1)

        timer_id = ventana.after(1000, actualizar_titulo)

    def on_close():
        nonlocal timer_id
        if timer_id:
            ventana.after_cancel(timer_id)
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", on_close)

    actualizar_titulo()

def windows_theme_dinamico(ventana):
    def actualizar_tema():
        nuevo_tema = darkdetect.theme().lower()

        if sv_ttk.get_theme() != nuevo_tema:
            sv_ttk.set_theme(nuevo_tema)

        ventana.after(1000, actualizar_tema)

    actualizar_tema()

def ventana2(parent):
    ventana2 = tk.Toplevel(parent)
    ventana2.title('Análisis de datos en todas las estaciones')
    ventana2.geometry("1600x900")

    fuente_titulo = ("Arial", 20, "bold")
    fuente_texto = ("Arial", 16, "bold")
    fuente_descripcion = ("Arial", 14)

    frame_derecho2 = ttk.Frame(ventana2)
    frame_derecho2.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    titulo = ttk.Label(frame_derecho2, text="En esta ventana puede revisar el gráfico de los valores diarios promedio para todos los contaminantes en todas las estaciones en la base de datos, además también puede visualizar las primeras 40 filas de los datos utilizados en este análisis, usando los botones para mostrar el gráfico y los datos respectivamente.", font=fuente_descripcion, wraplength=1100, justify="left")
    titulo.pack(pady=10)

    frame_grafico = ttk.Frame(frame_derecho2)
    frame_grafico.pack(pady=20, fill="both", expand=True)

    frame_izquierdo = ttk.Frame(ventana2)
    frame_izquierdo.place(x=10, y=100, width=200, height=500)
    frame_izquierdo.pack_propagate(False)

    frame_izquierdo.place_forget()

    botones = [
        ("Mostrar gráfico"),
        ("Mostrar datos"),
        ("Cancelar")
    ]

    def manejar_evento2(evento):
        if evento == "Cancelar":
            ventana2.destroy()
        elif evento == "Mostrar gráfico":
            all(frame2, frame_grafico)
        elif evento == "Mostrar datos":
            mostrar_dataframe(frame2, frame_grafico)

    for texto in botones:
        boton = ttk.Button(
            frame_izquierdo,
            text=texto,
            width=20,
            command=lambda t=texto: manejar_evento2(t),
        )
        boton.pack(pady=10) 

    def toggle_menu():
        if frame_izquierdo.winfo_ismapped():
            frame_izquierdo.place_forget()
        else:
            frame_izquierdo.place(x=10, y=60, width=200, height=160)

    boton_menu = ttk.Button(ventana2, text="Menú", command=toggle_menu)
    boton_menu.place(x=10, y=10)

    texto_cancelar = ttk.Label(
        frame_derecho2,
        text="\nPresione Cancelar para salir del programa",
        font=fuente_descripcion,
    )
    texto_cancelar.pack(pady=10)

    windows_theme_dinamico(ventana2)
    apply_theme_to_titlebar_dinamico(ventana2)

    ventana2.protocol("WM_DELETE_WINDOW", ventana2.destroy)

def ventana3(parent):
    ventana3 = tk.Toplevel(parent)
    ventana3.title('Análisis de datos en todas las estaciones')
    ventana3.geometry("1600x900")

    fuente_titulo = ("Arial", 20, "bold")
    fuente_texto = ("Arial", 16, "bold")
    fuente_descripcion = ("Arial", 14)

    titulo = ttk.Label(ventana3, text="Seleccione una estación para analizar los datos diarios promedio de los contaminantes. Use los botones para mostrar el gráfico o los datos correspondientes.", font=fuente_descripcion, wraplength=1100, justify="left")
    titulo.pack(pady=10)

    id_estaciones = sorted(frame2['codigoSerial'].unique())
    estacion_seleccionada = tk.StringVar(value=id_estaciones[0])

    combobox = ttk.Combobox(ventana3, textvariable=estacion_seleccionada, values=id_estaciones, state="readonly", font=fuente_texto)
    combobox.pack(pady=10)

    frame_contenido = ttk.Frame(ventana3)
    frame_contenido.pack(pady=20, fill="both", expand=True)

    frame_botones = ttk.Frame(ventana3)
    frame_botones.pack(pady=10)

    botones = [
        ("Mostrar gráfico"),
        ("Mostrar datos"),
        ("Cancelar")
    ]

    def manejar_evento3(evento):
        id_estacion = estacion_seleccionada.get()

        if evento == "Cancelar":
            ventana3.destroy()
        elif evento == "Mostrar gráfico":
            frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)]
            mostrar_grafico_est(frame_filtrado, frame_contenido)
        elif evento == "Mostrar datos":
            frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)]
            mostrar_dataframe_est(frame_filtrado, frame_contenido)

    for texto in botones:
        boton = ttk.Button(
            frame_botones,
            text=texto,
            width=20,
            command=lambda t=texto: manejar_evento3(t),
        )
        boton.pack(side="left", padx=5)

    texto_cancelar = ttk.Label(
        ventana3,
        text="Presione Cancelar para salir de la ventana",
        font=fuente_descripcion,
    )
    texto_cancelar.pack(pady=10)
    windows_theme_dinamico(ventana3)
    apply_theme_to_titlebar_dinamico(ventana3)

def ventana4():
    new_window = tk.Toplevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')

def ventana5():
    new_window = tk.Toplevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')

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
        text="Reducción de los contaminantes del aire a través de purificadores.",
        font=fuente_texto,
    )
    titulo_desc.pack(pady=10)

    descripcion = ttk.Label(
        frame_derecho,
        text=(
            "Los purificadores de aire han sido desarrollados a medida que la tecnología y la contaminación ha avanzado; con el fin de reducir los compuestos químicos que contaminan y están presentes en el aire se realizan mediciones y, dados los valores obtenidos, se puede saber qué índice de contaminación está presente en tiempo real y qué tipo de alternativa de purificación se puede utilizar para combatirlo.\nEn los dataframes pueden aparecer valores de -9999 o excesivamente altos, para algunos de los contaminantes, indicando que no se hizo la medición en ese tiempo, o que se trata de una medición errada, estos datos se filtran de manera automática al realizar las gráficas"
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
        "Índice parcial horario",
        "Índice global horario",
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
            ventana2(ventana)
        elif evento == "Análisis por estación":
            ventana3(ventana)
        elif evento == "Índice parcial horario":
            ventana4()
        elif evento == "Índice global horario":
            ventana5()

    windows_theme_dinamico(ventana)
    apply_theme_to_titlebar_dinamico(ventana)

    ventana.mainloop()

ventana_principal()