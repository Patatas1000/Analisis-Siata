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
from tema import window_theme
from adj_ven import centro

def ventana3(parent, frame2, coordenadas):
    ventana3 = tk.Toplevel(parent)
    ventana3.title('Análisis de datos en todas las estaciones')
    # ventana3.geometry("1200x600")

    w , h = 1126 , 634

    centro(ventana3, w, h)

    fuente_titulo = ("Arial", 20, "bold")
    fuente_texto = ("Arial", 16, "bold")
    fuente_descripcion = ("Arial", 14)

    frame_derecho = ttk.Frame(ventana3)
    frame_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    titulo = ttk.Label(frame_derecho, text="Use la lista desplegable para seleccionar la estación para la cual desea conocer los valores diarios promedio para los contaminantes medidos. " \
                                            "Use los botones Mostrar el gráfico y Datos correspondientes, en el menú desplegable para ver el gráfico o los datos para la estación seleccionada.",
                       font=fuente_descripcion, wraplength=700, justify="center")
    titulo.pack(pady=10)

    id_estaciones_frame2 = sorted(frame2['codigoSerial'].unique())
    nombres_estaciones = []
    id_a_nombre = {}

    for id_estacion in id_estaciones_frame2:
        if id_estacion in coordenadas.index:
            nombre_estacion = coordenadas.loc[id_estacion, 'Estacion']
            nombres_estaciones.append(nombre_estacion)
            id_a_nombre[nombre_estacion] = id_estacion
        else:
            nombres_estaciones.append(str(id_estacion))  # Usar la ID si no se encuentra el nombre
            id_a_nombre[str(id_estacion)] = id_estacion

    estacion_seleccionada_nombre = tk.StringVar(value=nombres_estaciones[0])

    combobox = ttk.Combobox(frame_derecho, textvariable=estacion_seleccionada_nombre, values=nombres_estaciones, state="readonly", font=fuente_texto)
    combobox.pack(pady=10)

    frame_contenido = ttk.Frame(frame_derecho)
    frame_contenido.pack(pady=20, fill="both", expand=True)

    frame_izquierdo = ttk.Frame(ventana3)
    frame_izquierdo.place(x=10, y=100, width=200, height=500)
    frame_izquierdo.pack_propagate(False)

    frame_izquierdo.place_forget()

    botones = [
        ("Mostrar gráfico"),
        ("Mostrar datos"),
        ("Cancelar")
    ]

    def manejar_evento3(evento):
        nombre_estacion = estacion_seleccionada_nombre.get()
        id_estacion = id_a_nombre[nombre_estacion]

        if evento == "Cancelar":
            ventana3.destroy()
        elif evento == "Mostrar gráfico":
            frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)]
            mostrar_grafico_est(frame_filtrado, frame_contenido)  # Asegúrate de que esta función esté definida
        elif evento == "Mostrar datos":
            frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)]
            mostrar_dataframe_est(frame_filtrado, frame_contenido)  # Asegúrate de que esta función esté definida

    for texto in botones:
        boton = ttk.Button(
            frame_izquierdo,
            text=texto,
            width=20,
            command=lambda t=texto: manejar_evento3(t),
        )
        boton.pack(pady=10)

    def toggle_menu():
        if frame_izquierdo.winfo_ismapped():
            frame_izquierdo.place_forget()
        else:
            frame_izquierdo.place(x=0, y=45, width=200, height=1080)

    boton_menu = ttk.Button(ventana3, text="Menú", command=toggle_menu)
    boton_menu.place(x=10, y=10)

    texto_cancelar = ttk.Label(
        frame_derecho,
        text="Para salir de esta ventana, presione el botón Cancelar en el menú desplegable.",
        font=fuente_descripcion,
    )
    texto_cancelar.pack(pady=10)
    apply_theme_to_titlebar(ventana3)