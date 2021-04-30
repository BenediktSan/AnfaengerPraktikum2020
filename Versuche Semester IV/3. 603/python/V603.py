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


#  Naturkonstanten

h = 6.62607015e-34
c = 299792458
d_LiF = 201.4e-12
e0 = 1.602176634e-19

## Kupfer Emissionsspektrum

k_a = ufloat(22.7 , 0.2)
k_b = ufloat(20.4 , 0.2)

# zugehörige Wellenlängen

lam_a = 2 * d_LiF * unp.sin(k_a * np.pi / 180)
lam_b = 2 * d_LiF * unp.sin(k_b * np.pi / 180)

# zugehörige Energien

E_a = h * c / lam_a
E_b = h * c / lam_b

# in elektronenvolt

E_ae = E_a/e0
E_be = E_b/e0

print("Energie K alpha:", E_ae.n , "pm" , E_ae.s)
print("Energie K beta:", E_be.n , "pm" , E_be.s)

# 1. Aufnahme eines Emissionssepktrums der Kupfer Röntgenröhre

theta_C , N_C = np.genfromtxt("EmissionCu.dat", unpack = True)
#print(theta_C)
#print(N_C)

#Emission = zip(theta_C, N_C)

#for s in len(N_C):
#    N_C[s] = int(N_C[s])
#list = []

#for i in range(len(theta_C)):
#    for n in range(N_C[i]):
#        list.append(theta_C[i])

#print(list)


#E_l= list(Emission)
#print(len(E_l))

#print(Emission.theta_C)
plt.figure()
#plt.hist(E_l, bins = 40)
plt.plot(theta_C, N_C , "y.", label = "Daten Cu")
plt.legend()
plt.xlabel("Einfallswinkel in °")
plt.ylabel("Anzahl Impulse pro s")
plt.tight_layout()
plt.savefig("build/plots/Emissionsspektrum.pdf")


#2.  Transmisson T(Lambda)

theta_0 , N_0_ = np.genfromtxt("ComptonOhne.txt", unpack=True)
theta_A , N_A_ = np.genfromtxt("ComptonAl.txt", unpack =True)

tau = 90e-6

#N_0_err = np.sqrt(N_0_)
#N_A_err = np.sqrt(N_A_)
#
#N_0 = ufloat(N_0_ , N_0_err)
#N_A = ufloat(N_A_ , N_A_err)
#
## Korrektur der Totzeit
#
#N0 = N_0 / (1 - tau*N_0)
#NA = N_A / (1 - tau*N_A)
#T = NA / N0
#


#plt.figure()
#plt.plot(theta_0, N_0 , "k.", label = "Daten Ohne")
#plt.legend()
#plt.savefig("build/plots/Compton_ohne.pdf")
#
#plt.figure()
#plt.plot(theta_A, N_A , "k.", label = "Daten Al")
#plt.legend()
#plt.savefig("build/plots/Compton_Al.pdf")


#Diskussion

E_a_t = 8048.11
E_b_t = 8906.9

ab_a = (E_a_t - E_a) * 100 / E_a_t
ab_b = (E_b_t - E_b) * 100 / E_b_t

print(f'Abweichung der Abweichung ')


