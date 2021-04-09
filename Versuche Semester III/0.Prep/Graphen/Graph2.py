import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
matplotlib.rcParams['text.usetex'] = True
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from matplotlib import rc


g=np.array([60,80,100,110,120,125])
#g*=1e-3

b=np.array([285,142,117,85,86,82])
#b*=1e-4

# a)
G=1/g
B=1/b

f=1/(B+G)
n=6


for i in range(0,6):
    print(f"Brennwerte für Messpaar {i+1} ={f[i]:.3f}")


def mittelf(f,n):
    return np.sum(f)/n
def stabwf(f,n):
    return np.sqrt(1/((n-1))*np.sum((mittelf(f,n)-(f))**2))
def fehlermittel(f,n):
    return np.sqrt(1/(n*(n-1))*np.sum((mittelf(f,n)-f)**2))

print(f'\nMittelwert:{mittelf(f,n):.4f}\nStandardabweichung:{stabwf(f,n):.4f}\nFehler des Mittelwerts:{fehlermittel(f,n):.4f}\n')



#b)

#Regressionsgerade

#manuell

#m=(mittelf(G*B,n)-(mittelf(G,n)*mittelf(B,n)))/(mittelf(B**2,n)-mittelf(B,n)**2)
#a=mittelf(G,n)-m*mittelf(B,n)
#abwm=stabwf(f,n)/(n*((mittelf(B**2,n)-mittelf(B,n)**2)))
#abwa=(stabwf(f,n)*mittelf(B,n))/(n*((mittelf(B**2,n)-mittelf(B,n)**2)))

#numpy

params , _ = np.polyfit(B,G, deg=1, cov=True)
err = np.sqrt( np.diag( _ ) )

m=ufloat(params[0],err[0])
a=ufloat(params[1],err[1])

print(m,a)
print(1/a)
#print(f'\nm:{m}\na:{a}\nabwm^2:{abwm}\nabwm:{np.sqrt(abwm)}\nabwa^2:{abwa}\nabwa:{np.sqrt(abwa)}\n')
#print(f" m={params[0]:.4f},\n a={params[1]:.4f},\n err_m={err[0]:.4f},\n err_a={err[1]:.4f}")

#datei = open('text2.txt','w')
#datei.write(f'')
#print(f'')

#plt.plot(B,1/f,'.',label=r'f')
#plt.plot(B,f,'.',label=r'f')
#plt.plot(B,f,'.',label=r'f')

plt.plot(B,G,'.',label=r'Messwerte')
plt.plot(B,(m.n*B+a.n),label=r'lineare Regression')
plt.legend()
plt.legend(loc='best')
plt.xlabel(r'$\frac{1}{b}$ / $\frac{1}{mm}$' )
plt.ylabel(r'$\frac{1}{g}$ / $\frac{1}{mm}$' )
#plt.show()

plt.savefig('build/Graph2.pdf')

