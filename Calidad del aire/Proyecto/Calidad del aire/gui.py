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
import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os

path=r'Calidad del aire\Proyecto\Bases'

frame2=data(path)

def apply_theme_to_titlebar_dinamico(ventana):
    # Almacenar ID del timer de after para cancelarlo posteriormente
    timer_id = None

    def actualizar_titulo():
        nonlocal timer_id  # Declarar la variable como no local
        if not ventana.winfo_exists():
            return  # No hacer nada si la ventana ha sido destruida

        # Detectar el tema del sistema
        tema_actual = darkdetect.theme().lower()

        version = sys.getwindowsversion()
        if version.major == 10 and version.build >= 22000:
            # Cambiar el color de la barra del título en Windows 11
            pywinstyles.change_header_color(ventana, "#1c1c1c" if tema_actual == "dark" else "#fafafa")
        elif version.major == 10:
            pywinstyles.apply_style(ventana, "dark" if tema_actual == "dark" else "normal")

            # "Hack" para actualizar el color de la barra del título en Windows 10
            ventana.wm_attributes("-alpha", 0.99)
            ventana.wm_attributes("-alpha", 1)

        # Programar otra verificación en 1000 ms (1 segundo)
        timer_id = ventana.after(1000, actualizar_titulo)

    def on_close():
        nonlocal timer_id
        if timer_id:
            ventana.after_cancel(timer_id)  # Cancelar el timer programado
        ventana.destroy()  # Destruir la ventana

    # Configurar el protocolo de cierre de la ventana
    ventana.protocol("WM_DELETE_WINDOW", on_close)

    # Comenzar la verificación periódica
    actualizar_titulo()

def windows_theme_dinamico(ventana):
    def actualizar_tema():
        # Detectar el tema del sistema
        nuevo_tema = darkdetect.theme().lower()

        # Cambiar el tema de la ventana si es diferente
        if sv_ttk.get_theme() != nuevo_tema:
            sv_ttk.set_theme(nuevo_tema)

        # Programar otra verificación en 1000 ms (1 segundo)
        ventana.after(1000, actualizar_tema)

    # Comenzar la verificación periódica
    actualizar_tema()

def ventana2(parent):
    ventana2 = tk.Toplevel(parent)  # Ventana secundaria ligada a la principal
    ventana2.title('Análisis de datos en todas las estaciones')
    ventana2.geometry("1200x800")  # Ajustar el tamaño de la ventana

    # Configuración de fuentes
    fuente_titulo = ("Arial", 20, "bold")
    fuente_texto = ("Arial", 16, "bold")
    fuente_descripcion = ("Arial", 14)

    # Título
    titulo = ttk.Label(ventana2, text="Calidad del aire", font=fuente_descripcion)
    titulo.pack(pady=10)

    # Crear área para el gráfico
    frame_grafico = ttk.Frame(ventana2)
    frame_grafico.pack(pady=20, fill="both", expand=True)

    # Botones
    frame_botones = ttk.Frame(ventana2)
    frame_botones.pack(pady=10)

    botones = [
        ("Gráfico de promedio\ndiario"),
        ("Mostrar parte del\ndataframe"),
        ("Cancelar\n")
    ]

    # Función para manejar eventos
    def manejar_evento2(evento):
        if evento == "Cancelar\n":
            ventana2.destroy()  # Usar `parent` en lugar de `ventana`
        elif evento == "Gráfico de promedio\ndiario":
            all(frame2, frame_grafico)
        # elif evento == "Gráfico de promedio\ndiario":
        #     all(frame2)  # Llamar a la función `all` con frame2
        elif evento == "Mostrar parte del\ndataframe":
            mostrar_dataframe(frame2, frame_grafico)  # Llama a la función para mostrar el DataFrame

    # Crear botones y asociar manejar_evento2
    for texto in botones:
        boton = ttk.Button(
            frame_botones,
            text=texto,
            width=20,
            command=lambda t=texto: manejar_evento2(t),
        )
        boton.pack(side="left", padx=5)

    # Texto para salir
    texto_cancelar = ttk.Label(
        ventana2,  # Cambiado a ventana2
        text="\nPresione Cancelar para salir del programa",
        font=fuente_descripcion,
    )
    texto_cancelar.pack(pady=10)

    # Aplicar el tema después de inicializar ventana2
    windows_theme_dinamico(ventana2)
    apply_theme_to_titlebar_dinamico(ventana2)

    # Asegurar que ventana2 se cierre adecuadamente
    ventana2.protocol("WM_DELETE_WINDOW", ventana2.destroy)

def ventana3():
    new_window = tk.Toplevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')

def ventana4():
    new_window = tk.Toplevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')

def ventana5():
    new_window = tk.Toplevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')

def ventana_principal():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Análisis calidad del aire de Medellín")
    ventana.geometry("1200x700")  # Ajustar el tamaño de la ventana

    # Configuración de fuentes
    fuente_titulo = ("Arial", 20, "bold")
    fuente_texto = ("Arial", 16, "bold")
    fuente_descripcion = ("Arial", 14)

    # Título
    titulo = ttk.Label(ventana, text="Calidad del aire", font=fuente_titulo)
    titulo.pack(pady=10)

    # Nombres
    nombres = ttk.Label(
        ventana,
        text="Juan Diego Suárez Agualimpia \nIngeniero Químico \nUniversidad Nacional de Colombia",
        font=fuente_texto,
    )
    nombres.pack(pady=10)

    titulo_desc = ttk.Label(
        ventana,
        text="Reducción de los contaminantes del aire a través de purificadores.",
        font=fuente_texto,
    )
    titulo_desc.pack(pady=10)

    # Descripción
    descripcion = ttk.Label(
        ventana,
        text=(
            "Los purificadores de aire han sido desarrollados a medida que la tecnología y la contaminación ha avanzado; con el fin de reducir los compuestos químicos que contaminan y están presentes en el aire se realizan mediciones y, dados los valores obtenidos, se puede saber qué índice de contaminación está presente en tiempo real y qué tipo de alternativa de purificación se puede utilizar para combatirlo."
        ),
        font=fuente_descripcion,
        wraplength=1100,  # Ajustar el texto
        justify="left",
    )
    descripcion.pack(pady=20)

    # # Imagen
    # ruta_imagen = r"Calidad del aire\Proyecto\UdeA1.gif"  # Cambia esta ruta a tu archivo
    # try:
    #     imagen = PhotoImage(file=ruta_imagen)
    #     etiqueta_imagen = tk.Label(ventana, image=imagen)
    #     etiqueta_imagen.pack(pady=10)
    # except tk.TclError:
    #     etiqueta_imagen = tk.Label(
    #         ventana, text="No se pudo cargar la imagen.", font=fuente_descripcion
    #     )
    #     etiqueta_imagen.pack(pady=10)

    # Indicaciones
    texto_opciones = ttk.Label(
        ventana,
        text="\nPresione una de las opciones que se muestra a continuación",
        font=fuente_descripcion,
    )
    texto_opciones.pack(pady=10)

    # Botones
    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(pady=10)

    botones = [
        ("Todas las estaciones"),
        ("Análisis por estación"),
        ("Índice parcial horario"),
        ("Índice global horario"),
        ("Cancelar")
    ]

    for texto in botones:
        boton = ttk.Button(
            frame_botones,
            text=texto,
            width=20,
            command=lambda t=texto: manejar_evento(t),
        )
        boton.pack(side="left", padx=5)

    # Texto para salir
    texto_cancelar = ttk.Label(
        ventana,
        text="\nPresione Cancelar para salir del programa",
        font=fuente_descripcion,
    )
    texto_cancelar.pack(pady=10)

    def manejar_evento(evento):
        if evento == "Cancelar":
            ventana.destroy()
        elif evento == "Todas las estaciones":
            ventana2(ventana)  # Pasar la ventana principal como padre
        elif evento == "Análisis por estación":
            ventana3()
        elif evento == "Índice parcial horario":
            ventana4()
        elif evento == "Índice global horario":
            ventana5()

    # sv_ttk.set_theme(darkdetect.theme())
    windows_theme_dinamico(ventana)
    # pywinstyles.apply_style(ventana,'acrylic')
    apply_theme_to_titlebar_dinamico(ventana)

    # Ejecutar el bucle de la ventana
    # ventana.call('wm', 'attributes', '.', '-topmost', '1')
    ventana.mainloop()


ventana_principal()