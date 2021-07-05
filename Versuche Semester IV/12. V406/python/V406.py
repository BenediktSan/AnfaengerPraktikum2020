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
L=1.472
lam=635e-9


#d in mm
d=np.array([25,23,21,19,17,15,13,11,10,9,8,7,6,5,4.5,4,3.5,3,2.5,2.25,2,1.75,1.5,1.25,1,0.75,0.5,0.25,0,
0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,3,3.5,4,4.5,5,6,7,8,9,10,11,13,15,17,19,21,23,25])
d[0:28]= -1* d[0:28]

#d=d+1
d = d * 10**-3




#I in micro 

dI=5.6 *10**-9

I2=np.array([0.00025,0.005,0.002,0.006,0.007,0.0045,0.013,0.0095,0.012,0.015,0.017,0.0135,0.014,0.025,0.135,0.02,0.31,0.42,0.52,0.595,0.61,
0.64,0.705,0.7,0.7,0.75,0.7,0.64,0.66,0.62,0.52,0.5,0.465,0.36,0.31,0.28,0.22,0.16,0.135,0.07,0.04,0.01,
0.016,0.022,0.033,0.0275,0.014,0.005,0.0085,0.012,0.008,0.0075,0.008,0.0025,0.005,0.0085,0.0015])



I1=np.array([0.003,0.0015,0.0015,0.007,0.0035,0.009,0.012,0.006,0.0175,0.032,0.032,0.016,0.0155,0.088,0.17,0.28,0.4,0.54,0.67,0.73,0.78,0.83,0.86,0.88,0.9,
0.89,0.88,0.85,0.8,0.76,0.7,0.64,0.56,0.5,0.42,0.36,0.29,0.23,0.18,0.095,0.04,0.015,0.01,0.019,0.044,0.047,0.027,0.01,0.0075,0.015,
0.0135,0.003,0.009,0.0045,0.003,0.005,0.001])


I1=I1 * 10**-6
I2=I2 * 10**-6
print("di ",dI)
print("L: ", L)


def rel(wert,theo):
    a=(theo-wert)/theo *100
    print(f'Relative Abweichung: {unp.nominal_values(a):.3f} /pm {unp.std_devs(a):.3f}\n')
    return
    






###########AUSWERTUNG#############

#table ={ 'delg':f, 'delr':U, }
#print("\n ",tabulate (table, tablefmt="latex"),"\n")

def einzel(phi1,b, a,test):
    lamda=lam
    phi=phi1-test
    uff=(a**2)*(b**2)*((lamda/(np.pi*b*np.sin(phi)))**2)
    teil2=(np.sin((np.pi*b*np.sin(phi))/lamda))**2
    return(uff*teil2)

def doppel(phi1,b,A_0,s,test):
    lamda=lam
    phi=(phi1-test)
    teil1=(A_0**2)*np.cos((np.pi*s*np.sin(phi)/lamda))**2
    teil2=(lamda/(np.pi*b*np.sin(phi)))**2
    teil3=np.sin((np.pi*b*np.sin(phi))/lamda)**2
    return(teil1*teil2*teil3)

phi=d/L




params, covariance =curve_fit(einzel,phi,I1,p0=[0.00018,4.578,-0.001])
errors = np.sqrt(np.diag(covariance))
print('breite des Spaltes:', params[0]*1000,'+-',errors[0]*1000)
rel(params[0],0.00015)
print('A_0:', params[1],'+-',errors[1])
print("versch:",params[2]*1000, '+-', errors[2]*1000)

#table ={ 'delg':d[0:29]*1000, 'delr':I2[0:29]*10**9,'delg2':d[29:]*1000, 'delr2':I2[29:]*10**9, }
#print("\n ",tabulate (table, tablefmt="latex"),"\n")
print("###################################")


params2, covariance2 =curve_fit(doppel,phi,I2,p0=[0.00017,0.0009, 0.001,-0.00064])
errors2 = np.sqrt(np.diag(covariance2))
print('breite des Spaltes:10^-3* ', params2[0]*1000,'+-',errors2[0]*1000)
rel(params2[0],0.00015)
print('A_0:10^-3* ', params2[1]*1000,'+-',errors2[1]*1000)
print("s:10^-3* ",params2[2]*1000, '+-', errors2[2]*1000)
rel(params2[2],0.001)
print("versch:10^-3* ",params2[3]*1000, '+-', errors2[3]*1000)

#print("Breite: ",params2[0])
#print("A_0: ",params2[1])
#print("s: ",params2[2])
#print("versch: ",params2[3])





##########PLOTS###########

x=np.linspace(d[0],d[-1],1000)

plt.figure()
plt.plot(phi,I1,"rx",label="Messwerte des Doppelspaltes")
plt.plot(x,doppel(x,*params2),'g-',label=r'Ausgleichsfunktion')
#plt.xscale('log')
plt.xlabel(r"$phi  \;\mathrm{ / }  \; °$")
plt.ylabel(r"$I \;  \mathrm{ / } \;  \mu A$")
#plt.xticks([-25,-20,-15,-10,-5,0,5,10,15,20,25],[r"$-25$",r"$-20$",r"$-15$",r"$-10$",r"$-5$",r"$0$",r"$5$",r"$10$",r"$15$",r"$20$",r"$25$"])
#plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot2.pdf")

plt.figure()
plt.plot(phi,I2,"rx",label="Messwerte des Einzelspaltes")
plt.plot(x,einzel(x,*params),'g-',label=r'Ausgleichsfunktion')
#plt.xscale('log')
plt.xlabel(r"$phi  \;\mathrm{ / }  \; °$")
plt.ylabel(r"$I \; \mathrm{ / } \;  \mu A$")
#plt.xticks([-25,-20,-15,-10,-5,0,5,10,15,20,25],[r"$-25$",r"$-20$",r"$-15$",r"$-10$",r"$-5$",r"$0$",r"$5$",r"$10$",r"$15$",r"$20$",r"$25$"])
#plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.tight_layout()
plt.legend(loc="best")
plt.savefig("build/plots/plot1.pdf")

plt.figure()
plt.plot(x,1/(params[1]**2*params[0]**2)*einzel(x,*params),'r-',label='Ausgleichsfunktion \ndes Einzelspaltes')
plt.plot(x,1/params2[1]**2*doppel(x,*params2),'g-',label='Ausgleichsfunktion \ndes Doppelspaltes')
#plt.xscale('log')
plt.xlabel(r"$phi  \;\mathrm{ / }  \; °$")
plt.ylabel(r"$\frac{I}{I_{max}}$")
#plt.xticks([-25,-20,-15,-10,-5,0,5,10,15,20,25],[r"$-25$",r"$-20$",r"$-15$",r"$-10$",r"$-5$",r"$0$",r"$5$",r"$10$",r"$15$",r"$20$",r"$25$"])
#plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.tight_layout()
plt.legend(loc="best")
plt.savefig("build/plots/plot3.pdf")