def centro(ventana, ancho, largo):
    p_largo= ventana.winfo_screenheight()
    p_ancho= ventana.winfo_screenwidth()
    x = int((p_ancho - ancho) / 2)
    y = int((p_largo - largo) / 2)
    return ventana.geometry(f"{ancho}x{largo}+{x}+{y}")
