import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os
from database_info import data

path=r'Calidad del aire\Proyecto\Bases'
frame2=data(path)


def ICA(frame2):
    columnas = ['pm25', 'pm10', 'no', 'no2', 'nox', 'ozono', 'so2']
    medias_dict = {}

    for columna in columnas:
        frame_filtrado = frame2[(frame2[columna] > 0) & (frame2[columna] < 1100)]
        medias = frame_filtrado.groupby([frame_filtrado.index.year,
                                            frame_filtrado.index.month,
                                            frame_filtrado.index.day])[columna].mean()
        # medias = frame2.groupby([frame2.index.year,
        #                                     frame2.index.month,
        #                                     frame2.index.day])[columna].mean()
        medias.index.names = ["Año", "Mes", "Día"]
        medias_df = medias.to_frame(name=columna)
        medias_df.index = pd.to_datetime(frame_filtrado.groupby(
            [frame_filtrado.index.year, frame_filtrado.index.month, frame_filtrado.index.day]
        ).apply(lambda x: x.index[0]).values)
        medias_dict[columna] = medias_df
    frame3=pd.concat(medias_dict.values(), axis=1)
    # print(frame3.columns)
    # print(frame3.index)





    # ICA = (((I_hi-I_lo)/(BP_hi-Bp_lo))*(C_cont-Bp_lo))-I_lo
# ICA(frame2)