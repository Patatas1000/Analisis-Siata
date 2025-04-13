import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
import sv_ttk
import darkdetect
import pywinstyles, sys

def apply_theme_to_titlebar_dinamico(ventana):
    timer_id = None

    def actualizar_titulo():
        nonlocal timer_id
        if not ventana.winfo_exists():
            return

        tema_actual = darkdetect.theme().lower()

        version = sys.getwindowsversion()
        if version.major == 10 and version.build >= 22000:
            pywinstyles.change_header_color(ventana, "#1c1c1c" if tema_actual == "dark" else "#fafafa")
        elif version.major == 10:
            pywinstyles.apply_style(ventana, "dark" if tema_actual == "dark" else "normal")
            
            ventana.wm_attributes("-alpha", 0.99)
            ventana.wm_attributes("-alpha", 1)

        timer_id = ventana.after(1000, actualizar_titulo)

    def on_close():
        nonlocal timer_id
        if timer_id:
            ventana.after_cancel(timer_id)
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", on_close)

    actualizar_titulo()

def windows_theme_dinamico(ventana):
    timer_id = None

    def actualizar_tema():
        global timer_id
        if ventana.winfo_exists():
            nuevo_tema = darkdetect.theme().lower()
            if sv_ttk.get_theme() != nuevo_tema:
                sv_ttk.set_theme(nuevo_tema)
            timer_id = ventana.after(1000, actualizar_tema)

    def on_close():
        if timer_id:
            ventana.after_cancel(timer_id)
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", on_close)
    actualizar_tema()