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

th_bra , n_bra = np.genfromtxt("Daten/Bragg.txt", unpack=True)
print(th_bra)
th_bro , n_bro = np.genfromtxt("Daten/Brom2.txt", unpack=True)
print(th_bro)
th_cu  , n_cu  = np.genfromtxt("Daten/Emissionsspektrum2.txt", unpack=True)
th_gal , n_gal = np.genfromtxt("Daten/Gallium2.txt", unpack=True)
th_rub , n_rub = np.genfromtxt("Daten/Rubidium2.txt", unpack=True)
th_str , n_str = np.genfromtxt("Daten/Strontium2.txt", unpack=True)
th_zin , n_zin = np.genfromtxt("Daten/Zink2.txt", unpack=True)
th_Zir , n_zir = np.genfromtxt('Daten/Zirkonium2.txt', unpack=True)