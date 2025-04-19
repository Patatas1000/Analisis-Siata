import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tema import apply_theme_to_titlebar_dinamico
from tema import windows_theme_dinamico
from adj_ven import centro
from all_stations import mostrar_todo
from all_stations import mostrar_dataframe
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
        self.menu_style = tb.Style("darkly")

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
            "Inicio": self.crear_inicio(),
            "Perfil": self.crear_perfil(),
            "Configuración": self.crear_configuracion(),
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
        apply_theme_to_titlebar_dinamico(self.root)

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
    def crear_inicio(self):
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

    def crear_perfil(self):

        path=r'aire\proyecto\bases'
        path2=r'aire\proyecto\estaciones'

        frame2=data(path)
        coordenadas = coord(path2)

        fuente_titulo = ("Arial", 20, "bold")
        fuente_texto = ("Arial", 16, "bold")
        fuente_descripcion = ("Arial", 14)

        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="Análisis en todas las estaciones", font=("Arial", 24))
        label.pack(pady=20)
 
        frame_derecho2 = tk.Frame(frame)
        frame_derecho2.pack(fill="both", expand=False, padx=10, pady=10)

        titulo = tk.Label(frame_derecho2, text="En esta ventana puede revisar el gráfico de los valores diarios promedio para todos los contaminantes en todas las estaciones en la base de datos, además también puede visualizar las primeras 40 filas de los datos utilizados en este análisis, usando los botones para mostrar el gráfico y los datos respectivamente.",
                        font=fuente_descripcion, wraplength=700, justify="center")
        titulo.pack(pady=10)

        frame_grafico = tk.Frame(frame)
        frame_grafico.pack(pady=20, fill="both", expand=True)

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
                frame,
                text=texto,
                width=20,
                command=lambda t=texto: manejar_evento2(t),
            )
            boton.pack(side="left", pady=10)

        return frame

    def crear_configuracion(self):
        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="⚙️ Configuración", font=("Arial", 24))
        label.pack(pady=20)
        return frame

    def crear_salir(self):
        frame = tk.Frame(self.container, bg="white")
        label = tk.Label(frame, text="🚪 ¿Deseas salir?", font=("Arial", 24))
        label.pack(pady=20)
        btn_salir = tk.Button(frame, text="Cerrar aplicación", command=self.root.destroy)
        btn_salir.pack(pady=10)
        return frame

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()