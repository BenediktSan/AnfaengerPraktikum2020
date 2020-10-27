import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit

m=np.array([2.,3.,4.,5.,6.])
#m*=1e-3

x=np.array([1.6,2.7,3.2,3.5,4.])
#x*=1e-3


def func(m,a,b):
    return a*m+b

plt.plot(x,m,'.',label=r'Messwerte')

fitted ,a= curve_fit(func, x, m)

datei = open('build/text1.txt','w')
datei.write(f'Die Kurve ist {fitted[0]:.4f}*m+({fitted[1]:.4f}). Damit ist k={9.81/fitted[0]:.4f}')
#print(f'Die Kurve ist {fitted[0]:.4f}*m+({fitted[1]:.4f}). Damit ist k={9.81/fitted[0]:.4f}')
x_new=np.linspace(1,5,50)
fitted_curve = func(x_new, fitted[0], fitted[1])


plt.plot(x_new,fitted_curve,label=r'Ausgleichsgerade')
plt.legend(loc='best')
plt.xlim(1.4,4.6)

with plt.xkcd():
   plt.xlabel('x/cm')
   plt.ylabel('m/g')

plt.savefig('build/Graph1.pdf')

#ax2.plot(x,y,'g.')
#ax2.set_yscale('log')
#ax2.set_xlabel('$x$')
#ax2.set_ylabel('$y$')
#plt.savefig('.pdf')
#plt.tight_layout()

#plt.show()
