import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
import sympy

#Aufgabe1

print('\nAufgabe 1)\n\n\t1.1) Der Mitelwert ist eine Art "Durchschnittswert" von Messwerten.')
print('\t1.2) Die Standardabweichung ist ein Maß für die Abweichung ')
print('\t1.3) ')


#Aufgabe 2

C=100               #willkürlicher wert für die summe

n0=(C/100)+1    #mit c willkürlich und n0=2 willkürlich für einfachere rechnung berechnung von n.
                #=> n zusätzliche rechnungen nötig

n1=(C/9)+1
n2=(C/0.25)+1
print('\nAufgabe 2)\n\n\tVorher beliebige Wahl von von der Summe als C=100, damit man für den Fehler 10 n0 als 2(kleinstmögliches n) setzen kann')
print('\tZusätzliche Durchführungen für Standardabweichung 3:\n\t',n1-n0,'\n\tZusätzliche Durchführungen für Standardabweichung 0.5:\n\t',n2-n0)


#Aufgabe 3

Rin=unc.ufloat(10,1)
Rau=unc.ufloat(15,1)
h=unc.ufloat(20,1)

V=np.pi*(Rau**2-Rin**2)*h

print('\n\n\nAufgabe 3)\n\n\tVergleichswert des Volumen:',V,'\n')

r1, r2, H = sympy.var('r1 r2 H')

err=0.1

f=H* np.pi*((r2**2)-(r1**2))

errf=sympy.sqrt((f.diff(r1)**2*err**2+f.diff(r2)**2*err**2+f.diff(H)**2*err**2))
print(f'\tFunktion: {f}\n\tFehlerfunktion: {errf}\n')
print(f'\tWert der Funtion: {f.evalf(subs={r1:10,r2:15,H:20})}')
print(f'\tFehlerwert: {errf.evalf(subs={r1:10,r2:15,H:20})}\n')





#Aufgabe 4

m=unc.ufloat(5,0.1)*1e-3
v=unc.ufloat(200,10)
t=unc.ufloat(6,0)

s=v*t
Ekin=(v**2)*m*0.5

print('\n\n\nAufgabe 4)\n\n\tVergleichswert der Strecke:',s,'\n\tVergleichswert der Energie:',Ekin,'\n')

Geschw,M = sympy.var('Geschw M')

energ=1/2*M*Geschw**2
strecke=Geschw*6
errGeschw=10
errM=0.1*1e-3
errenerg=sympy.sqrt((energ.diff(Geschw)**2*errGeschw**2+energ.diff(M)**2*errM**2))
errstrecke=sympy.sqrt(strecke.diff(Geschw)**2*errGeschw**2)

print(f'\tFunktion Energie: {energ}\n\tFehlerfunktion Energie: {errenerg}\n')
print(f'\tFunktion Strecke: {strecke}\n\tFehlerfunktion Strecke: {errstrecke}\n')
print(f'\tWert der Energie: {energ.evalf(subs={Geschw:200,M:5*1e-3})}')
print(f'\tFehlerwert Energie: {errenerg.evalf(subs={Geschw:200,M:5*1e-3})}\n')
print(f'\tWert der Strecke: {strecke.evalf(subs={Geschw:200})}')
print(f'\tFehlerwert Strecke: {errstrecke.evalf(subs={Geschw:200})}\n')



x=np.linspace(2,500,10000)
a=np.linspace(3,3,10000)
b=np.linspace(0.5,0.5,10000)


plt.title('Aufgabe 2')
plt.plot(x,np.sqrt(1/(x-1)*C))
plt.plot(x,a,label='3')
plt.plot(x,b,label='0.5')
plt.legend()
plt.show()




