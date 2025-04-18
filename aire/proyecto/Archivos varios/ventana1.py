from tkinter import *

ventana1=Tk()
ventana1.title("VentanaPortada" )
ventana1.geometry("800x800")

L1=Label(ventana1, text="¿Qué desea calcular?" ,
      fg="black", bg= "white",
      font=("Arial", "16", "bold")
            ).place(
                x=150,y=150)

Bsiguiente=Button(ventana1, text="Calidad del aire", command=quit).place(x=150, y=200)
Bsiguiente=Button(ventana1, text="Datos de cada contaminante", command=quit).place(x=150, y=250)
Bsiguiente=Button(ventana1, text="Valores límites", command=quit).place(x=150, y=300)
Bsiguiente=Button(ventana1, text="índices horarios y globales", command=quit).place(x=150, y=350)


ventana1.mainloop()
