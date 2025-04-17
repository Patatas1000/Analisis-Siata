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

# def ventana3(parent,frame2):
#     ventana3 = tk.Toplevel(parent)
#     ventana3.title('Análisis de datos en todas las estaciones')
#     ventana3.geometry("1200x600")

#     fuente_titulo = ("Arial", 20, "bold")
#     fuente_texto = ("Arial", 16, "bold")
#     fuente_descripcion = ("Arial", 14)

#     frame_derecho = ttk.Frame(ventana3)
#     frame_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=10)

#     titulo = ttk.Label(frame_derecho, text="Use la lista desplegable para seleccionar el código de la estación para la cual desea conocer los valores diarios promedio para los contaminantes medidos. " \
#     "Use los botones Mostrar el gráfico y Datos correspondientes, en el menú desplegable para ver el gráfico o los datos para la estación seleccionada.",
#                        font=fuente_descripcion, wraplength=700, justify="center")
#     titulo.pack(pady=10)

#     id_estaciones = sorted(frame2['codigoSerial'].unique())
#     estacion_seleccionada = tk.StringVar(value=id_estaciones[0])

#     combobox = ttk.Combobox(frame_derecho, textvariable=estacion_seleccionada, values=id_estaciones, state="readonly", font=fuente_texto)
#     combobox.pack(pady=10)

#     frame_contenido = ttk.Frame(frame_derecho)
#     frame_contenido.pack(pady=20, fill="both", expand=True)

#     frame_izquierdo = ttk.Frame(ventana3)
#     frame_izquierdo.place(x=10, y=100, width=200, height=500)
#     frame_izquierdo.pack_propagate(False)

#     frame_izquierdo.place_forget()

#     botones = [
#         ("Mostrar gráfico"),
#         ("Mostrar datos"),
#         ("Cancelar")
#     ]

#     def manejar_evento3(evento):
#         id_estacion = estacion_seleccionada.get()

#         if evento == "Cancelar":
#             ventana3.destroy()
#         elif evento == "Mostrar gráfico":
#             frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)]
#             mostrar_grafico_est(frame_filtrado, frame_contenido)
#         elif evento == "Mostrar datos":
#             frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)]
#             mostrar_dataframe_est(frame_filtrado, frame_contenido)

#     for texto in botones:
#         boton = ttk.Button(
#             frame_izquierdo,
#             text=texto,
#             width=20,
#             command=lambda t=texto: manejar_evento3(t),
#         )
#         boton.pack(pady=10)

#     def toggle_menu():
#         if frame_izquierdo.winfo_ismapped():
#             frame_izquierdo.place_forget()
#         else:
#             frame_izquierdo.place(x=0, y=45, width=200, height=1080)

#     boton_menu = ttk.Button(ventana3, text="Menú", command=toggle_menu)
#     boton_menu.place(x=10, y=10)

#     texto_cancelar = ttk.Label(
#         frame_derecho,
#         text="Para salir de esta ventana, presione el botón Cancelar en el menú desplegable.",
#         font=fuente_descripcion,
#     )
#     texto_cancelar.pack(pady=10)
#     apply_theme_to_titlebar_dinamico(ventana3)

def ventana3(parent, frame2, coordenadas): 
    ventana3 = tk.Toplevel(parent) 
    ventana3.title('An?lisis de datos en todas las estaciones') 
    ventana3.geometry("1200x600") 

    fuente_titulo = ("Arial", 20, "bold") 
    fuente_texto = ("Arial", 16, "bold") 
    fuente_descripcion = ("Arial", 14)
    fuente_lista = ("Arial", 10) 

    frame_derecho = ttk.Frame(ventana3) 
    frame_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=10) 

    titulo = ttk.Label(frame_derecho, text=u"Use la lista desplegable para seleccionar el c?digo de la estaci?n para la cual desea conocer los valores diarios promedio para los contaminantes medidos. " \
    "Use los botones Mostrar el gr?fico y Datos correspondientes, en el men? desplegable para ver el gr?fico o los datos para la estaci?n seleccionada.", 
                       font=fuente_descripcion, wraplength=700, justify="center") 
    titulo.pack(pady=10) 

    id_estaciones = sorted(frame2['codigoSerial'].unique()) 
    estaciones_validas = {codigo: coordenadas.loc[codigo, "Estacion"] for codigo in id_estaciones if codigo in coordenadas.index} 

    if not estaciones_validas: 
        raise ValueError("No hay estaciones v?lidas en el dataframe 'coordenadas'.") 

    estacion_seleccionada = tk.StringVar(value=list(estaciones_validas.values())[0]) 

    combobox = ttk.Combobox(frame_derecho, textvariable=estacion_seleccionada, values=list(estaciones_validas.values()), state="readonly", font=fuente_lista) 
    combobox.pack(pady=10) 

    frame_contenido = ttk.Frame(frame_derecho) 
    frame_contenido.pack(pady=20, fill="both", expand=True) 

    frame_izquierdo = ttk.Frame(ventana3) 
    frame_izquierdo.place(x=10, y=100, width=200, height=500) 
    frame_izquierdo.pack_propagate(False) 
    frame_izquierdo.place_forget() 

    botones = [ 
        (u"Mostrar gr?fico"), 
        (u"Mostrar datos"), 
        (u"Cancelar") 
    ] 

    def manejar_evento3(evento):
        nombre_estacion = estacion_seleccionada.get() 
        id_estacion = next(codigo for codigo, nombre in estaciones_validas.items() if nombre == nombre_estacion) 

        if evento == "Cancelar": 
            ventana3.destroy() 
        elif evento == "Mostrar gr?fico": 
            frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)] 
            mostrar_grafico_est(frame_filtrado, frame_contenido) 
        elif evento == "Mostrar datos": 
            frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)] 
            mostrar_dataframe_est(frame_filtrado, frame_contenido) 

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

    boton_menu = ttk.Button(ventana3, text=u"Men?", command=toggle_menu) 
    boton_menu.place(x=10, y=10) 

    texto_cancelar = ttk.Label( 
        frame_derecho, 
        text="Para salir de esta ventana, presione el bot?n Cancelar en el men? desplegable.", 
        font=fuente_descripcion, 
    ) 
    texto_cancelar.pack(pady=10) 
    apply_theme_to_titlebar_dinamico(ventana3) 