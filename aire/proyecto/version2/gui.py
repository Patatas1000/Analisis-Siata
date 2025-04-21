import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkintermapview
import math
from tema import apply_theme_to_titlebar
from tema import window_theme
from adj_ven import centro
from all_stations import mostrar_todo
from all_stations import mostrar_dataframe
from per_station import mostrar_grafico_est
from per_station import mostrar_dataframe_est
from database_info import data
from database_info import coord
from database_info import empr
from mapdens import dist

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Análisis de calidad del aire de Medellín")
        centro(self.root, 1690, 950)
        self.menu_visible = False
        self.menu_width = 170

        self.container = tk.Frame(self.root, bg="#f0f0f0")
        self.container.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        p_ancho= self.root.winfo_screenwidth()

        self.menu_frame = tb.Frame(self.root, bootstyle="dark", width=0, height=600)
        self.menu_frame.place(x=0, y=0, height=p_ancho)

        self.toggle_btn = tk.Button(self.root, text="☰", font=("Arial", 16), command=self.toggle_menu)
        self.toggle_btn.place(x=10, y=10)

        self.frames = {
            "Inicio": self.inicio(),
            "Análisis total": self.todas(),
            "Análisis por estación": self.estacion(),
            "Mapa":self.mapa(),
            "Glosario": self.glosario(),
            "Salir": self.salir()
        }

        opciones = list(self.frames.keys())
        for i, texto in enumerate(opciones):
            btn = tb.Button(self.menu_frame, text=texto, bootstyle="secondary", width=20,
                            command=lambda name=texto: self.mostrar_frame(name))
            btn.place(x=10, y=60 + i * 60, height=40)

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
        path3=r'aire\proyecto\indus'

        frame2=data(path)
        coordenadas = coord(path2)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis en todas las estaciones del SIATA", font=("Arial", 24))
        label.pack(pady=20)
 
        titulo = tk.Label(frame, text="En esta ventana puede revisar el gráfico de los valores diarios promedio para todos los contaminantes en todas las estaciones en la base de datos, además también puede visualizar las primeras 40 filas de los datos utilizados en este análisis, usando los botones para mostrar el gráfico y los datos respectivamente.",
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

        titulo = tk.Label(frame, text="Use la lista desplegable para seleccionar la estación para la cual desea conocer los valores diarios promedio para los contaminantes medidos. " \
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

        combobox = ttk.Combobox(frame, textvariable=estacion_seleccionada_nombre, values=nombres_estaciones, state="readonly", font=fuente_texto)
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
        path = r'aire\proyecto\bases'
        path2 = r'aire\proyecto\estaciones'
        path3 = r'aire\proyecto\indus'

        frame2 = data(path)
        coordenadas_estaciones = coord(path2)
        empresas = empr(path3)

        columnas = ['Estacion', 'Longitud', 'Latitud', 'Ciudad']
        Cities = ['Medellin', 'Medellín']

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Mapa de las estaciones y fuentes de contaminantes", font=("Arial", 24))
        label.pack(pady=20)

        fuente_descripcion = ("Arial", 14)
        titulo = ttk.Label(frame, text="Para visualizar los nombres de las estaciones haga click sobre el marcador de la estación en el mapa.", font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        map_widget = tkintermapview.TkinterMapView(frame)
        map_widget.pack(fill="both", expand=True)
        map_widget.set_position(6.25256, -75.56958)
        map_widget.set_zoom(14)

        markers = {}
        estaciones_densidad = {}

        def marker_clicked(marker):
            if marker.text == "":
                estacion_nombre = markers[marker]
                marker.set_text(estacion_nombre)
            else:
                marker.set_text("")

        fr = {}
        for city in Cities:
            coord2 = coordenadas_estaciones.loc[coordenadas_estaciones['Ciudad'] == city, columnas]
            fr[city] = coord2
            for i, row in coord2.iterrows():
                lat_estacion, lon_estacion = row['Latitud'], row['Longitud']
                nombre_estacion = row['Estacion']

                marker = map_widget.set_marker(lat_estacion, lon_estacion, text="", marker_color_circle="black", marker_color_outside="darkblue", command=marker_clicked)
                markers[marker] = nombre_estacion
                estaciones_densidad[nombre_estacion] = 0

        radio_km = 1
        for nombre_empresa, row_empresa in empresas.iterrows():
            lon_empresa_str = row_empresa['Longitud']
            lat_empresa_str = row_empresa['Latitud']
            lon_empresa = float(lon_empresa_str)
            lat_empresa = float(lat_empresa_str)
            for nombre_estacion in estaciones_densidad:
                estacion_info = coordenadas_estaciones[coordenadas_estaciones['Estacion'] == nombre_estacion].iloc[0]
                lat_estacion = float(estacion_info['Latitud'])
                lon_estacion = float(estacion_info['Longitud'])
                distancia = dist(lat_empresa, lon_empresa, lat_estacion, lon_estacion)
                if distancia <= radio_km:
                    estaciones_densidad[nombre_estacion] += 1

        earth_radius_km = 6371
        area_km2 = math.pi * (radio_km**2)

        for nombre_estacion, num_empresas in estaciones_densidad.items():
            estacion_info = coordenadas_estaciones[coordenadas_estaciones['Estacion'] == nombre_estacion].iloc[0]
            lat_estacion = float(estacion_info['Latitud'])
            lon_estacion = float(estacion_info['Longitud'])
            densidad = num_empresas / area_km2 if area_km2 > 0 else 0
            num_points = 20
            circle_points = []
            for j in range(num_points):
                angle = (j / num_points) * 2 * math.pi
                delta_lat = (radio_km / earth_radius_km) * (180 / math.pi) * math.sin(angle)
                delta_lon = (radio_km / earth_radius_km) * (180 / math.pi) * math.cos(angle) / math.cos(math.radians(lat_estacion))
                circle_points.append((lat_estacion + delta_lat, lon_estacion + delta_lon))

            fill_color = f"#{int(min(255, densidad * 20)):02x}0000"
            map_widget.set_polygon(circle_points, outline_color="red", fill_color=fill_color)

            map_widget.set_marker(lat_estacion + 0.005, lon_estacion + 0.005, text=f"{densidad:.2f}", text_color="black")

        return frame

    def glosario(self):
        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Glosario", font=("Arial", 24))
        label.pack(pady=20)
        btn_salir = tk.Button(frame, text="Cerrar aplicación", command=self.root.destroy)
        btn_salir.pack(pady=10)
        return frame    

    def salir(self):
        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="🚪 ¿Deseas salir?", font=("Arial", 24))
        label.pack(pady=20)
        btn_salir = tk.Button(frame, text="Cerrar aplicación", command=self.root.destroy)
        btn_salir.pack(pady=10)
        return frame