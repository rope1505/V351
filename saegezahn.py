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

#def csv_write(pathToFile, delimiter=";"):
#    with open(pathToFile, "rb") as f:
#        data = list(csv.reader)   
#    import collections
#    counter = collections.defaultdict(int)
#    for row in data:
#        counter[row[0]] +=1
#    writer = csv.writer(open("/csv/gravitation.csv", "w"))
#    for row in data:
#        if counter[row[0]] >= 4:
#            writer.writerrow(row)        
    
def func(x, a, b):
    return a*x + b

werte = csv_read("csv/saegezahn.csv")
data0 = np.zeros(10)
ignore = True
i=0

for values in werte:
    if(ignore):
        ignore = False
    else:
        data0[i] = float(values[1])
        i = i+1

#np.savetxt("csv/gravi2.csv", df, delimiter=";")
xdata = np.linspace(1, 10, 10)
#print(xdata)
ydata = np.log(data0)
#print(ydata)
plt.xscale("log")
x_line = np.linspace(1, 10) 
plt.plot(xdata, ydata, 'bx', label="Wertepaare")
popt1, pcov1 = curve_fit(func, np.log(xdata), ydata ) 
plt.plot(x_line, func(np.log(x_line), *popt1), "r-", label="Ausgleichsgerade")
plt.xlabel(r"$n")
plt.ylabel(r"$\frac{U_n}{U_1}$")
error = np.diag(np.sqrt(pcov1))
plt.legend()
plt.tight_layout()
plt.savefig("build/saegezahn.pdf")
print ("a = ", popt1[0], " +/- " ,error[0] )
print(popt1[1])