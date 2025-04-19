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
from gui import App


root = tk.Tk()
app = App(root)
root.mainloop()