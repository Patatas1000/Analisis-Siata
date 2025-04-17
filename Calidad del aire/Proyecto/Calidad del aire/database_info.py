import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os

# path=r'Calidad del aire\Proyecto\Datos'
path=r'Calidad del aire\Proyecto\Bases'

def data(path):

    all_files = glob.glob(os.path.join(path + "/*.csv"))

    data = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, encoding='utf-8')
        data.append(df)

    frame = pd.concat(data, axis=0, ignore_index=True)
    frame[['Fecha', 'Hora']] = frame['Fecha_Hora'].str.split(' ', n=1, expand=True)
    frame.insert(0, 'Fecha', frame.pop('Fecha'))
    frame.insert(1, 'Hora', frame.pop('Hora'))
    frame.pop('Fecha_Hora')
    frame.set_index('Fecha', inplace=True)
    frame.index = pd.to_datetime(frame.index, format='%Y-%m-%d')
    drop=['calidad_pm1', 'pm1', 'calidad_pm10', 'calidad_pm25', 'calidad_no',
        'calidad_no2', 'calidad_nox','calidad_ozono', 'co','calidad_co', 'calidad_so2', 'pst', 'calidad_pst',
        'dviento_ssr', 'calidad_dviento_ssr', 'haire10_ssr', 'calidad_haire10_ssr', 'p_ssr', 'calidad_p_ssr',
        'pliquida_ssr', 'calidad_pliquida_ssr', 'rglobal_ssr', 'calidad_rglobal_ssr', 'taire10_ssr', 'calidad_taire10_ssr', 'vviento_ssr', 'calidad_vviento_ssr']
    frame2=frame.drop(columns=drop, axis=1)
    return(frame2)

##path2 = r'Calidad del aire\Proyecto\Estaciones'

path2= r'C:\Users\ivans\OneDrive\Desktop\Juan\Analisis-Siata\Calidad del aire\Proyecto\Estaciones'

estaciones = pd.read_csv(path2 + '/Estaciones_CalidadAire.csv', encoding='latin1')

print(estaciones.head(10))