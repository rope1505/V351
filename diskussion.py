import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

r = -1/ ufloat( -1.0020193577691352,  0.020762907665498438 )
s = -1 / ufloat( -0.9664466707707665, 0.02111659357306444 )
d = -2 / ufloat( -2.041958747882847,  0.03743878154468241 )
print("Rechteck ", 1 - r )
print("Sägezahn ", 1 - s )
print("Dreieck ", 1 - d )