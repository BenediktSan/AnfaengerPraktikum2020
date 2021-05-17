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

#####MEsSWERTE#########

del1=1
U1=1

del2=1
del2=1




####mittlere freie weglänge#####

T=1
p=(5.5*10^7*np.exp(-6876/T))e-3 #in bra
omega=(0.0029/p)e-2 #in meter
a=10^-2             #in meter

print("\n\n######Mittlere freie Weglänge#####\n")
table1 ={ 'T':T, 'omeag':omega,'verhältnis':a/omega }
print("\n ",tabulate (table1, tablefmt="latex"))


#####differentiele Energieverteilung######
print("\n\n######Differentielle Energieverteilung#####\n")


























#########PLOTS#########


#plt.figure()
#plt.plot(t,np.log(U_),"x",label="Messwerte")
#plt.plot(x1,huell(x1,*params1),"g",label="Fit-Funktion")
##plt.plot(plot0,-huell(plot0,*params),"g")
#plt.xlabel("t [s]")
#plt.ylabel(r'$\ln\left({\frac{U}{U_0}}\right)$')
#plt.tight_layout()
#plt.legend()
#plt.savefig("build/plots/plot0.pdf")

plt.plot(U1, del1, 'rx', label='Messdaten')
plt.ylabel(r'\frac{\increment y}{\increment x} [EINHEIT]')
plt.xlabel(r'$U_A$')
plt.yscale('log')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

plt.plot(U2, del2, 'rx', label='Messdaten')
plt.ylabel(r'\frac{\increment y}{\increment x} [EINHEIT]')
plt.xlabel(r'$U_A$')
plt.yscale('log')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2.pdf')



#######TABELLEN########


#np.savetxt(
#    'build/f.txt',
#    np.column_stack([U2,U2/U2[0], f1]),
#    fmt=['%.3f', '%.3f', '%.3f'],       
#    delimiter=' & ',
#    header='U2,U/U0,f',
#)