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



########MESSWERTE#######

def rel(wert,theo):
    a=(theo-wert)/theo
    print(f'Relative Abweichung: {unp.nominal_values(a):.3f} /pm {unp.std_devs(a):.3f}')
    return
    






###########AUSWERTUNG#############

#table ={ 'delg':f, 'delr':U, }
#print("\n ",tabulate (table, tablefmt="latex"),"\n")







##########PLOTS###########
x=np.logspace(1,4,1000)
plt.figure()
plt.plot(f,1/(10),"x",label="Messwerte")
plt.xscale('log')
plt.xlabel(r"$\Omega=\frac{\nu}{\nu_0}$")
plt.ylabel(r"$\frac{U_Br}{U_0}$")
#plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
#plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot1.pdf")