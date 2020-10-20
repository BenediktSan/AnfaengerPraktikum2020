import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp


g=np.array([60,80,100,110,120,125])
#g*=1e-3

b=np.array([285,142,117,85,86,82])
#b*=1e-4
B=1/b
G=1/g
f=1/(B+G)
n=6

def mittelf(f,n):
    return np.sum(f)/n
def stabwf(f,n):
    return np.sqrt(1/((n-1))*np.sum((mittelf(f,n)-(f))**2))
def fehlermittel(f,n):
    return np.sqrt(1/(n*(n-1))*np.sum((mittelf(f,n)-f)**2))

print(f'\nMittelwert:{mittelf(f,n)}\nStandardabweichung:{stabwf(f,n)}\nFehler des Mittelwerts:{fehlermittel(f,n)}\n')

#Regressionsgerade

m=(mittelf(G*B,n)-(mittelf(G,n)*mittelf(B,n)))/(mittelf(B**2,n)-mittelf(B,n)**2)
a=mittelf(G,n)-m*mittelf(B,n)
abwm=stabwf(f,n)/(n*((mittelf(B**2,n)-mittelf(B,n)**2)))
abwa=(stabwf(f,n)*mittelf(B,n))/(n*((mittelf(B**2,n)-mittelf(B,n)**2)))

print(f'\nm:{m}\na:{a}\nabwm^2:{abwm}\nabwm:{np.sqrt(abwm)}\nabwa^2:{abwa}\nabwa:{np.sqrt(abwa)}\n')


#datei = open('text2.txt','w')
#datei.write(f'')
#print(f'')


plt.plot(B,1/f,'.',label=r'f')
#plt.plot(B,f,'.',label=r'f')
#plt.plot(B,f,'.',label=r'f')

plt.plot(B,G,'.',label=r'Messwerte')
plt.plot(B,(m*B+a),label=r'lineare Regression')
plt.legend()
plt.legend(loc='best')

with plt.xkcd():
   plt.xlabel('$B/mm^-1$')
   plt.ylabel('$G/mm^-1$')

#plt.savefig('Graph2.pdf')
plt.show()
