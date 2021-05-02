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


params1, _1 =curve_fit(huell,t,np.log(U_),p0=(0.001,0.002)
err1 =np.sqrt(np.diag(_1))
uparams1=unp.uarray(params1,err1)

print(f'\nFit:\nRC= {uparams1[0]:.4f}s \nb={uparams1[1]:.5f}\n')


###methode über frequenz


def freq(f,A,B):
    return (np.exp(-A*f+B))



params2, _2 =curve_fit(freq,f1,U2,p0=(0.003,2))
err2 =np.sqrt(np.diag(_2))
uparams2=unp.uarray(params2,err2)

print(f'\nFit:\na= {uparams2[0]:.4f}s \nb={uparams2[1]:.5f}\n')
print(f'RC={uparams2[0]e3} *10^3 s')


######Plots


x1=np.linspace(0,0.01,150)
x2=np.linspace(0,10e5,300)

plt.figure()
plt.plot(t,np.log(U_),"x",label="Messwerte")
plt.plot(x1,huell(x1,*params1),"g",label="Fit-Funktion")
#plt.plot(plot0,-huell(plot0,*params),"g")
plt.xlabel("t [s]")
plt.ylabel(r'\log{\frac{U}{U_0}}')
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot0.pdf")

plt.figure()
plt.plot(f1,U2,"x",label="Messwerte")
plt.plot(x1,freq(x1,*params2),"g",label="Fit-Funktion")
#plt.plot(plot0,-huell(plot0,*params),"g")
plt.xlabel(r'f [Hz]')
plt.ylabel(r'U [V]')
plt.xscale('log')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig("build/plots/plot1.pdf")

#plt.figure()
#plt.plot(fd,phi1,"x",label="Messwerte")
##plt.plot(plot1,sigmoid(plot1,*params3))
#plt.xscale('log')
#plt.xlabel("f [Hz]")
#plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
#plt.yticks([0,np.pi/4,np.pi/2,(3*np.pi)/4,np.pi],[r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",r"$\pi$"])
#plt.ylabel(r"$\phi$ [rad]")
#plt.tight_layout()
#plt.legend()
#plt.savefig("build/plots/plot3.pdf")