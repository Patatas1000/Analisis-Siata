import numpy as np
import pandas as pd
import regex as rg
import matplotlib.pyplot as plt
import glob
import os
from database_info import data


def ICAcont():
    columnas = ['pm25', 'pm10', 'no', 'no2', 'nox', 'ozono', 'so2']
    for columna in columnas:
        if columna=='pm25':


    # ICA = (((I_hi-I_lo)/(BP_hi-Bp_lo))*(C_cont-Bp_lo))-I_lo
