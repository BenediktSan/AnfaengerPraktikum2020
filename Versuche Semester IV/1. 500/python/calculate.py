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

#einlesen
U_ge , I_ge = np.genfromtxt("gelb.dat", unpack=True)
I_ge *=1e-9

U_gr , I_gr = np.genfromtxt("green.dat", unpack=True)
I_gr *=1e-9

U_vi , I_vi = np.genfromtxt("violett.dat", unpack=True)
I_vi *=1e-9

#Fit gelbes Licht
params_ge , ma_ge = np.polyfit(U_ge[6:17],np.sqrt(I_ge[6:17]), deg =1, cov = True)
errors_ge = np.sqrt(np.diag(ma_ge))
a_ge = ufloat(params_ge[0], errors_ge[0])
b_ge = ufloat(params_ge[1], errors_ge[1])
#print(params_ge,errors_ge)

#Fit gruenes Licht
params_gr , ma_gr = np.polyfit(U_gr,np.sqrt(I_gr), deg =1, cov = True)
errors_gr = np.sqrt(np.diag(ma_gr))

a_gr = ufloat(params_gr[0], errors_gr[0])
b_gr = ufloat(params_gr[1], errors_gr[1])

#Fit violettes Licht 
params_vi , ma_vi = np.polyfit(U_vi,np.sqrt(I_vi), deg =1, cov = True)
errors_vi = np.sqrt(np.diag(ma_vi))

a_vi = ufloat(params_vi[0], errors_vi[0])
b_vi = ufloat(params_vi[1], errors_vi[1])

#Grenzspannungen
Ug_ge=-b_ge/a_ge
Ug_gr=-b_gr/a_gr
Ug_vi=-b_vi/a_vi
print("Nullstelle gelb", -b_ge/a_ge)
print("Nullstelle grün", -b_gr/a_gr)
print("Nullstelle violett", -b_vi/a_vi)

# gelbes Licht
plt.figure()
plt.plot(U_ge,I_ge, label="gelb")
plt.savefig("build/plots/gelb.pdf")

# grünes Licht
plt.figure()
plt.plot(U_gr, I_gr, label="grün")
plt.savefig("build/plots/green.pdf")

#violettes Licht
plt.figure()
plt.plot(U_vi, I_vi, label="violett")
plt.savefig("build/plots/violett.pdf")


## Wurzel Relation
# gelbes Licht
x1=np.linspace(-1.1,1)
plt.figure()
plt.plot(x1, x1*params_ge[0]+params_ge[1],label= "fit")
plt.ylim(0,0.0002)
plt.xlim(-1.1,0.7)
plt.plot(U_ge[6:17],np.sqrt(I_ge[6:17]),".", label="gelb")
plt.legend()
plt.savefig("build/plots/sqrtgelb.pdf")

# grünes Licht
x2=np.linspace(0,0.6)
plt.figure()
plt.plot(x2, x2*params_gr[0]+params_gr[1],label="fit")
plt.plot(U_gr, np.sqrt(I_gr),".", label="grün")
plt.ylim(0,9e-5)
plt.legend()
plt.savefig("build/plots/sqrtgreen.pdf")

#violettes Licht
x3=np.linspace(0,1.25)
plt.figure()
plt.plot(x3, x3* params_vi[0] + params_vi[1],label="fit")
plt.plot(U_vi, np.sqrt(I_vi),".", label="violett")
plt.ylim(0,0.00013)
plt.legend
plt.savefig("build/plots/sqrtviolett.pdf")


#b)
Ugs = np.array([Ug_ge.n,Ug_gr.n,Ug_vi.n])
lam = np.array([580e-9,546e-9,435e-9])

params_Ug , ma_Ug = np.polyfit(lam ,Ugs , deg =1, cov = True)
errors_Ug = np.sqrt(np.diag(ma_Ug))
print("h/e0",params_Ug[0])
print(6.62607015e-34/-1.602176634e-19 )
print(params_Ug[0]/(6.62607015e-34/-1.602176634e-19))

x4=np.linspace(4.3e-7,6e-7)

plt.figure()
plt.plot(lam,Ugs,".",label="Werte")
plt.plot(x4, x4 * params_Ug[0] + params_Ug[1])
plt.savefig("build/plots/Grenz.pdf")