import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os

path=r'Calidad del aire\Proyecto\Datos'
all_files = glob.glob(os.path.join(path + "/*.csv"))

data = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    data.append(df)

frame = pd.concat(data, axis=0, ignore_index=True)
frame[['Fecha', 'Hora']] = frame['Fecha_Hora'].str.split(' ', n=1, expand=True)
frame.insert(0, 'Fecha', frame.pop('Fecha'))
frame.insert(1, 'Hora', frame.pop('Hora'))
frame.pop('Fecha_Hora')
frame.pop('calidad_pm1')
frame.pop('pm1')
frame.pop('calidad_pm10')
frame.pop('pm10')
frame.set_index('Fecha', inplace=True)
frame.index = pd.to_datetime(frame.index, format='%Y-%m-%d')

# print(frame.index)
# print(frame.head(6))
# print(frame.tail(6))
# print(frame['pm25'])

frame2=frame[(frame['pm25']>0) & (frame['pm25']<100)]

# slize = pd.DataFrame(frame2.loc["2024-10-12",:]) # Secciona una parte del dataframe
# print(slize) # Muestra un fragmento del dataframe donde habría una inconsistencia normalmente
medias = frame2.groupby([frame2.index.year,
                     frame2.index.month,
                     frame2.index.day])['pm25'].mean()
medias.index.names = ["Año", "Mes", "Día"]

# print(medias.head(35)) # Muestra las primeras 35 del dataframe de promedios