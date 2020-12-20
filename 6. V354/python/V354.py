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
#print(f'\nFit:\nA0= {uparams[0]:.4f}V \nmu={uparams[1]:.5f}1/s\n')

Reff=uparams[1]*4*np.pi*L
Tex=1/(2*np.pi*uparams[1])
#print(f'\nReff= {Reff:.4f}ohm \nTex={Tex*10**6:.10f} *10^-6s\nReff-R1={(Reff-R1):.4f} \n')

###aperdiodischer Grenzfall


Raptheo=unp.sqrt((4*L)/(C))
#print(f'\nAperiodischer Grenzfall:\nRap= {Rap:}ohm\nRaptheo={(Raptheo):.4f}ohm \nrelative Abweichung: {((Raptheo-Rap)/Raptheo)*100}%\n')


###Resonanzüberhöhung
R1new=R1+50
w0=(1/(L*C))**(1/2)
qexp=3.8
qtheo=unp.sqrt((L)/(R1new**2*C))



#print(f'\nResonanzüberhöhung\nw0= {w0} 1/s \nqexp={qexp} ohne einheit \nqtheo={(qtheo)} ohne einheit \nrelative Abweichung: {((qtheo-qexp)/qtheo)*100}%\n')





#plotparameter
k=np.linspace(3.8/np.sqrt(2),3.8/np.sqrt(2),25)
x=np.linspace(14,36,25)*1000
xplot2=np.linspace(20,32,50)*1000

#neue größen für lineare darstellung
Unew=np.array([1.44,2.16,2.4,3,3.4,3.72,3.8,3.64,3.12,2.44,1.6,1.24]) 
fnew=np.array([15,20,21,23,24,25,26,27,28.5,30,33,35]) *1000


#fit für schnittpunkt mit halbwertsbreite
Unew2=np.array([3,3.4,3.72,3.8,3.64,3.12,2.44]) 
fnew2=np.array([23,24,25,26,27,28.5,30]) *1000

def square(f,A,B,C):
    return (A*(f**2)+B*f+C)

params2, _2= curve_fit(square,fnew2,Unew2,p0=(25000,1,4))
err2 = np.sqrt(np.diag(_2))
uparams2=unp.uarray(params2,err2)
#print(f'\nFit2:\nFunktionswerte= {uparams2[0]} & {uparams2[1]} & {uparams2[2]}\n')




##Abweichung für Breite errechnen

#weinen und wolfram alpha wert nehmen
wolf1=np.linspace(22395.6,22395.6,25)
wolf2=np.linspace(29532,29532,25)


breitetheo=R1new/L *10**-3
#print("\nwolf1: ",wolf1[0],"\nwolf2: ",wolf2[1])
#print(f'\nbreitetheo={breitetheo} kHz\nbreiteexp={((wolf2[1]-wolf1[1])/1000)} kHz\nAbweichung={(-breitetheo+((wolf2[1]-wolf1[1])/1000))/(breitetheo)}\n')



###Phasenverschiebung

fdnew=np.array([20,25,30,35,35.75,36.25,36.75,37.5,38,38.25,38.75,40,42.5,45]) *1000
dtnew=np.array([0,0.5,1,1.5,3,4,6,8,10,11,11,11,11.5,11]) *(10**-6)




phi1=dt*fd*2*np.pi
phi2=dtnew*fdnew*2*np.pi

#fit auf phi2
def sigmoid(x, a, b,c,d):
    return (a / (1 + np.exp(-(x - b)/d)) + c)


params3, _3= curve_fit(sigmoid,fdnew,phi2,p0=(2,38000,1,200) )
err3 = np.sqrt(np.diag(_3))
uparams3=unp.uarray(params3,err3)
plot1=np.linspace(20,45,50)*1000
#print(f'Fit 3:\n{uparams3}')


def schnittsig(a,b,c,d,s):
    return (-d*np.log(a/(s-c)-1)+b)

w1exp=schnittsig(*params3,np.pi/4)
w2exp=schnittsig(*params3,3*np.pi/4)
wresexp=schnittsig(*params3,np.pi/2)


w1theo=(R1new/(2*L))+unp.sqrt((R1new**2/(4*L**2))+(1/(L*C)))
w2theo=-1*(R1new/(2*L))+unp.sqrt((R1new/(2*L))**2+(1/(L*C)))
wrestheo=unp.sqrt((1/(L*C))-(R1new**2/(2*L**2)))

#print(f'\nPhasenverschiebung:\nwrestheo= {wrestheo} 1/s \twresexp= {wresexp} 1/s \trelative Abweichung: {((wrestheo-wresexp)/wrestheo)*100}%')
#print(f'w1theo= {w1theo} 1/s \tw1exp= {w1exp} \trelative Abweichung: {((w1theo-w1exp)/w1theo)*100}%')
#print(f'w2theo= {w2theo} 1/s \tw2exp= {w2exp} 1/s\trelative Abweichung: {((w2theo-w2exp)/w2theo)*100}%')

#plotparameter hierfür

höhe2=np.linspace(0,3,25)
w1=np.linspace(unp.nominal_values(w1exp),unp.nominal_values(w1exp),25)
w2=np.linspace(unp.nominal_values(w2exp),unp.nominal_values(w2exp),25)
wres=np.linspace(unp.nominal_values(wresexp),unp.nominal_values(wresexp),25)












#halbwertsbreite plotparameter

höhe=np.linspace(1.35,4,25)
plot0=np.linspace(tamp[0],tamp[-1])


#plots
plt.figure()
plt.plot(tamp,Uamp,"x",label="Messwerte")
plt.plot(plot0,huell(plot0,*params),"g",label="Einhüllende Funktion")
plt.plot(plot0,-huell(plot0,*params),"g")
plt.xlabel("t [s]")
plt.ylabel("U [V]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot0.pdf")


plt.figure()
plt.plot(fc,Uu0,"x",label="Messwerte")
plt.xscale('log')
plt.xlabel("f [Hz]")
plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
plt.ylabel("Uc/U [V]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot1.pdf")



plt.figure()
plt.plot(fnew,Unew,"x",label="Messwerte")
plt.plot(x,k,"b--",linewidth=0.6,label=r"$\frac{{\frac{U}{U_0}}_{max}}{\sqrt{2}}$")
#plt.plot(halb1,höhe,"g--",linewidth=0.6,label=r"Halbwertsbreite")
#plt.plot(halb2,höhe,"g--",linewidth=0.6,label=r"Halbwertsbreite")
plt.plot(wolf1,höhe,"g--",linewidth=0.6,label=r"Halbwertsbreite")
plt.plot(wolf2,höhe,"g--",linewidth=0.6,)
plt.plot(xplot2,square(xplot2,*params2))
plt.xlabel("f [Hz]")
plt.ylabel("Uc/U [V]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot2.pdf")



plt.figure()
plt.plot(fd,phi1,"x",label="Messwerte")
#plt.plot(plot1,sigmoid(plot1,*params3))
plt.xscale('log')
plt.xlabel("f [Hz]")
plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
plt.yticks([0,np.pi/4,np.pi/2,(3*np.pi)/4,np.pi],[r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",r"$\pi$"])
plt.ylabel(r"$\phi$ [rad]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot3.pdf")


plt.figure()
plt.plot(fdnew,phi2,"x",label="Messwerte")
plt.plot(plot1,sigmoid(plot1,*params3),label="Fit-Funktion")
plt.plot(w1,höhe2,"g--",linewidth=0.6,label=r"$w_1$")
plt.plot(w2,höhe2,"g--",linewidth=0.6,label=r"$w_2$")
plt.plot(wres,höhe2,"r--",linewidth=0.6,label=r"$w_{res}$")
plt.yticks([0,np.pi/4,np.pi/2,(3*np.pi)/4,np.pi],[r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",r"$\pi$"])
plt.xlabel("f [Hz]")
plt.ylabel(r"$\phi$ [rad]")
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot4.pdf")

