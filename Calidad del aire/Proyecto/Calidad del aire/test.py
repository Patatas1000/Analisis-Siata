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

import tkinter as tk
import tkintermapview

# Crear ventana principal
root = tk.Tk()
root.title("Mapa con TkinterMapView")

# Crear widget de mapa
map_widget = tkintermapview.TkinterMapView(root, width=800, height=600)
map_widget.pack(fill="both", expand=True)

# Establecer posición inicial (por ejemplo, Bogotá, Colombia)
map_widget.set_position(4.711, -74.072)
map_widget.set_zoom(12)

# Ejecutar la ventana
root.mainloop()