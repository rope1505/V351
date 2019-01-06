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
data0 = np.zeros(10)
data1 = np.zeros(10)
data2 = np.zeros(4)
ignore = True
i=0

for values in rwerte:
    if(ignore):
        ignore = False
    else:
        data0[i] = float(values[1])
        i = i+1

ignore = True
i=0      
for values in swerte:
    if(ignore):
        ignore = False
    else:
        data1[i] = float(values[1])
        i = i+1

ignore = True
i=0
for values in dwerte:
    if(ignore):
        ignore = False
    else:
        data2[i] = float(values[1])
        i = i+1
                        


print(data0, data1, data2)                        

