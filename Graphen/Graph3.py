import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat

d=np.array([0.1,0.2,.3,.4,.5,1,1.2,1.5,2,3,4,5])
#d*=1e-2

N=np.array([7565,6907,6214,5531,4942,2652,2116,1466,970,333,127,48])
#N*=N/60


#datei = open('text3.txt','w')
#datei.write(f'')
#print(f'')
def exp(x,m):
    return 7565*np.exp(- x * m)
params, covariance_matrix = curve_fit(exp,d,N)

uncertainties = np.sqrt(np.diag(covariance_matrix))

m=ufloat(params,uncertainties)
print(m)

fig, (ax1,ax2)=plt.subplots(2,1)

ax1.set_title(r"Nicht Logarithmisch")
#ax1.plot(d,N,'.',label=r'Messwerte')
#ax1.plot(d,N+np.sqrt(N),'.',label=r'Messwerteplus')
ax1.plot(d,np.sqrt(N),'.',label=r'Messunsicherheit')
ax1.plot(d,exp(d,0.94),label=r'Fit')
ax1.errorbar(d, N, yerr=np.sqrt(N)*5 , fmt='.' ,label=r'Messwerte')
ax1.legend()
ax1.legend(loc='best')
ax1.set_xlabel('$d/cm$')
ax1.set_ylabel('$N/60s^-1$')


ax2.set_title(r"$Logarithmisch$")
#ax2.plot(d,N,'.',label=r'Messwerte')
#ax2.plot(d,N+np.sqrt(N),'.',label=r'Messwerteplus')
#ax2.plot(d,N-np.sqrt(N),'.',label=r'Messwerteminus')
ax2.errorbar(d, N, yerr=np.sqrt(N)*5, fmt='.',label=r'Messwerte')
ax2.plot(d,np.sqrt(N),'.',label=r'Messunsicherheit')
ax2.plot(d,exp(d,0.94),label=r'Fit')
ax2.set_yscale('log')
ax2.legend()
ax2.legend(loc='best')
ax2.set_xlabel('$d/cm$')
ax2.set_ylabel('$N/60s^-1$')



fig.tight_layout()
plt.savefig('build/Graph3.pdf')

plt.show()
