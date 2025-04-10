# Esta función permite graficar los promedios diarios de las estaciones de calidad del aire

import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os

def all(frame2):

    # for i in columns:
    #     framex=frame2[(frame2[i]>0) & (frame2[i]<700)]

    frame3=frame2[(frame2['pm25']>0) & (frame2['pm25']<700)]

    frame4=frame2[(frame2['no']>0) & (frame2['no']<700)]

    frame5=frame2[(frame2['no2']>0) & (frame2['no2']<700)]

    frame6=frame2[(frame2['nox']>0) & (frame2['nox']<700)]

    frame7=frame2[(frame2['ozono']>0) & (frame2['ozono']<700)]

    # frame8=frame2[(frame2['co']>0) & (frame2['co']<700)]

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

    # medias_co = frame8.groupby([frame8.index.year,
    #                      frame8.index.month,
    #                      frame8.index.day])['co'].mean()
    # medias_co.index.names = ["Año", "Mes", "Día"]

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
    # print(medias_co.head(35))
    # print(medias_so2.head(4))

    # Convertir la serie medias_pm25 en un DataFrame con índice de fechas basado en frame3
    medias_pm25 = medias_pm25.to_frame(name='pm25')  # Convertir la serie a DataFrame
    medias_pm25.index = pd.to_datetime(frame3.groupby([frame3.index.year,
                                                        frame3.index.month,
                                                        frame3.index.day]).apply(lambda x: x.index[0]).values)  # Usar las fechas originales como índice

    medias_no = medias_no.to_frame(name='no')  # Convertir la serie a DataFrame
    medias_no.index = pd.to_datetime(frame4.groupby([frame4.index.year,
                                                        frame4.index.month,
                                                        frame4.index.day]).apply(lambda x: x.index[0]).values)  # Usar las fechas originales como índice

    medias_no2 = medias_no2.to_frame(name='no2')  # Convertir la serie a DataFrame
    medias_no2.index = pd.to_datetime(frame5.groupby([frame5.index.year,
                                                        frame5.index.month,
                                                        frame5.index.day]).apply(lambda x: x.index[0]).values)  # Usar las fechas originales como índice

    medias_nox = medias_nox.to_frame(name='nox')  # Convertir la serie a DataFrame
    medias_nox.index = pd.to_datetime(frame6.groupby([frame6.index.year,
                                                        frame6.index.month,
                                                        frame6.index.day]).apply(lambda x: x.index[0]).values)  # Usar las fechas originales como índice

    medias_ozono = medias_ozono.to_frame(name='ozono')  # Convertir la serie a DataFrame
    medias_ozono.index = pd.to_datetime(frame7.groupby([frame7.index.year,
                                                        frame7.index.month,
                                                        frame7.index.day]).apply(lambda x: x.index[0]).values)  # Usar las fechas originales como índice

    # medias_co = medias_co.to_frame(name='co')  # Convertir la serie a DataFrame
    # medias_co.index = pd.to_datetime(frame8.groupby([frame8.index.year,
    #                                                     frame8.index.month,
    #                                                     frame8.index.day]).apply(lambda x: x.index[0]).values)  # Usar las fechas originales como índice

    medias_so2 = medias_so2.to_frame(name='so2')  # Convertir la serie a DataFrame
    medias_so2.index = pd.to_datetime(frame9.groupby([frame9.index.year,
                                                        frame9.index.month,
                                                        frame9.index.day]).apply(lambda x: x.index[0]).values)  # Usar las fechas originales como índice

    # Graficar los puntos promedio de pm25 con respecto a la fecha
    plt.figure(figsize=(10, 6))
    plt.plot(medias_pm25.index, medias_pm25['pm25'], marker='.', linestyle='-', color='b', label='Promedio PM2.5')
    plt.plot(medias_no.index, medias_no['no'], marker='.', linestyle='-', color='r', label='Promedio NO')
    plt.plot(medias_no2.index, medias_no2['no2'], marker='.', linestyle='-', color='g', label='Promedio NO2')
    plt.plot(medias_nox.index, medias_nox['nox'], marker='.', linestyle='-', color='purple', label='Promedio NOX')
    plt.plot(medias_ozono.index, medias_ozono['ozono'], marker='.', linestyle='-', color='y', label='Promedio Ozono')
    # plt.scatter(medias_co.index, medias_co['co'], marker='v', linestyle='-', color='orange', label='Promedio CO')
    plt.plot(medias_so2.index, medias_so2['so2'], marker='.', linestyle='-', color='orange', label='Promedio SO2')
    plt.title('Promedio Diario de concentración', fontsize=14)
    plt.xlabel('Fecha', fontsize=12)
    plt.ylabel('Concentración contaminante (µg/m³)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    return(plt.show())