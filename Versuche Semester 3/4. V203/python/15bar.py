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
p = p*1e5


#Ausgleichspolynom

param, _1 = np.polyfit(T,p, deg=3, cov=True)
err = np.sqrt(np.diag(_1))
uparam=unp.uarray(param,err)
print('\n\n15 bar')
print("\nPolynomwerte in pa/T^3, pa/T^2, pa/T und pa:\n", uparam,'\n')


plt.figure()
plt.plot(T,p,"x",label="Messwerte des Drucks")
plt.plot(T, param[0]*T**3 + param[1]*T**2+param[2]*T+param[3], label="Ausgleichskurve")
plt.xlabel("T [K]")
plt.ylabel("p [bar]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot2.pdf")



R=const.gas_constant
C=0.9
def L1(x,a,b,c,d):
    return (((R*x/2)+np.sqrt((R*x/2)**2-0.9*(a*x**3 + b*x**2+c*x+d)))*((3*a*x**3+2*b*x**2+c*x)/(a*x**3+b*x**2+c*x+d)))


def L2(x,a,b,c,d):
    return (((R*x/2)-np.sqrt((R*x/2)**2-0.9*(a*x**3 + b*x**2+c*x+d)))*((3*a*x**3+2*b*x**2+c*x)/(a*x**3+b*x**2+c*x+d)))




#Theoriewerte
xtheo=np.array([120,140,160,180,200])
ytheo=np.array([39.684,38.643,37.518,36.304,34.962])

umr=np.linspace(1,1,xtheo.size)*273.15
xtheo= xtheo + umr
ytheo =ytheo *1000







x= np.linspace(T[0],T[-1],1000)


plt.figure()
plt.plot(x, L1(x, *param), label="Berechnete L Werte")
plt.plot(xtheo, ytheo,"x", label="Theoriewerte")
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot3+.pdf")

plt.figure()
plt.plot(x, L2(x, *param), label="Berechnete L Werte")
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot3-.pdf")




#L-Werte auslesen


np.savetxt(
    'L-werte.txt',
    np.column_stack([xtheo, ytheo,L1(xtheo, *param),((L1(xtheo, *param)/ytheo)-1)*100 ]),
    fmt=['%.1f', '%.3f', '%.3f', '%.1f'],       
    delimiter=' & ',
    header='T,L_theo,L_fit,err',
)