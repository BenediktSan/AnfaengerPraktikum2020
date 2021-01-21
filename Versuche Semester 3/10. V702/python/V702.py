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

if os.path.exists("build/tab") == False:
    os.mkdir("build/tab")


tv , Nv = np.genfromtxt("Versuchsdateien/Vanadium.dat", unpack=True)
tr , Nr = np.genfromtxt("Versuchsdateien/Rhodium.dat", unpack=True)


#Werte einlesen

NU = np.array([129, 143, 144, 136, 139, 126, 158]) #über t=300s
NU =NU/10 #auf 30s

#VANADIUM
print('\nVANADIUM')
NU_V=np.array(np.mean(NU))
print(f'\nNullrate VA pro 30s:\nNU_V= {NU_V:.4f} \n')

Nv_=unp.uarray(Nv-NU_V,np.sqrt(Nv-NU_V))
print(f'\nangepasste messwerte:\nNv_= {Nv_} \n')
print(f'\nangepasste messwerte:\nNv_= {unp.log(Nv_)} \n')


#fit

err =np.sqrt(np.diag(_1))
uparams1=unp.uarray(params1,err)
print(f'\nFit:\nmu= {uparams1[0]:.5f}1/s \nb={uparams1[1]:.5f}\n')




#RHODIUM





#PLOTTEN

#plotparameter


#plots


#Vanadium
plt.figure()
plt.errorbar(tv,unp.nominal_values(unp.log(Nv_)),yerr=unp.std_devs(unp.log(Nv_)),fmt='.',label="Messwerte")
#plt.plot(tv,np.log(Nv_),"x",label="Messwerte")
plt.plot(tv,params1[0]*tv+params1[1],label="Fit-Funktion")
#plt.yticks([0,np.pi/4,np.pi/2,(3*np.pi)/4,np.pi],[r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",r"$\pi$"])
plt.xlabel(r"$ln(N_V-N_0)$")
plt.ylabel(r"$t/[s]$")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot1.pdf")


#WERTE SPEICHERN
np.savetxt(
    'build/tab/Vanadium_modifiziert.txt',
    np.column_stack([tv,unp.nominal_values(Nv_), unp.std_devs(Nv_)]),
    fmt='%-20s', 
    delimiter='    & ',
    header='t,Nv_, err',
)
