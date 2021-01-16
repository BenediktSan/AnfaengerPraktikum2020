import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy

        #Daten auslesen

p = np.load('python/variables/p_2.npy')
T = np.load('python/variables/T_2.npy')

#Temp in °K

umr=np.linspace(1,1,T.size)*273.15
T = T + umr

#Druck in pascal
p = p*1e5
#print(np.log(p))
#print(1/T)

#Ausgleichsrechnung für L
#Verdampfungswärme L[Joule/mol] R[Joule/mol*K]

print('\n\n Werte für 1 bar')

param, _1 = np.polyfit(1/T,np.log(p), deg=1, cov=True)
L1=-1*param[0]*const.gas_constant
err = np.sqrt(np.diag(_1))
print("\nParam=",param)
print("err=", err)
print(f"L1={L1:.8f} 8te nachkommastelle\n")
uparam=unp.uarray(param,err)
uL1=-1*uparam[0]*const.gas_constant

La=const.gas_constant * 373
uLa=unc.ufloat(La,0)
uLi=uL1-uLa
uLimolekül=uLi/(const.Avogadro*const.elementary_charge)

print(f'\n \n L1= {uL1:.4f} J/mol \n La={uLa:.4f} J/mol \n Li= {uLi:.4f} J/mol\n Li pro Molekül in eV: {uLimolekül:.4f} eV\n')
#25  43990
#40  43350
#60  42483
#80  41585
#120 39684  
z=(43990+43350+42483+41585+40657+39684)/6
print("Mittelwert(?): ",z)
#print("komischer testmittelwert: ",(43990*3/4+43350+42483+41585+39684)/5)
uz=unc.ufloat(z,0)
#uz2=unc.ufloat((43990*3/4+43350+42483+41585+39684)/5,0)
print("Abweichnung vom Mittelwert: ",((uz/uL1)-1)*100)
#print("Testabweichung: ",((uz2/uL1)-1)*100)



#plotting
x1=np.linspace(1/T[-1],1/T[0],1000)



plt.figure()
plt.plot(1/T,np.log(p),".",label="Werte von T")
plt.plot(x1, param[0]*x1 + param[1], label="Regression zu T")
plt.xlabel("1/T [1/K]")
plt.ylabel("log(p/p0)")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot1.pdf")



#Variablen speichern
#np.save('python/variables/L1.npy', L1, allow_pickle=False)