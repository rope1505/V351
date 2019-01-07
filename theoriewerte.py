import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
        return content

rwerte = csv_read("csv/amplituden_einrecht.csv")
swerte = csv_read("csv/amplituden_einrecht.csv")
dwerte = csv_read("csv/amplituden_eindrei.csv")
datar = np.zeros(5)
datas = np.zeros(10)
datad = np.zeros(4)
ignore = True
i=0

for values in rwerte:
    if(ignore):
        ignore = False
    else:
        datar[i] = float(values[1])
        i = i+1
        ignore = True

ignore = True
i=0      
for values in swerte:
    if(ignore):
        ignore = False
    else:
        datas[i] = float(values[1])
        i = i+1

ignore = True
i=0
for values in dwerte:
    if(ignore):
        ignore = False
    else:
        datad[i] = float(values[1])
        i = i+1
                        
theorier = np.zeros(5)
theories = np.zeros(10)
theoried = np.zeros(4)      
i = 0
for  i < 5
    theorier [i] = theorier[i-1] + (4/(np.pi * i)) * np.sin(i * )


print(datar, datas, datad)                        

