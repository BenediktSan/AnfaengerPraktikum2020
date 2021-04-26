import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")

if os.path.exists("python/tabellen") == False:
    os.mkdir("python/tabellen")

# 1. Aufnahme eines Emissionssepktrums der Kupfer Röntgenröhre

theta_C , N_C = np.genfromtxt("EmissionCu.dat", unpack = True)
theta_0 , N_0 = np.genfromtxt("ComptonOhne.txt", unpack=True)
theta_A , N_A = np.genfromtxt("ComptonAl.txt", unpack =True)

plt.figure
plt.plot(theta_C, N_C , "k.", label = "Daten Cu")
plt.legend()
plt.show()

plt.figure
plt.plot(theta_0, N_0 , "k.", label = "Daten Ohne")
plt.legend()
plt.show()

plt.figure
plt.plot(theta_A, N_A , "k.", label = "Daten Al")
plt.legend()
plt.show()

