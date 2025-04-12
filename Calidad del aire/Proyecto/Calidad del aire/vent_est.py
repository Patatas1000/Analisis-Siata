import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys
from per_station import mostrar_grafico_est
from per_station import mostrar_dataframe_est
from tema import apply_theme_to_titlebar_dinamico
from tema import windows_theme_dinamico

def ventana3(parent,frame2):
    ventana3 = tk.Toplevel(parent)
    ventana3.title('Análisis de datos en todas las estaciones')
    ventana3.geometry("1200x600")

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
