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
frame.set_index('Fecha', inplace=True)
frame.index = pd.to_datetime(frame.index, format='%Y-%m-%d')
drop=['calidad_pm1', 'pm1', 'calidad_pm10', 'pm10', 'calidad_pm25', 'calidad_no',
      'calidad_no2', 'calidad_nox','calidad_ozono','calidad_co', 'calidad_so2', 'pst', 'calidad_pst',
      'dviento_ssr', 'calidad_dviento_ssr', 'haire10_ssr', 'calidad_haire10_ssr', 'p_ssr', 'calidad_p_ssr',
      'pliquida_ssr', 'calidad_pliquida_ssr', 'rglobal_ssr', 'calidad_rglobal_ssr', 'taire10_ssr', 'calidad_taire10_ssr', 'vviento_ssr', 'calidad_vviento_ssr']
frame2=frame.drop(columns=drop, axis=1)

# print(frame.index)
# print(frame.head(6))
# print(frame.tail(6))
# print(frame['pm25'])

frame3=frame2[(frame2['pm25']>0) & (frame2['pm25']<700)]

frame4=frame2[(frame2['no']>0) & (frame2['no']<700)]

frame5=frame2[(frame2['no2']>0) & (frame2['no2']<700)]

frame6=frame2[(frame2['nox']>0) & (frame2['nox']<700)]

frame7=frame2[(frame2['ozono']>0) & (frame2['ozono']<700)]

frame8=frame2[(frame2['co']>0) & (frame2['co']<700)]

frame9=frame2[(frame2['so2']>0) & (frame2['so2']<700)]

# slize = pd.DataFrame(frame2.loc["2024-10-12",:]) # Secciona una parte del dataframe
# print(slize) # Muestra un fragmento del dataframe donde habría una inconsistencia normalmente

medias_pm25 = frame3.groupby([frame3.index.year,
                     frame3.index.month,
                     frame3.index.day])['pm25'].mean() # Calcula los promedios para la variable pm25
medias_pm25.index.names = ["Año", "Mes", "Día"] # Crea un dataframe con los promedios diarios de pm25

medias_no = frame4.groupby([frame4.index.year,
                     frame4.index.month,
                     frame4.index.day])['no'].mean()
medias_no.index.names = ["Año", "Mes", "Día"]

medias_no2 = frame5.groupby([frame5.index.year,
                     frame5.index.month,
                     frame5.index.day])['no2'].mean()
medias_no2.index.names = ["Año", "Mes", "Día"]

medias_nox = frame6.groupby([frame6.index.year,
                     frame6.index.month,
                     frame6.index.day])['nox'].mean()
medias_nox.index.names = ["Año", "Mes", "Día"]

medias_ozono = frame7.groupby([frame7.index.year,
                     frame7.index.month,
                     frame7.index.day])['ozono'].mean()
medias_ozono.index.names = ["Año", "Mes", "Día"]

medias_co = frame8.groupby([frame8.index.year,
                     frame8.index.month,
                     frame8.index.day])['co'].mean()
medias_co.index.names = ["Año", "Mes", "Día"]

medias_so2 = frame9.groupby([frame9.index.year,
                     frame9.index.month,
                     frame9.index.day])['so2'].mean()
medias_so2.index.names = ["Año", "Mes", "Día"]

# print(frame3.head(6))
# print(medias_pm25.head(4))
# print(medias_no.head(4))
# print(medias_no2.head(4))
# print(medias_nox.head(4))
# print(medias_ozono.head(4))
# print(medias_co.head(4))
# print(medias_so2.head(4))

# Convertir la serie medias_pm25 en un DataFrame con índice de fechas basado en frame3
medias_pm25 = medias_pm25.to_frame(name='pm25')  # Convertir la serie a DataFrame
medias_pm25.index = pd.to_datetime(frame3.groupby([frame3.index.year,
                                                    frame3.index.month,
                                                    frame3.index.day]).apply(lambda x: x.index[0]).values)  # Usar las fechas originales como índice

# Graficar los puntos promedio de pm25 con respecto a la fecha
plt.figure(figsize=(10, 6))
plt.scatter(medias_pm25.index, medias_pm25['pm25'], marker='o', linestyle='-', color='b', label='Promedio PM2.5')
plt.title('Promedio Diario de PM2.5', fontsize=14)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('PM2.5 (µg/m³)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()