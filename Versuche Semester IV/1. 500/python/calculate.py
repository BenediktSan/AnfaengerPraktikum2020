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

if os.path.exists("python/tabellen") == False:
    os.mkdir("python/tabellen")

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
print("a_ge", a_ge*1e5)
b_ge = ufloat(params_ge[1], errors_ge[1])
print("b_ge", b_ge)
#print(params_ge,errors_ge)

#Fit gruenes Licht
params_gr , ma_gr = np.polyfit(U_gr,np.sqrt(I_gr), deg =1, cov = True)
errors_gr = np.sqrt(np.diag(ma_gr))

a_gr = ufloat(params_gr[0], errors_gr[0])
print("a_gr", a_gr*1e5)
b_gr = ufloat(params_gr[1], errors_gr[1])
print("b_gr", b_gr)
#Fit violettes Licht 
params_vi , ma_vi = np.polyfit(U_vi,np.sqrt(I_vi), deg =1, cov = True)
errors_vi = np.sqrt(np.diag(ma_vi))

a_vi = ufloat(params_vi[0], errors_vi[0])
print("a_vi",a_vi*1e5)
b_vi = ufloat(params_vi[1], errors_vi[1])
print("b_vi", b_vi*1e5)
#Grenzspannungen
Ug_ge=-b_ge/a_ge
Ug_gr=-b_gr/a_gr
Ug_vi=-b_vi/a_vi
print("Nullstelle gelb", -b_ge/a_ge)
print("Nullstelle grün", -b_gr/a_gr)
print("Nullstelle violett", -b_vi/a_vi)

# gelbes Licht
plt.figure()
plt.plot(U_ge,I_ge,".", label="gelb")
plt.xlabel("U / V")
plt.ylabel("I / A")
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
plt.xlabel("U / V")
plt.ylabel(r'I / $A^{\frac{1}{2}}$')
plt.legend()
plt.tight_layout()
plt.savefig("build/plots/sqrtgelb.pdf")

# grünes Licht
x2=np.linspace(0,0.6)
plt.figure()
plt.plot(x2, x2*params_gr[0]+params_gr[1],label="fit")
plt.plot(U_gr, np.sqrt(I_gr),".", label="grün")
plt.ylim(0,9e-5)
plt.xlabel("U / V")
plt.ylabel(r'I / $A^{\frac{1}{2}}$')
plt.legend()
plt.tight_layout()
plt.savefig("build/plots/sqrtgreen.pdf")

#violettes Licht
x3=np.linspace(0,1.25)
plt.figure()
plt.plot(x3, x3* params_vi[0] + params_vi[1],label="fit")
plt.plot(U_vi, np.sqrt(I_vi),".", label="violett")
plt.ylim(0,0.00013)
plt.xlabel("U / V")
plt.ylabel(r'I / $A^{\frac{1}{2}}$')
plt.legend
plt.tight_layout()
plt.savefig("build/plots/sqrtviolett.pdf")


#b)
Ugs = np.array([Ug_ge.n,Ug_gr.n,Ug_vi.n])
lam = np.array([580e-9,546e-9,435e-9])

e = 1.602176634e-19 
c = 299792458
params_Ug , ma_Ug = np.polyfit(c/lam ,Ugs , deg =1, cov = True)
errors_Ug = np.sqrt(np.diag(ma_Ug))
frac = ufloat(params_Ug[0], errors_Ug[0])
Ak = ufloat(params_Ug[1], errors_Ug[1]) * c / e
print("berechnetes h/e0", (frac/e).n, (frac/e).s )
print("Theorie Wert", (6.62607015e-34/(-1.602176634e-19))/e)
print("prozentuale Abweichung", 1 + frac/(6.62607015e-34/(-1.602176634e-19)))
print("Austrittsarbeit ", Ak)
print("a", frac)
print("b", Ak)

x4=np.linspace(5e14,7e14)


plt.figure()
plt.plot(c/lam,Ugs,".",label="Werte")
plt.plot(x4, x4 * params_Ug[0] + params_Ug[1], label="Fit")
plt.xlabel(r'$\nu \quad / \quad s^{-1}$')
plt.ylabel(r'$ U_g \quad / \quad V$')
plt.legend()
plt.savefig("build/plots/Grenz.pdf")

#print(I_gr)
np.savetxt(
    'python/tabellen/gelb.txt',
    np.column_stack([U_ge,I_ge*1e9]),
    fmt=['%.2f', '%.4f'],       
    delimiter=' & ',
    header='U_ge,I_ge',
)

np.savetxt(
    'python/tabellen/green.txt',
    np.column_stack([U_gr,I_gr*1e9]),
    fmt=['%.2f', '%.4f'],       
    delimiter=' & ',
    header='U_gr,I_gr',
)

np.savetxt(
    'python/tabellen/violett.txt',
    np.column_stack([U_vi,I_vi*1e9]),
    fmt=['%.2f', '%.4f'],       
    delimiter=' & ',
    header='U_vi,I_vi',
)