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

#a
R2a=np.array([332,664])
R3a=np.array([542,370])
R4a=np.array([458,630])

#b
R2b=np.array([205,503])
R3b=np.array([580,451])
R4b=np.array([420,549])
C2b=np.array([750e-9,399e-9])

#c
R2c=np.array([104])
R3c=np.array([775])
R4c=np.array([225])

#d
R2d=np.array([1000])
R3d=np.array([64])
R4d=np.array([638])

#e
RstrichE=332
Re=1000
Ce=295e-9


f=np.array([20,100,200,300,400,420,440,460,480,500,510,520,530,540,550,560,570,580,590,600,620,640,660,680,700,800,900,1000,1500,2000,3000,4000,5000,7500,10000])
U=np.array([3.2,3,2,1.35,0.64,0.56,0.44,0.34,0.25,0.16,0.12,0.08,0.044,0.005,0.036,0.08,0.12,0.15,0.18,0.22,0.28,0.36,0.44,0.5,0.56,0.8,1.05,1.25,2,2.4,2.7,2.8,2.9,3,2.9])

#print("a) 1.", 332 * (542/ 458))
#print("a) 2.", 664 * (370/630))
#
#print("b) 1. R_x : " , 205 * (580/420))
#print("b) 1. C_x : " , 750e-9 * (420/580))
#
#print("b) 2. R_x : " , 503 * (451/549))
#print("b) 2. C_x : " , 399e-9 * (548/452))
#
#
#print('c) R_x:' ,  104 * (775/225))
#print('c) L_x' , 14.6 *(225/775))
#
#print(' d) R_x: ' , 1000 * 64 / 638)
#print('d) L_x: ' , 1000 * 64 * 399e-9)

#####RECHNUNGEN#######
def rech(a,b,c):
    return (a*b)/c


print("Messung a: Wheatstone\n  Wert 12\n")
theo=392.9
a1=1
a2=1
print(f'Wert1: {a1}\nWert2: {a2}\n')
print(f'Theo: {theo}')
print(f'abw1: {(theo-a1)/theo}')
print(f'abw2: {(theo-a2)/theo}')

print("\n\nMessung b: kapazität\n  Wert 9 Teil 1\n")
theo1=464
theo2=433e-9
b1=1
b2=1
print(f'Wert1: {b1}\nWert2: {b2}\n')
print(f'TheoR: {theo1}')
print(f'abw: {(theo1-b1)/theo1}\n')
print(f'Theoc: {theo2*10**9}nF')
print(f'abw: {(theo2-b2)/theo2}')

print("\nMessung b: kapazität\n  Wert 9 Teil 2\n")
theo1=413.2
theo2=483.7e-9
b1=1
b2=1
print(f'Wert1: {b1}\nWert2: {b2}\n')
print(f'TheoR: {theo1}')
print(f'abw: {(theo1-b1)/theo1}\n')
print(f'TheoC: {theo2*10**9}nF')
print(f'abw: {(theo2-b2)/theo2}')

print("\n\nMessung c: Indukt\n Wert 18\n")
theo1=108.7
theo2=26.9e-3
c1=1
c2=1
print(f'Wert1: {c1}\nWert2: {c2}\n')
print(f'TheoR: {theo1}')
print(f'abw: {(theo1-c1)/theo1}\n')
print(f'TheoL: {theo2*10**3}mL')
print(f'abw: {(theo2-c2)/theo2}')

print("\nMessung d: maxwell\n Wert 18  \n")
d1=1
d2=1
print(f'Wert1: {d1}\nWert2: {d2}\n')
print(f'TheoR: {theo1}')
print(f'abw: {(theo1-d1)/theo1}\n')
print(f'TheoL: {theo2*10**3}mL')
print(f'abw: {(theo2-d2)/theo2}')

#e
print("\nMessung e: Wien-Robinson\n")
omega0=1/(Re*Ce)
omega0=omega0/(2*np.pi)
print("omega0:",omega0)
def func(ohm,omega0): 
    ohm=ohm/omega0
    return(1/9 * (ohm**2-1)**2/((1-ohm**2)**2+9*ohm**2) )  


table ={ 'delg':f, 'delr':U, }
print("\n ",tabulate (table, tablefmt="latex"),"\n")


########Grafiken########
x=np.linspace(f[0],f[-1],1000)
plt.figure()
plt.plot(f,U/np.sqrt(8),"x",label="Messwerte")
plt.plot(x,func(x,omega0))
plt.xscale('log')
plt.xlabel("f [Hz]")
#plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
#plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
#plt.ylabel(r"$\phi$ [rad]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot4.pdf")