import tkinter
from tkinter import ttk

import sv_ttk
import darkdetect
import pywinstyles, sys

root = tkinter.Tk()

frame_botones = ttk.Frame(root)
frame_botones.pack(pady=10)

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

# This is where the magic happens
sv_ttk.set_theme(darkdetect.theme())

def apply_theme_to_titlebar(root):
    version = sys.getwindowsversion()

    if version.major == 10 and version.build >= 22000:
        # Set the title bar color to the background color on Windows 11 for better appearance
        pywinstyles.change_header_color(root, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
    elif version.major == 10:
        pywinstyles.apply_style(root, "dark" if sv_ttk.get_theme() == "dark" else "normal")

        # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
        root.wm_attributes("-alpha", 0.99)
        root.wm_attributes("-alpha", 1)

# Example usage (replace `root` with the reference to your main/Toplevel window)
apply_theme_to_titlebar(root)

root.mainloop()