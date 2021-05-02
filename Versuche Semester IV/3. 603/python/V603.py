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
#plt.hist(E_l, bins = 40)
#print(Emission.theta_C)

plt.figure()
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

N_0_err = np.sqrt(N_0_)
N_A_err = np.sqrt(N_A_)

N_0 = unp.uarray(N_0_ , N_0_err)
N_A = unp.uarray(N_A_ , N_A_err)

lam = 2 * d_LiF * np.sin(theta_0 * np.pi / 180)

# Korrektur der Totzeit

N0 = N_0 / (1 - tau*N_0)
NA = N_A / (1 - tau*N_A)
#print(N_0 / N0)
T = NA / N0

params, cov = np.polyfit(lam, unp.nominal_values(T), deg=1, cov=True)
errs = np.sqrt(np.diag(cov))
for name, value, error in zip('ab', params, errs):
    print(f'{name} = {value:.3f} +- {error:.3f}')

l_start = 2* d_LiF * np.sin(7 * np.pi /180)
l_fin = 2 * d_LiF *np.sin(10* np.pi/180)
lam_plot = np.linspace(l_start, l_fin)

plt.figure()
plt.plot(lam,unp.nominal_values(T), 'b.', label="Messwerte")
plt.plot(lam_plot, params[0]*lam_plot + params[1], '-', label='Lineare Regression')
plt.errorbar(lam, unp.nominal_values(T), yerr=unp.std_devs(T), fmt='r_')
plt.legend()
plt.xlabel(r'Wellenlänge $\lambda$')
plt.ylabel(r'Transmission')
plt.savefig('build/plots/transmission.pdf')

I_0 = 2731.0
print("I_0",(I_0-(I_0 / (1 - tau*(I_0/300)))/I_0))
I_1 = 1180.0
I_2 = 1024.0

T_1 = I_1/I_0
T_2 = I_2/I_0

print(f'T_1 = {T_1:.3f}, T_2 = {T_2:.3f}')


a = unp.uarray(params[0], errs[0])
b = unp.uarray(params[1], errs[1])

lam_1 = (T_1 - b)/a
lam_2 = (T_2 - b)/a

lam_c = lam_2 - lam_1

print(f'Lambda 1 = {lam_1.n , lam_1.s}')
print(f'Lambda 2 = {lam_2.n , lam_2.s}')
print(f'Compton  = {lam_c.n , lam_c.s}')


#Diskussion

E_a_t = 8048.11
E_b_t = 8906.9

print("Energie Alpha", E_ae.n, E_ae.s)
print("Energie Beta", E_be.n, E_be.s)
ab_a = (E_a_t - E_ae) * 100 / E_a_t
ab_b = (E_b_t - E_be) * 100 / E_b_t

print(f'Abweichung der alpha Linie ', ab_a)
print(f'Abweichung der beta Linie ', ab_b)


