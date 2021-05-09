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


####### Messwerte einlesen

U1=np.load('python/variables/U1.npy')
U2=np.load('python/variables/u2.npy')

t=np.load('python/variables/t.npy')
f1=np.load('python/variables/f1.npy')


phi=np.load('python/variables/phi.npy')
f2=np.load('python/variables/f2.npy')


U_0=1





###logarithmischer fit

def huell(t,RC,b):
    return ((-1/RC)*t+b)

U_=U1/U_0


params1, _1 =curve_fit(huell,t,np.log(U_),p0=(0.001,0.002))
err1 = np.sqrt(np.diag(_1))
uparams1 = unp.uarray(params1,err1)

print(f'\nFit:\nRC= {uparams1[0]:.4f}s \nb={uparams1[1]:.5f}\n')


###methode über frequenz


def freq(f,R):
    return 1/np.sqrt(1+f**2*R**2)

params2, _2 =curve_fit(freq,f1,U2,p0=(-0.01))
err2 =np.sqrt(np.diag(_2))
uparams2=unp.uarray(params2,err2)

print(f'\nFit:\nRC= {uparams2[0]:.4f} ')
print(f'RC={uparams2[0]*10**3} *10^-3 s')




#####Phasenverschiebung

def arc (f, a, m):
    return a*np.arctan(m*f)

params3, _3 =curve_fit(arc,f2,phi)
err3 =np.sqrt(np.diag(_3))
uparams3=unp.uarray(params3,err3)

print(f'\nFit:\na= {uparams3[0]:.4f} \nm={uparams3[1]:.5f}s')
print(f'RC={uparams3[1]*10**3} *10^-3 s')

######Plots


x1=np.linspace(0,t[-1],150)
x2=np.logspace(0,6,1000)
x3=np.logspace(0,5,1000)

plt.figure()
plt.plot(t,np.log(U_),"x",label="Messwerte")
plt.plot(x1,huell(x1,*params1),"g",label="Fit-Funktion")
#plt.plot(plot0,-huell(plot0,*params),"g")
plt.xlabel("t [s]")
plt.ylabel(r'$\ln\left({\frac{U}{U_0}}\right)$')
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot0.pdf")

plt.figure()
plt.plot(f1,U2,"x",label="Messwerte")
plt.plot(x2,freq(x2,*params2),"g",label="Fit-Funktion")
#plt.plot(f1,freq(f1,*params2),"g",label="Fit-Funktion")
#plt.plot(x2,freq1(x2,*params2),"g",label="Fit-Funktion")
#plt.plot(plot0,-huell(plot0,*params),"g")
plt.xlabel(r'f [Hz]')
plt.ylabel(r'U [V]')
plt.xscale('log')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig("build/plots/plot1.pdf")

plt.figure()
plt.plot(f2,phi,"x",label="Messwerte")
plt.plot(x3,arc(x3,*params3))
plt.xscale('log')
plt.xlabel("f [Hz]")
#plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
#plt.ylabel(r"$\phi$ [rad]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot2.pdf")



phineu=np.array([phi[0],phi[1],phi[2],phi[4],phi[5],phi[6],phi[12],phi[13],phi[14]])
Uneu=np.array([U2[1],U2[2],U2[4],U2[7],U2[8],U2[9],U2[12],U2[13],U2[14]])



RC = params1[0]
x = np.linspace(0, 50000, 10000000)
phi = np.arcsin(((x*RC)/(np.sqrt(1+x**2*(RC)**2))))
y = 1/(np.sqrt(1+x**2*(RC)**2))



plt.polar(phineu, Uneu,'xr', label=r'${Messwerte} \; \phi $')
plt.polar(phi,y,'b-', label=r'$Messwerte  \; U_C \ /\  U_0$')
plt.xticks([0, np.pi/4, np.pi/2,  3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4],[r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$",  r"$\frac{3\pi}{4}$", r"$\pi$", r"$\frac{5\pi}{4}$", r"$\frac{3\pi}{2}$", r"$\frac{7\pi}{4}$"])
plt.xlabel(r"U")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.tight_layout()
plt.legend(loc="best")
plt.savefig("build/plots/plot3.pdf")

table ={ 'delg':Uneu, 'delr':phineu, }
print("\n ",tabulate (table, tablefmt="latex"))
