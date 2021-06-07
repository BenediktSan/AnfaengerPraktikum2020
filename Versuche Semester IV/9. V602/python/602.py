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

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")

##Einlesen der gegeben Daten:

th_bra , n_bra = np.genfromtxt("Daten/Bragg.txt", unpack=True)
th_bro , n_bro = np.genfromtxt("Daten/Brom2.txt", unpack=True)
th_cu  , n_cu  = np.genfromtxt("Daten/Emissionsspektrum2.txt", unpack=True)
th_gal , n_gal = np.genfromtxt("Daten/Gallium2.txt", unpack=True)
th_rub , n_rub = np.genfromtxt("Daten/Rubidium2.txt", unpack=True)
th_str , n_str = np.genfromtxt("Daten/Strontium2.txt", unpack=True)
th_zin , n_zin = np.genfromtxt("Daten/Zink2.txt", unpack=True)
th_zir , n_zir = np.genfromtxt('Daten/Zirkonium2.txt', unpack=True)

th = [th_bra,th_bro,th_cu,th_gal,th_rub,th_str,th_zin,th_zir]
n  = [n_bra, n_bro,n_cu,n_gal,n_rub,n_str,n_zin,n_zir]
nam = ["Bragg","Bromium","Kupfer","Gallium","Rubidium","Strontium","Zink","Zirkonium"]
for names, x, y in zip(nam, th , n):
    plt.figure()
    plt.plot(x,y,".",label=names)
    plt.legend()
    plt.savefig("build/plots/"+ names + ".pdf")