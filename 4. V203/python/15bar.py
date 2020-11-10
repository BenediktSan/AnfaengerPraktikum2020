import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy



        #Daten auslesen

p = np.load('python/variables/p_1.npy')
T = np.load('python/variables/T_1.npy')

#Temp in °K

umr=np.linspace(1,1,T.size)*273.15
T = T + umr

#Druck in pascal
#p = p*1e5


#Ausgleichspolynom

param, _1 = np.polyfit(T,p, deg=3, cov=True)
err = np.sqrt(np.diag(_1))

uparam=unp.uarray(param,err)
print("Polynomwerte in pa/T^3, pa/T^2, pa/T und pa:", uparam)


plt.figure()
plt.plot(T,p,"x",label="Messwerte des Drucks")
plt.plot(T, param[0]*T**3 + param[1]*T**2+param[2]*T+param[3], label="Ausgleichskurve")
plt.xlabel("T [K]")
plt.ylabel("p [bar]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot2.pdf")



R=const.gas_constant
C= 0.9
def L1(x,a,b,c,d):
    return ((R*x/2)+np.sqrt((R*x/2)**2-C*(a*x**3 + b*x**2+c*x+d))*((3*a*x**2+2*b*x+c)/(a*x**3+b*x**2+c*x+d)))


def L2(x,a,b,c,d):
    return ((R*x/2)-np.sqrt((R*x/2)**2-C*(a*x**3 + b*x**2+c*x+d))*((3*a*x**2+2*b*x+c)/(a*x**3+b*x**2+c*x+d)))








plt.figure()
plt.plot(T, L1(T, *param),"x", label="Berechnete L Werte")
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot3+.pdf")

plt.figure()
plt.plot(T, L2(T, *param),"x", label="Berechnete L Werte")
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot3-.pdf")