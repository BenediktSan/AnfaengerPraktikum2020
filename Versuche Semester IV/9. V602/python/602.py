import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os
from tabulate import tabulate

##Einlesen der gegeben Daten:

th_Bra, N_Bra = np.genfromtxt('Bragg.dat', unpack=True)
print(th_Bra)