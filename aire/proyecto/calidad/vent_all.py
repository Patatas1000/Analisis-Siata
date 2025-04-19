import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys
from all_stations import all
from all_stations import mostrar_dataframe
from tema import apply_theme_to_titlebar_dinamico
from adj_ven import centro

def ventana2(parent,frame2):
    ventana2 = tk.Toplevel(parent)
    ventana2.title('Análisis de datos en todas las estaciones')
    # ventana2.geometry("1200x600")

    w , h = 1126 , 634

    centro(ventana2, w, h)

    fuente_titulo = ("Arial", 20, "bold")
    fuente_texto = ("Arial", 16, "bold")
    fuente_descripcion = ("Arial", 14)

    frame_derecho2 = ttk.Frame(ventana2)
    frame_derecho2.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    titulo = ttk.Label(frame_derecho2, text="En esta ventana puede revisar el gráfico de los valores diarios promedio para todos los contaminantes en todas las estaciones en la base de datos, además también puede visualizar las primeras 40 filas de los datos utilizados en este análisis, usando los botones para mostrar el gráfico y los datos respectivamente.",
                       font=fuente_descripcion, wraplength=700, justify="center")
    titulo.pack(pady=10)

    frame_grafico = ttk.Frame(frame_derecho2)
    frame_grafico.pack(pady=20, fill="both", expand=True)

    frame_izquierdo = ttk.Frame(ventana2)
    frame_izquierdo.place(x=10, y=100, width=200, height=1080)
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
            frame_izquierdo.place(x=0, y=45, width=200, height=1080)

    # icon=PhotoImage(file=r'Calidad del aire\Proyecto\Icons\menuL.png')
    # icon=menu_dinamico(ventana2)
    # icon_label= Label(ventana2, image=icon)
    
    boton_menu = ttk.Button(ventana2, text='Menú', command=toggle_menu)
    boton_menu.place(x=10, y=10)

    texto_cancelar = ttk.Label(
        frame_derecho2,
        text="Para salir de esta ventana, presione el botón Cancelar en el menú desplegable.",
        font=fuente_descripcion,
    )
    texto_cancelar.pack(pady=10)

    apply_theme_to_titlebar_dinamico(ventana2)

    ventana2.mainloop()