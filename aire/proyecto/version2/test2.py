import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkintermapview
from tema import apply_theme_to_titlebar
from tema import window_theme
from adj_ven import centro
from all_stations import mostrar_todo
from all_stations import mostrar_dataframe
from per_station import mostrar_grafico_est
from per_station import mostrar_dataframe_est
from database_info import data
from database_info import coord

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Análisis de calidad del aire de Medellín")
        # self.root.geometry("900x600")
        centro(self.root, 1126, 634)
        self.menu_visible = False
        self.menu_width = 170

        # Estilo solo para el menú
        # self.menu_style = tb.Style("darkly")

        # Crear contenedor para las vistas internas
        self.container = tk.Frame(self.root, bg="#f0f0f0")
        self.container.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        p_ancho= self.root.winfo_screenwidth()

        # Frame lateral
        self.menu_frame = tb.Frame(self.root, bootstyle="dark", width=0, height=600)
        self.menu_frame.place(x=0, y=0, height=p_ancho)
        
        # Botón para abrir/cerrar el menú
        self.toggle_btn = tk.Button(self.root, text="☰", font=("Arial", 16), command=self.toggle_menu)
        self.toggle_btn.place(x=10, y=10)

        # Vistas (frames)
        self.frames = {
            "Inicio": self.inicio(),
            "Análisis total": self.todas(),
            "Análisis por estación": self.estacion(),
            "Mapa":self.mapa(),
            "Salir": self.crear_salir()
        }

        # Botones del menú
        opciones = list(self.frames.keys())
        for i, texto in enumerate(opciones):
            btn = tb.Button(self.menu_frame, text=texto, bootstyle="secondary", width=20,
                            command=lambda name=texto: self.mostrar_frame(name))
            btn.place(x=10, y=60 + i * 60, height=40)

        # Mostrar inicio por defecto
        self.mostrar_frame("Inicio")
        apply_theme_to_titlebar(self.root)
        window_theme(self.root)

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

    def mostrar_frame(self, name):
        for frame in self.frames.values():
            frame.place_forget()
        self.frames[name].place(x=0, y=0, relwidth=1, relheight=1)

    # Frames individuales
    def inicio(self):
        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="🏠 Bienvenido al Inicio", font=("Arial", 24), justify="center")
        label.pack(pady=20)

        nombres = tk.Label(
            frame,
            text="Juan Diego Suárez Agualimpia \nIngeniero Químico \nUniversidad Nacional de Colombia",
            font=fuente_texto,justify="center"
        )
        nombres.pack(pady=10)

        titulo_desc = tk.Label(
            frame,
            text="Análsis de los datos provenientes del SIATA",
            font=fuente_texto,
        )
        titulo_desc.pack(pady=10)

        descripcion = tk.Label(
            frame,
            text=(
                "El Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA) es un sistema que busca prevenir y mitigar los efectos de la contaminación del aire en la región. Este análisis se centra en los datos recopilados por el SIATA, que incluyen información sobre la calidad del aire, las condiciones meteorológicas y otros factores relevantes. El objetivo es proporcionar una visión general de la calidad del aire en Medellín y su evolución a lo largo del tiempo."
            ),
            font=fuente_descripcion,
            wraplength=700,
            justify="left",
        )
        descripcion.pack(pady=20)

        return frame

    def todas(self):

        path=r'aire\proyecto\bases'
        path2=r'aire\proyecto\estaciones'

        frame2=data(path)
        coordenadas = coord(path2)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis en todas las estaciones del SIATA", font=("Arial", 24))
        label.pack(pady=20)
 
        frame_derecho2 = tk.Frame(frame)
        frame_derecho2.pack(fill="both", expand=False, padx=10, pady=10)

        titulo = tk.Label(frame_derecho2, text="En esta ventana puede revisar el gráfico de los valores diarios promedio para todos los contaminantes en todas las estaciones en la base de datos, además también puede visualizar las primeras 40 filas de los datos utilizados en este análisis, usando los botones para mostrar el gráfico y los datos respectivamente.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)
        
        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),
            ("Mostrar datos")]

        def manejar_evento2(evento):
            if evento == "Mostrar gráfico":
                mostrar_todo(frame2, frame_grafico)             
            elif evento == "Mostrar datos":
                mostrar_dataframe(frame2, frame_grafico)

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", padx=5)

        return frame

    def estacion(self):

        path=r'aire\proyecto\bases'
        path2=r'aire\proyecto\estaciones'

        frame2=data(path)
        coordenadas = coord(path2)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis por estaciones del SIATA", font=("Arial", 24))
        label.pack(pady=20)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame_derecho = tk.Frame(frame)
        frame_derecho.pack(fill="both", expand=False, padx=10, pady=10)

        titulo = tk.Label(frame_derecho, text="Use la lista desplegable para seleccionar la estación para la cual desea conocer los valores diarios promedio para los contaminantes medidos. " \
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

        frame_contenido = tk.Frame(frame)
        frame_contenido.pack(pady=20, fill="both", expand=True)

        frame_botones = tk.Frame(frame)
        frame_botones.pack(pady=10)

        botones = [
            ("Mostrar gráfico"),
            ("Mostrar datos")]

        def manejar_evento3(evento):
            nombre_estacion = estacion_seleccionada_nombre.get()
            id_estacion = id_a_nombre[nombre_estacion]

            if evento == "Mostrar gráfico":
                frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)]
                mostrar_grafico_est(frame_filtrado, frame_contenido)
            elif evento == "Mostrar datos":
                frame_filtrado = frame2[frame2['codigoSerial'] == int(id_estacion)]
                mostrar_dataframe_est(frame_filtrado, frame_contenido)

        for texto in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento3(t),
            )
            boton.pack(side="left", padx=5)


        return frame

    def mapa(self):

        path=r'aire\proyecto\bases'
        path2=r'aire\proyecto\estaciones'

        frame2=data(path)
        coordenadas = coord(path2)

        columnas = ['Estacion', 'Longitud', 'Latitud', 'Ciudad']
        Cities = ['Medellin', 'Medellín']

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Mapa de las estaciones y fuentes de contaminantes", font=("Arial", 24))
        label.pack(pady=20)

        fuente_descripcion = ("Arial", 14)
        
        # frame2 = ttk.Frame(frame)
        # frame.pack(fill="both", expand=True, padx=10, pady=10)

        titulo = ttk.Label(frame, text="Para visualizar los nombres de las estaciones haga click sobre el marcador de la estación en el mapa.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        map_widget = tkintermapview.TkinterMapView(frame)
        map_widget.pack(fill="both", expand=True)

        map_widget.set_position(6.25256, -75.56958)
        map_widget.set_zoom(14)

        markers = {}

        def marker_clicked(marker):
            if marker.text == "":
                estacion_nombre = markers[marker]
                marker.set_text(estacion_nombre)
            else:
                marker.set_text("")

        fr = {}
        for city in Cities:
            coord2 = coordenadas.loc[coordenadas['Ciudad'] == city, columnas]
            fr[city] = coord2
            for i, row in coord2.iterrows():
                marker = map_widget.set_marker(
                    row['Latitud'],
                    row['Longitud'],
                    text="",
                    marker_color_circle="black",
                    marker_color_outside="darkblue",
                    command=marker_clicked
                )
                markers[marker] = row['Estacion']

        return frame

    def crear_salir(self):
        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="🚪 ¿Deseas salir?", font=("Arial", 24))
        label.pack(pady=20)
        btn_salir = tk.Button(frame, text="Cerrar aplicación", command=self.root.destroy)
        btn_salir.pack(pady=10)
        return frame

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()