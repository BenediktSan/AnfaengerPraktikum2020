import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import sympy


        #Daten auslesen

p = np.load('python/variables/p_2.npy')
T = np.load('python/variables/T_2.npy')

#Temp in °K

umr=np.linspace(1,1,T.size)*273.15
T = T + umr
#Druck in pascal
p = p*1e5
print(np.log(p))
print(1/T)

#Ausgleichsrechnung für L
#Verdampfungswärme L[Joule/mol] R[Joule/mol*K]

#param, err = np.polyfit(1/T,np.log(p), deg=1, cov=True)
#L1=-1*parameter3[0]*8.314
#print("'\n'Param=",param)
#print("err=",err)
#print(f"L1={L1:.5f},'\n'")








#plotting
x1=np.linspace(0,1/T[0],1000)



plt.figure()
plt.plot(1/T,np.log(p),".",label="Werte von T")
#plt.plot(x1, param[0]*x1 + param[1], label="Regression zu T")
#plt.plot(1/T2,P2,".",label="Werte von T2")
#plt.plot(x3, parameter4[0]*x3 + parameter4[1], label="Regression zu 2")
plt.xlabel("1/T [1/K]")
plt.ylabel("log(p/p0)")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot1.pdf")
