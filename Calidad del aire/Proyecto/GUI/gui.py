import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys
from database_info import data
from all_stations import all

def ventana2():
    new_window = TopLevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')

def ventana3():
    new_window = TopLevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')

def ventana4():
    new_window = TopLevel()
    new_window.title('Gráfica de contaminantes en todas lass estaciones')

def ventana5():
    new_window = TopLevel()
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

    # botones = [
    #     ("Calidad del aire", "LightCyan", "DarkSlateGrey"),
    #     ("Valores límites diarios", "LightCyan", "DarkSlateGrey"),
    #     ("Índice parcial horario", "LightCyan", "DarkSlateGrey"),
    #     ("Índice global horario", "LightCyan", "DarkSlateGrey"),
    #     ("Cancelar", "DarkCyan", "Pink"),
    # ]
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

    # Función para manejar eventos
    def manejar_evento(evento):
        if evento == "Cancelar":
            ventana.destroy()
        elif evento == "Todas las estaciones":
            ventana2()
        elif evento == "Análisis por estación":
            ventana3()
        elif evento == "Índice parcial horario":
            ventana4()
        elif evento == "Índice global horario":
            ventana5()

    sv_ttk.set_theme(darkdetect.theme())

    def apply_theme_to_titlebar(ventana):
        version = sys.getwindowsversion()

        if version.major == 10 and version.build >= 22000:
            # Set the title bar color to the background color on Windows 11 for better appearance
            pywinstyles.change_header_color(ventana, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
        elif version.major == 10:
            pywinstyles.apply_style(ventana, "dark" if sv_ttk.get_theme() == "dark" else "normal")

            # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
            ventana.wm_attributes("-alpha", 0.99)
            ventana.wm_attributes("-alpha", 1)

    # Example usage (replace `root` with the reference to your main/Toplevel window)
    apply_theme_to_titlebar(ventana)

    # Ejecutar el bucle de la ventana
    ventana.mainloop()


ventana_principal()
