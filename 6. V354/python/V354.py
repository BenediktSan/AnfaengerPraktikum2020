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



###werte einlesen

tamp = np.load('python/variables/tamp.npy')
Uamp = np.load('python/variables/Uamp.npy')

Rap = np.load('python/variables/Rap.npy')

Uu0 = np.load('python/variables/Uu0.npy')
fc = np.load('python/variables/fc.npy')

dt = np.load('python/variables/dt.npy')
fd = np.load('python/variables/fd.npy')

#Bauteildaten

L=ufloat(16.78,0.09) *(10**-3) #in henry
C=ufloat(2.066,0.066) *(10**-9) #in farrad
R1=ufloat(67.2,0.2) #in ohm
R2=ufloat(682,1) #in ohm


###einhüllende erstellen und Reff und Tex

def huell(t,A0,mu):
    return (A0*np.exp(-2*np.pi*mu*t))

Uamppos=np.sqrt(Uamp**2)

params, _1 =curve_fit(huell,tamp,Uamppos,p0=(15,400))
err =np.sqrt(np.diag(_1))
uparams=unp.uarray(params,err)
print(f'\nFit:\nA0= {uparams[0]:.4f}V \nmu={uparams[1]:.5f}1/s\n')

Reff=uparams[1]*4*np.pi*L
Tex=1/(2*np.pi*uparams[1])
print(f'\nReff= {Reff:.4f}ohm \nTex={Tex*10**6:.10f} *10^-6s\nReff-R1={(Reff-R1):.4f} \n')

#aperdiodischer Grenzfall


Raptheo=unp.sqrt((4*L)/(C))
print(f'\nAperiodischer Grenzfall:\nRap= {Rap:}ohm\nRaptheo={(Raptheo):.4f}ohm \nrelative Abweichung: {((Raptheo-Rap)/Rap)*100}%\n')


#Resonanzüberhöhung
R1_=R1+50
w0=unp.sqrt(1/(L*C))
qexp=3.8
qtheo=1/(w0*R1_*C)


breitetheo=R1_/L *10**-3
print(f'\nResonanzüberhöhung\nw0= {w0} 1/s \nqexp={qexp}ohne einheit \nqtheo={(qtheo)}ohne einheit \nrelative Abweichung: {((qtheo-qexp)/qexp)*100}%\n')
print(f'\nbreitetheo={breitetheo} kHz\n')





#plots
plt.figure()
plt.plot(fc,Uu0,"x",label="Messwerte")
plt.xscale('log')
plt.xlabel("f [Hz]")
plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
plt.ylabel("Uc/U [V]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot1.pdf")

#neue größe für lineare darstellung
Unew=np.array([1.44,2.16,2.4,3,3.4,3.72,3.8,3.64,3.12,2.44,1.6,1.24]) 
fnew=np.array([15,20,21,23,24,25,26,27,28.5,30,33,35]) *1000

k=np.linspace(3.8/np.sqrt(2),3.8/np.sqrt(2),25)
x=np.linspace(14,36,25)*1000


h=unp.nominal_values(6.9)*10**3
halb1=np.linspace(26000+h/2,26000+h/2,25)
halb2=np.linspace(26000-h/2,26000-h/2,25)
höhe=np.linspace(1.35,4,25)

plt.figure()
plt.plot(fnew,Unew,"x",label="Messwerte")
plt.plot(x,k,"g--",linewidth=0.6,label=r"$\frac{U_{max}}{\sqrt{2}}$")
plt.plot(halb1,höhe,"g--",linewidth=0.6,label=r"Halbwertsbreite")
plt.plot(halb2,höhe,"g--",linewidth=0.6,label=r"Halbwertsbreite")
plt.xlabel("f [Hz]")
plt.ylabel("Uc/U [V]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot2.pdf")





