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


U , N = np.genfromtxt("Versuchsdateien/Kennlinie.dat", unpack=True)



##  a)
U1=U[5:32]
N1=N[5:32]

var , _1 = np.polyfit(U1,N1,deg=1, cov=True)
err1=np.sqrt(np.diag(_1))
print(var)
print(err1)
m=var[0]
b=var[1]

plt.figure()
plt.errorbar(U,N,yerr=np.sqrt(N),fmt="+",label="Daten")
plt.plot(U1,U1*m+b,label="fit")
plt.legend()
plt.savefig("build/plots/a")


## b) 
# entfällt?


## c)

N_1 = 96041

N_2 = 76518

N_3 = 158479

T = (N_1 + N_2 + N_3)/(2*N_1*N_2)

print(T)



## d)

e = 1.602e-19

U2 , I = np.genfromtxt("Versuchsdateien/Zaehlrohrstrom.dat", unpack=True)
I=I*1e-6
N2=N[3:40:5]

#print(N2)

N2 = unp.uarray(N2,np.sqrt(N2))
I = unp.uarray(I,np.ones(8)*0.05*1e-6)
Z_q = I/(e*N2)

#print(Z_q)

plt.figure()
plt.errorbar(U2,unp.nominal_values(Z_q),yerr=unp.std_devs(Z_q),fmt=".",label="freigesetzte Ladungen")
plt.legend()
plt.savefig("build/plots/d")

np.savetxt(
    'build/Strom.txt',
    np.column_stack([U2,unp.nominal_values(N2),unp.nominal_values(I)*1e6]),
    fmt=['%.4f','%.1f', '%.2f'],       
    delimiter=' & ',
    header='Spannung,Stromstärke',
)

np.savetxt(
    'build/Elektronenzahl.txt',
    np.column_stack([U2,unp.nominal_values(Z_q),unp.std_devs(Z_q)]),
    fmt=['%.4f', '%.4f','%.4f'],       
    delimiter=' & ',
    header='U,Z value,Z error',
)

np.savetxt(
    'build/Charakteristik.txt',
    np.column_stack([U,N]),
    fmt=['%.4f', '%.4f'],       
    delimiter=' & ',
    header='U,Z value,Z error',
)