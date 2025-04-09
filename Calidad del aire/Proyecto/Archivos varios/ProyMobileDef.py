import PySimpleGUI as sg
import numpy as np

sg.theme('DarkBlue')   # Window theme

def ventana1():
    layout = [  [sg.Text(text='Universidad de Antioquia', font=('Arial', 8,'bold'))],
                [sg.Text(text='Ximena Londoño \nNicoll Fajardo \nLaura Jimenez',font=('Arial', 6,'bold'))],
                [sg.Text(text='Reducción de los contaminantes del aire a través de purificadores.\n\nLos purificadores de aire han sido desarrollados a medida que la tecnología y la contaminación ha avanzado; con el fin de reducir los compuestos químicos que contaminan y están presentes en el aire se realizan mediciones y dados los valores obtenidos se puede saber que índice de contaminación está presente en tiempo real y qué tipo de alternativa de purificación se puede utilizar para combatirlo.', size = (105,10), font=('Arial', 6), pad = ((0,0),(0,0))),sg.Image(filename = 'UdeA1.gif', pad = ((0,0),(0,0)), key = "icon_image")],
                [sg.Text(text='\nPresione una de las opciones que se muestra a continuacin', font=('Arial', 6))],
                [sg.Text(text='\nPresione Cancelar para salir del programa', font=('Arial', 6))],
                [sg.Button(button_text='Calidad del aire',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Valores límites diarios',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Índice parcial horario',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Índice global horario',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]  # identify the multiline via key option
    window = sg.Window('Proyecto Algoritmos y programación',layout,location=(0,0)).Finalize()
    grab_anywhere=True
    window.maximize()
    return

def ventana2():

    layout = [  [sg.Text('Nivel de la calidad del aire',font=('Arial',6))],
                [sg.Text('Ingrese el valor de la calidad del aire',font=('Arial',6)), sg.Input()],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button(button_text='Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]  # identify the multiline via key option

    # Create the Window

    window = sg.Window('Calidad del aire', layout).Finalize()

    # window.Maximize()
    while True:
    
        event, values = window.read()

        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
  
        if (n<0 or n>500):
            window['-OUTPUT-'].update('Hola, su valor ingresado fue ' + values[0] + ", este valor no está admitido en la escala y debe ingresar un nuevo valor",font=('Arial',6), text_color='LightCyan')
        elif (n>=0 and n<=50):
            window['-OUTPUT-'].update('Hola, su valor ingresado fue ' + values[0] + ", esto significa que la calidad del aire es muy buena",font=('Arial',6), text_color='green')
        elif (n>50 and n<=100):
            window['-OUTPUT-'].update('Hola, su valor ingresado fue ' + values[0] + ", esto significa que la calidad del aire es aceptable",font=('Arial',6), text_color='yellow')
        elif (n>100 and n<=150):
            window['-OUTPUT-'].update('Hola, su valor ingresado fue ' + values[0] + ", esto significa que la calidad del aire es dañina para la salud de grupos sensibles",font=('Arial',6), text_color='orange')
        elif (n>150 and n<=200):
            window['-OUTPUT-'].update('Hola, su valor ingresado fue ' + values[0] + ", esto significa que la calidad del aire es dañina para la salud",font=('Arial',6), text_color='red')
        elif (n>200 and n<=300):
            window['-OUTPUT-'].update('Hola, su valor ingresado fue ' + values[0] + ", esto significa que la calidad del aire es muy dañina para la salud",font=('Arial',6), text_color='purple')
        elif (n>300 and n<=500):
            window['-OUTPUT-'].update('Hola, su valor ingresado fue ' + values[0] + ", esto significa que la calidad del aire es peligrosa",font=('Arial',6), text_color='brown')
    
    window.close()
    return

def ventana3():

    layout = [  [sg.Text('A continuación presione uno de los siguientes contaminantes',font=('Arial',6))],
                [sg.Text('O presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Button(button_text='Dióxido de azufre (SO2)',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Dióxido de nitrógeno (NO2)',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Partículas PM10',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Ozono (O3)',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button(button_text='Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]  # identify the multiline via key option

    return sg.Window('Valores límites diarios de concentración de un contaminante', layout).Finalize()

    

def ventana4():

    layout = [  [sg.Text('A continuación ingrese los valores diarios para el dióxido de azufre y el número de ocasiones al año',font=('Arial',6))],
                [sg.Text('Ingrese el valor diario',font=('Arial',6)), sg.Input()],
                [sg.Text('Ingrese el número de ocasiones en el año',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('Valores límites diarios de concentración del dióxido de azufre', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
        m = int(values[1])
    
        if (n>125 and m>24):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que hay un nivel alto de peligro",font=('Arial',6))
        elif (n<=125 and m>24):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que no hay ningún peligro",font=('Arial',6))
        elif (n<=125 and m<=24):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que no hay ningún peligro",font=('Arial',6))
        elif (n>125 and m<=24):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que hay un nivel moderado de peligro",font=('Arial',6))

    window.close()
    return
    
def ventana5():

    layout = [  [sg.Text('A continuación ingrese los valores diarios para el dióxido de nitrógeno y el número de ocasiones al año',font=('Arial',6))],
                [sg.Text('Ingrese el valor diario',font=('Arial',6)), sg.Input()],
                [sg.Text('Ingrese el número de ocasiones en el año',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('Valores límites diarios de concentración del dióxido de nitrógeno', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
        m = int(values[1])
    
        if (n>200 and m>18):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que hay un nivel alto de peligro",font=('Arial',6))
        elif (n<=200 and m>18):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que no hay ningún peligro",font=('Arial',6))
        elif (n<=200 and m<=18):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que no hay ningún peligro",font=('Arial',6))
        elif (n>200 and m<=18):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que hay un nivel moderado peligro",font=('Arial',6))

    window.close()
    return

def ventana6():

    layout = [  [sg.Text('A continuación ingrese los valores diarios para las partículas PM10 y el número de ocasiones al año',font=('Arial',6))],
                [sg.Text('Ingrese el valor diario',font=('Arial',6)), sg.Input()],
                [sg.Text('Ingrese el número de ocasiones en el año',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('Valores límites diarios de concentración de las partículas PM10', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
        m = int(values[1])
    
        if (n>50 and m>35):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que hay un nivel alto de peligro",font=('Arial',6))
        elif (n<=50 and m>35):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que no hay ningún peligro",font=('Arial',6))
        elif (n<=50 and m<=35):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que no hay ningún peligro",font=('Arial',6))
        elif (n>50 and m<=35):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que hay un nivel moderado de peligro",font=('Arial',6))

    window.close()
    return

def ventana7():

    layout = [  [sg.Text('A continuación ingrese los valores diarios para el Ozono (O3) y el número de ocasiones al año',font=('Arial',6))],
                [sg.Text('Ingrese el valor diario',font=('Arial',6)), sg.Input()],
                [sg.Text('Ingrese el número de ocasiones en el año',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('Valores límites diarios de concentración del Ozono (O3)', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
        m = int(values[1])
    
        if (n>120 and m>25):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que hay un nivel alto de peligro",font=('Arial',6))
        elif (n<=120 and m>25):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que no hay ningún peligro",font=('Arial',6))
        elif (n<=120 and m<=25):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que no hay ningún peligro",font=('Arial',6))
        elif (n>120 and m<=25):
            window['-OUTPUT-'].update('Hola, su valor diario ingresado fue ' + values[0] + ' y el valor de ocasiones al año ingresadas fue ' + values[1] +", estos valores indican que hay un nivel moderado de peligro",font=('Arial',6))

    window.close()
    return

def ventana8():

    layout = [  [sg.Text('A continuación presione uno de los siguientes contaminantes',font=('Arial',6))],
                [sg.Text('O presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Button('IP Dióxido de azufre (SO2)',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('IP Dióxido de nitrógeno (NO2)',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('IP Partículas PM10',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('IP Ozono (O3)',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]  # identify the multiline via key option

    return sg.Window('Índice parcial horario de los contaminantes', layout).Finalize()

def ventana9():

    layout = [  [sg.Text('A continuación ingrese los valores de concentración para cada uno de los contaminantes',font=('Arial',6))],
                [sg.Text('Ingrese la concentración del SO2',font=('Arial',6)), sg.Input()],
                [sg.Text('Ingrese la concentración del NO2',font=('Arial',6)), sg.Input()],
                [sg.Text('Ingrese la concentración de las partículas PM10',font=('Arial',6)), sg.Input()],
                [sg.Text('Ingrese la concentración del O3',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,3), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('Índice global horario', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        SO = int(values[0])
        NO = int(values[1])
        PM = int(values[2])
        O = int(values[3])

        IPMatrix = []
        
        IPSO = 0.286*SO
        IPNO = 0.5*NO
        IPPM = 1*PM
        IPO = 0.556*O

        IPMatrix.append(IPSO)
        IPMatrix.append(IPNO)
        IPMatrix.append(IPPM)
        IPMatrix.append(IPO)

        maximo = IPMatrix[0]

        for i in range(0,len(IPMatrix)):
            if(IPMatrix[i]>maximo):
                maximo=IPMatrix[i]

        m=""
        result=m+str(maximo)

        if (maximo<0 or maximo>500):
            window['-OUTPUT-'].update("El valor del índice global excede la escala, por favor revise sus datos",font=('Arial',6))
        elif (maximo>=0 and maximo<=50):
            window['-OUTPUT-'].update('La calidad del aire es muy buena y no es necesario usar purificadores, el valor del índice global es '+ result + "",font=('Arial',6))
        elif (maximo>50 and maximo<=100):
            window['-OUTPUT-'].update('La calidad del aire es aceptable, se recomienda evitar el uso de automóviles y reducir el uso industrial, el valor del índice global es ' + result + "",font=('Arial',6))
        elif (maximo>100 and maximo<=150):
            window['-OUTPUT-'].update('La calidad del aire es intermedia, se recomienda usar pinturas especiales en los murales, el valor del índice global es ' + result + "",font=('Arial',6))
        elif (maximo>150 and maximo<=200):
            window['-OUTPUT-'].update('La calidad del aire es dañina a la salud, se recomienda usar paredes arbóreas, el valor del índice global es ' + result + "",font=('Arial',6))
        elif (maximo>200 and maximo<=300):
            window['-OUTPUT-'].update('La calidad del aire es muy dañina a la salud, se recomienda utilizar tejados que reducen el smog, el valor del índice global es ' + result + "",font=('Arial',6))
        elif (maximo>300 and maximo<=500):
            window['-OUTPUT-'].update('La calidad del are es peligrosa, se recomienda la hoja biosolar, el valor del índice global es ' + result + "",font=('Arial',6))

    window.close()
    return

def ventana10():

    layout = [  [sg.Text('A continuación ingrese los valores de concentración para calcular el IP del SO2',font=('Arial',6))],
                [sg.Text('Ingrese el valor de concentración del SO2',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('IP Dióxido de azufre (SO2)', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
        IP = 0.286*n
        m = ""
        result = m + str(IP)
        
        window['-OUTPUT-'].update('Hola, su valor de concentración del SO2 ingresado fue ' + values[0] + ', el valor del IP para el SO2 es: ' + result + "",font=('Arial',6))

    window.close()
    return

def ventana11():

    layout = [  [sg.Text('A continuación ingrese los valores de concentración para calcular el IP del NO2',font=('Arial',6))],
                [sg.Text('Ingrese el valor de concentración del NO2',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('IP Dióxido de nitrógeno (NO2)', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
        IP = 0.5*n
        m = ""
        result = m + str(IP)
        
        window['-OUTPUT-'].update('Hola, su valor de concentración del NO2 ingresado fue ' + values[0] + ', el valor del IP para el NO2 es: ' + result + "",font=('Arial',6))

    window.close()
    return

def ventana12():

    layout = [  [sg.Text('A continuación ingrese los valores de concentración para calcular el IP de las partículas PM10',font=('Arial',6))],
                [sg.Text('Ingrese el valor de concentración',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('IP Partículas PM10', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
        IP = 1*n
        m = ""
        result = m + str(IP)
        
        window['-OUTPUT-'].update('Hola, su valor de concentración de las partículas PM10 ingresado fue ' + values[0] + ', el valor del IP para las partículas PM10 es: ' + result + "",font=('Arial',6))

    window.close()
    return

def ventana13():

    layout = [  [sg.Text('A continuación ingrese los valores de concentración para calcular el IP del O3',font=('Arial',6))],
                [sg.Text('Ingrese el valor de concentración',font=('Arial',6)), sg.Input()],
                [sg.Text('Presione Cancelar para salir de la ventana',font=('Arial',6))],
                [sg.Text('',font=('Arial',6),size=(105,2), key='-OUTPUT-')],
                [sg.Button('Ok',font=('Arial',6),button_color=('LightCyan','DarkSlateGrey'),mouseover_colors=('DarkSlateGrey','LightCyan'),border_width=(3)),sg.Button('Cancelar',font=('Arial',6),button_color=('LightCyan','Red'),mouseover_colors=('Red','LightCyan'),border_width=(3))]]

    window = sg.Window('IP Ozono (O3)', layout).Finalize()

    while True:
    
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
    
        n = int(values[0])
        IP = 0.556*n
        m = ""
        result = m + str(IP)
        
        window['-OUTPUT-'].update('Hola, su valor de concentración del SO2 ingresado fue ' + values[0] + ', el valor del IP para el SO2 es: ' + result + "",font=('Arial',6))

    window.close()
    return

window1, window2 = ventana1(), None

while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Calidad del aire':  #If the option is selected, then open the related window
        window2 = ventana2()
    elif event == 'Valores límites diarios':
        window3 = ventana3()
    elif event == 'Dióxido de azufre (SO2)':
        window4 = ventana4()
    elif event == 'Dióxido de nitrógeno (NO2)':
        window5 = ventana5()
    elif event == 'Partículas PM10':
        window6 = ventana6()
    elif event == 'Ozono (O3)':
        window7 = ventana7()
    elif event == 'Índice parcial horario':
        window8 = ventana8()
    elif event == 'Índice global horario':
        window9 = ventana9()
    elif event == 'IP Dióxido de azufre (SO2)':
        window10 = ventana10()
    elif event == 'IP Dióxido de nitrógeno (NO2)':
        window11 = ventana11()
    elif event == 'IP Partículas PM10':
        window12 = ventana12()
    elif event == 'IP Ozono (O3)':
        window13 = ventana13()
        
window.close()
