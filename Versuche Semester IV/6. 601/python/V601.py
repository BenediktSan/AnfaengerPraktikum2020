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

#####MEsSWERTE#########


U1=np.linspace(1,22,22)
U1[-4]=U1[-5]+0.5
U1[-3]=U1[-4]+0.5
U1[-2]=U1[-1]+1
U1[-1]=U1[-2]+1




del1=np.array([0.2,0.15,0.20,0.25,0.2,0.2,0.30,0.3,0.4,0.4,0.65,0.7,0.65,0.85,1.1,1.5,1.8,2.7,1.6,0.7,0.5,0.05])


#del2=1/np.array([0.6,1.45,1.35,1.35,1.3,1.15,1.05,0.75,0.25,0.2,0.2])

U2=np.linspace(0.5,21.5,22)-1
U2[0]=0
U2[-4]=U2[-4]+0.5
U2[-3]=U2[-3]+0.5
U2[-2]=U2[-2]+1



del2=np.array([1.2,1.45,1.35,1.35,1.3,1.15,1.05,0.75,0.25,0.2,0.20,0,0,0,0,0.05,0.05,0,0,0,0.05,0.05])





####mittlere freie weglänge#####

T=np.array([20.5,148,182]) +273.15
p=(5.5*10**7*np.exp(-6876/T)) #in bra
omega=(0.0029/p) #in meter
a=1           #in meter

print("\n\n######Mittlere freie Weglänge#####\n")
table1 ={ 'T':T, 'omeag':omega,'verhältnis':a/omega }
print("\n ",tabulate (table1, tablefmt="latex"))


#####differentiele Energieverteilung######
print("\n\n######Differentielle Energieverteilung#####\n")

l1=1/np.array([2.8,2.75,2.4,2.2,2.6,2.4,2.4,2.2,2.7,2.75])
print("Messung 1:")
print(f'Spannung  {np.mean(l1):.2f} \pm {np.std(l1):.2f}')
print("Kontaktpotential: ",11-6.6 )

U1=U2*np.mean(l1)
U2=U2*np.mean(l1)


table1 ={ 'T':U1, 'omeag':del1,'U2':U2, 'del2':del2 }
print("\n ",tabulate (table1, tablefmt="latex"))


#####FRanck_hErtzs######

l2=1/(np.array([5,4.6,4.6,4.9])/10)


print("\n\n######Franck hertzs#####\n")
print(f'Spannung {np.mean(l2):.2f} \pm {np.std(l2):.2f}')


d=np.array([2.4,2.4,2.6,2.5,2.7,2.6,3])
d_=d*np.mean(l2)

print(f'mean distance {np.mean(d_):.2f} \pm {np.std(d_):.2f}')
mean_=ufloat(np.mean(d_),np.std(d_))
print(mean_)
print(f' lamda: {(const.c/((mean_*const.elementary_charge)/const.h))*10**9} nm')
lam=(const.c/((mean_*const.elementary_charge)/const.h))
e=mean_*const.elementary_charge

theo=(const.c/(4.9*const.elementary_charge/const.h))
print("lambda theo: ", theo*10**9)
print(f'relabw Energy: {(4.9-mean_)/4.9}percent \n relabw lamda: {((theo-lam)/theo)}percent')

x=np.linspace(1,7,7)
table1 ={ 'T':x, 'omeag':d,'del2':d_ }
print("\n ",tabulate (table1, tablefmt="latex"))



















#########PLOTS#########
a=6.6
x=np.linspace(a,a,100)
y=np.linspace(0,2.7,100)

#plt.figure()
#plt.plot(t,np.log(U_),"x",label="Messwerte")
#plt.plot(x1,huell(x1,*params1),"g",label="Fit-Funktion")
##plt.plot(plot0,-huell(plot0,*params),"g")
#plt.xlabel("t [s]")
#plt.ylabel(r'$\ln\left({\frac{U}{U_0}}\right)$')
#plt.tight_layout()
#plt.legend()
#plt.savefig("build/plots/plot0.pdf")

plt.figure()
plt.plot(U1,del1, 'rx', label='Messdaten')
plt.plot(x,y,"g--",linewidth=0.6)
plt.ylabel(r'$\frac{\Delta y}{\Delta x} $')
plt.xlabel(r'$U_A$ [V]')
#plt.yscale('log')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plots/plot1.pdf')

plt.figure()
plt.plot(U2,del2,  'rx', label='Messdaten')
plt.ylabel(r'$\frac{\Delta y}{\Delta x} $')
plt.xlabel(r'$U_A$ [V]')
##plt.yscale('log')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plots/plot2.pdf')



#######TABELLEN########


#np.savetxt(
#    'build/f.txt',
#    np.column_stack([U2,U2/U2[0], f1]),
#    fmt=['%.3f', '%.3f', '%.3f'],       
#    delimiter=' & ',
#    header='U2,U/U0,f',
#)