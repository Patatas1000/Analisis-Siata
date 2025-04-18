from tkinter import *

#programa principal
ventanaH=Tk()
ventanaH.title("VentanaPortada" )
ventanaH.geometry("800x800")
Label(ventanaH, text="Universidad de Antioquia" ,
      fg="black", bg= "white",
      font=("Arial", "20", "bold")
            ).place(
                x=100,y=100)

imag=PhotoImage(file="Udea1.gif")
Label(ventanaH, image=imag, bd=0).place(x=500, y=10)

L1=Label(ventanaH, text="Ximena Londoño \n Nicoll Fajardo \n Laura Jimenez " ,
      fg="black", bg= "white",
      font=("Arial", "16", "bold")
            ).place(
                x=150,y=150)

L2=Label(ventanaH, text="Reducción de los contaminantes del aire a través de purificadores" ,
      fg="green", bg= "white",
      font=("Arial", "18", "bold")
            ).place(
                x=0,y=300)

L3=Label(ventanaH, text="Los purificadores de aire han sido desarrollados a medida que la \n tecnología y la contaminación ha avanzado; con el fin de reducir \n los compuestos químicos que contaminan y están presentes en \n el aire se realizan mediciones y dados los valores obtenidos \n se puede saber que índice de contaminación está presente en \n tiempo real y qué tipo de alternativa de purificación se puede \n utilizar para combatirlo.",
      fg="black", bg= "white",
      font=("Arial", "14", "bold")
            ).place(
                x=50,y=350)

strOp1=StringVar()
strOp2=StringVar()

          
Bsiguiente=Button(ventanaH, text="Siguiente", command=ventanaH).place(x=150, y=600)
Bsiguiente=Button(ventanaH, text="Salir", command=quit).place(x=150, y=640)



ventanaH.mainloop()

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
