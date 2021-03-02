import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties import unumpy
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy

#Physik 3 Blatt 8

def t(x):
    return np.log( np.sqrt(((1+np.sqrt(2)) / ( (1/np.sin(x)) + (np.cos(x)/np.sin(x))))**2) ) 

x1=np.linspace(0.00001,0.99999*np.pi,100)
#np.linspace(1.00001*np.pi,1.99*np.pi,100),np.linspace(2.00001*np.pi,2.99*np.pi,100)]
x1=np.append(x1,np.linspace(1.0000001*np.pi,1.9999999*np.pi,100))
x1=np.append(x1,np.linspace(2.0000001*np.pi,2.9999999*np.pi,100))
x1=np.append(x1,np.linspace(3.0000001*np.pi,3.9999999*np.pi,100))
x1=np.append(x1,np.linspace(4.0000001*np.pi,4.9999999*np.pi,100))   

plt.figure()
plt.plot(x1,t(x1),label="t")
plt.xlim(0,5*np.pi)
plt.ylim(-10,10)

plt.xticks([np.pi,2*np.pi,3*np.pi,4*np.pi,5*np.pi,],[r"$\pi$",r"$2\pi$",r"$3\pi$",r"$4\pi$",r"$5\pi$"])
plt.legend()
plt.savefig("t(x).pdf")

x2=np.linspace(-2*np.pi,2*np.pi,200)

plt.figure()
x3=np.linspace(0,2*np.pi,20)
plt.plot(x2+x3[1],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[2],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[3],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[4],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[5],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[6],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[7],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[8],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[9],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[10],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[11],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[12],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[13],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[14],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[15],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[16],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[17],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[18],np.sin(x2),label="sinus(x)")
plt.plot(x2+x3[19],np.sin(x2),label="sinus(x)")
#plt.plot(x2+x3[20],np.sin(x2),label="sinus(x)")
plt.xlim(0,2*np.pi)
#plt.xticks([-2*np.pi,-1*np.pi,0*np.pi,1*np.pi,2*np.pi,],[r"$-2\pi$",r"$-1\pi$",r"$0$",r"$1\pi$",r"$2\pi$"])
#plt.legend()
plt.savefig("sinus.pdf")