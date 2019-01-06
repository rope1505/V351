import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

r = -1/ ufloat( -1.2509623101931575, 0.036595737515691854 )
s = -1 / ufloat( -0.9664466707707665, 0.02111659357306444 )
d = -2 / ufloat( -2.7094250830038322, 0.14422294081680928 )
print("Rechteck ", 1 - r )
print("Sägezahn ", 1 - s )
print("Dreieck ", 1 - d )