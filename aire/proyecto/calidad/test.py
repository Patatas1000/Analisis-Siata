# import tkinter as tk
# from tkinter import ttk
# import folium
# import webbrowser

# def mostrar_mapa():
#     m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)  # Ejemplo: Nueva York
#     m.save('mi_mapa.html')
#     webbrowser.open_new_tab('mi_mapa.html')

# root = tk.Tk()
# root.title("Integración de Mapa")

# boton_mostrar = ttk.Button(root, text="Mostrar Mapa", command=mostrar_mapa)
# boton_mostrar.pack(pady=20)

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk
# from tkinterweb import HtmlFrame

# root = tk.Tk()
# root.title("Página Web en Tkinter")

# frame_html = HtmlFrame(root)
# frame_html.pack(fill="both", expand=True)
# frame_html.load_file(r"C:\Users\ivans\OneDrive\Desktop\Juan\Analisis-Siata\mapa.html")

# root.mainloop()

# import tkinter as tk
# from tkinterweb import HtmlFrame
# import folium

# # Crear un mapa con folium
# mapa = folium.Map(location=[6.5, -74.5], zoom_start=12)
# mapa.save("mapa2.html")  # Guardar el mapa en un archivo HTML

# # Crear ventana principal con tkinter
# root = tk.Tk()
# root.title("Mapa con tkinterweb")

# # Crear marco HTML
# frame = HtmlFrame(root)
# frame.pack(fill="both", expand=True)

# # Cargar el mapa HTML generado por folium
# frame.load_file(r"C:\Users\ivans\OneDrive\Desktop\Juan\Analisis-Siata\mapa2.html")  # Cargar el archivo HTML del mapa

# # Ejecutar la ventana
# root.mainloop()

# import tkinter as tk
# import tkintermapview

# # Crear ventana principal
# root = tk.Tk()
# root.title("Mapa con TkinterMapView")

# # Crear widget de mapa
# map_widget = tkintermapview.TkinterMapView(root, width=800, height=600)
# map_widget.pack(fill="both", expand=True)

# # Establecer posición inicial (por ejemplo, Bogotá, Colombia)
# map_widget.set_position(4.711, -74.072)
# map_widget.set_zoom(12)

# # Ejecutar la ventana
# root.mainloop()

from tkinter import *
#from tkinter import ttk
from ttkbootstrap import ttk
from test2 import *

#python -m pip install git+https://github.com/israel-dryer/ttkbootstrap
#pip3 install git+https://github.com/israel-dryer/ttkbootstrap
#https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/installation/



#class Functions(Tk):
class Functions(ttk.Window):
    def unload_frame_content(self):
        #self.panedwindow_left.remove(self.frame_content)
        self.frame_content.pack_forget()
        return


    def load_content_0(self, event=None):
        self.unload_frame_content()
        self.frame_right0()
        return

    def load_content_1(self, event=None):
        self.unload_frame_content()
        self.frame_right1()
        return


class MainFrame(Functions):
    def __init__(self):
        #Tk.__init__(self)
        ttk.Window.__init__(self, themename='pulse')

        self.geometry('500x300')
        self.title('Tkinter')
        
        self.set_frame_left()
        self.frame_right0()
        return


    def set_frame_left(self):
        self.frame_left = ttk.Frame(self)
        self.frame_left.pack(side=LEFT, fill=Y)

        self.frame_ctt_left = ttk.Frame(self.frame_left, bootstyle='info')
        self.frame_ctt_left.pack(fill=BOTH, expand=1, ipadx=10)
        
        self.btn0 = ttk.Button(self.frame_ctt_left, text='One', command=self.load_content_0)
        self.btn0.pack(pady=2)
        self.btn1 = ttk.Button(self.frame_ctt_left, text='Two', command=self.load_content_1)
        self.btn1.pack(pady=2)
        return


    def frame_right0(self):
        self.frame_content = ttk.Frame(self)
        self.frame_content.pack(fill=BOTH, expand=1)
        #self.panedwindow_left.add(self.frame_content)

        data= {'var_text': 'Hellow World!'}
        self.ctt = Content0(self.frame_content, data=data)
        self.ctt.pack(fill=BOTH, expand=1)
        return


    def frame_right1(self):
        self.frame_content = ttk.Frame(self)
        self.frame_content.pack(fill=BOTH, expand=1)
        #self.panedwindow_left.add(self.frame_content)
        
        ttk.Label(self.frame_content, text='Content Two').pack()
        return

if __name__== '__main__':
    app = MainFrame()
    app.mainloop()