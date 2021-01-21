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
#print(f'\nangepasste messwerte:\nNv_= {Nv_} \n')
#print(f'\nangepasste messwerte:\nNv_= {unp.log(Nv_)} \n')


#fit
def huell(t,mu,A0):
    return (A0*np.exp(-mu*t))

params1, _1 =curve_fit(huell,tv,unp.nominal_values(Nv_),p0=(0.0035,205))
err1 =np.sqrt(np.diag(_1))
uparams1=unp.uarray(params1,err1)
print(f'\nFit1:\nmu= {uparams1[0]:.5f} 1/s \nA0={uparams1[1]:.5f}\n')

#Haltbwertszeit

TV=(np.log(2))/uparams1[0]
print(f'\nHalbwertszeit Vanadium= {TV:.5f} s \n')

#Halbwertszeit genauer

params1_, _1_ =curve_fit(huell,tv[0:14],unp.nominal_values(Nv_[0:14]),p0=(0.0035,205))
err1_ =np.sqrt(np.diag(_1_))
uparams1_=unp.uarray(params1_,err1_)
print(f'\nFit1 genauer:\nmu= {uparams1_[0]:.5f} 1/s \nA0={uparams1_[1]:.5f}\n')

TV_=(np.log(2))/uparams1_[0]
print(f'\nHalbwertszeit Vanadium genauer= {TV_:.5f} s \n')





#RHODIUM

print('\nRHODIUM')


Nr_=unp.uarray(Nr-0.5*NU_V,np.sqrt(Nr-0.5*NU_V))

#neuer Startwert t=300s also slot 20

params2, _2 =curve_fit(huell,tr[20:],unp.nominal_values(Nr_[20:]),p0=(0.0025,72))
err2 =np.sqrt(np.diag(_2))
uparams2=unp.uarray(params2,err2)
print(f'\nFit2:\nmu= {uparams2[0]:.5f} 1/s \nA0={uparams2[1]:.5f}\n')

TR=(np.log(2))/uparams2[0]
print(f'\nHalbwertszeit Rhodium 104= {TR:.5f} s \n')

#kurzlebiges Isotop






#PLOTTEN

#plotparameter
höhe=np.linspace(1,6,100)
tcut=np.linspace(250,250,100)

#plots


#Vanadium
plt.figure()
plt.errorbar(tv,unp.nominal_values(unp.log(Nv_)),yerr=unp.std_devs(unp.log(Nv_)),fmt='.',label="Messwerte")
#plt.plot(tv,np.log(Nv_),"x",label="Messwerte")
plt.plot(tv,np.log(huell(tv,*params1)),label="Fit-Funktion")
plt.plot(tv,np.log(huell(tv,*params1_)),label="Fit-Funktion mit doppelter Halbwertszeit")
#plt.yticks([0,np.pi/4,np.pi/2,(3*np.pi)/4,np.pi],[r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",r"$\pi$"])
plt.ylabel(r"$ln(N_V-N_0)$")
plt.xlabel(r"$t/[s]$")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot1.pdf")



#Rhodium
plt.figure()
plt.errorbar(tr,unp.nominal_values(unp.log(Nr_)),yerr=unp.std_devs(unp.log(Nr_)),fmt='.',label="Messwerte")
#plt.plot(tr,np.log(Nr),"x",label="Messwerte")
plt.plot(tr,np.log(huell(tr,*params2)),label=r"Fit-Funktion für 104 Rh")
plt.plot(tcut,höhe,"g--",linewidth=0.6,label=r"t'")
plt.ylabel(r"$ln(N_V-N_0)$")
plt.xlabel(r"$t/[s]$")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot2.pdf")


#WERTE SPEICHERN

np.savetxt(
    'build/tab/Vanadium_modifiziert.txt',
    np.column_stack([tv,Nv,unp.nominal_values(Nv_), unp.std_devs(Nv_)]),
    fmt='%-20s', 
    delimiter=' & ',
    header='t,Nv,Nv_, err',
)

np.savetxt(
    'build/tab/Vanadium_ln.txt',
    np.column_stack([tv,unp.nominal_values(unp.log(Nv_)), unp.std_devs(unp.log(Nv_))]),
    fmt='%-20s', 
    delimiter=' & ',
    header='t,log(Nv_),log(err)',
)


np.savetxt(
    'build/tab/Rhodium_modifiziert.txt',
    np.column_stack([tr,Nr,unp.nominal_values(unp.log(Nr_)), unp.std_devs(unp.log(Nr_))]),
    fmt='%-20s', 
    delimiter=' & ',
    header='t,Nr,Nv_,err',
)