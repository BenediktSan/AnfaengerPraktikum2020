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

##Einlesen der gegeben Daten:

th_bra , n_bra = np.genfromtxt("Daten/Bragg.txt", unpack=True)
th_bro , n_bro = np.genfromtxt("Daten/Brom2.txt", unpack=True)
th_cu  , n_cu  = np.genfromtxt("Daten/Emissionsspektrum2.txt", unpack=True)
th_gal , n_gal = np.genfromtxt("Daten/Gallium2.txt", unpack=True)
th_rub , n_rub = np.genfromtxt("Daten/Rubidium2.txt", unpack=True)
th_str , n_str = np.genfromtxt("Daten/Strontium2.txt", unpack=True)
th_zin , n_zin = np.genfromtxt("Daten/Zink2.txt", unpack=True)
th_zir , n_zir = np.genfromtxt('Daten/Zirkonium2.txt', unpack=True)

##Konstanten definieren 

h = const.h
c = const.c 
e = const.e 
d = 201.4e-12
E_abs = 8980.476
R = 13.6 
b_min = ufloat(20.155, 0.2)
b_max = ufloat(20.57, 0.2)
a_min = ufloat(22.35, 0.2)
a_max = ufloat(22.85, 0.2)

## Funktionen 

def E(th): #In eV
    return h * c / (2 * d * unp.sin(th * np.pi /180 ) * e)


def s(En,Z):
     w = (En)/(R) - (const.alpha**2 * Z**4)/(4)
     print(w)
     return Z - unp.sqrt(w)


def rvsline(Ik, a, b):
    return (Ik - b ) / a




## Bragg Bedingung überprüfen



th_theo = 28 

print("-------Überpüfung der Braggbedingung------")
print("Theoriewert des Glanzwinkels: ",th_theo)
print("Abgemessener Glanzwinkel: " , th_bra[22])
ab_bra =( 1- th_theo/th_bra[22])* 100 
print("Abweichung vom Theoriewert: " , ab_bra)

#print(th_bra[np.where(n_bra == max(n_bra))])
#print(n_bra.index(max(n_bra)))
#print(th_bra[22])
#print(n_bra[22])




####         Kupfer Spektralanalyse

print( "\n -------Spektralanalyse Kupfer------")
print("Berechnung der \"Full Width at Half Maximum\"")

#Seiten der halben Höhe der Peaks
b_l = ufloat(20.14 , 0.15)
b_r = ufloat(20.58 , 0.15)
a_l = ufloat(22.37 , 0.15)
a_r = ufloat(22.87 , 0.15)

print('a_l', a_l)
print('a_r', a_r)
print('b_l', b_l)
print('b_r', b_r)

#FWHM
dE_a = E(a_l) - E(a_r)
print("Delta E_a", E(a_l) - E(a_r) )
dE_b = E(b_l) - E(b_r)
print("Delta E_b", E(b_l) - E(b_r) )

#Peaks
p_a = ufloat(22.5 , 0.2)
p_b = ufloat(20.3 , 0,2)
print("p_a" , p_a)
print("p_b" , p_b)
#print("peak", th_cu[145])

E_max_a = E(p_a)
print("E,max alpha" , E_max_a)
E_max_b = E(p_b)
print("E,max beta"  , E_max_b)

#Auflösung
A_a = E_max_a / dE_a
A_b = E_max_b / dE_b
print("Auflösung Peak alpha: " , A_a)
print("Auflösung Peak beta: " , A_b)


#k_a = ufloat()

cu_min = 145
cu_max_b = 1533



## Absorptionskoeffizient

print('Absorptionskoeffizienten')
s1 = 29 - unp.sqrt(E_abs/R)
print("s1: " , s1)
s2 = 29 - 2* unp.sqrt((E_abs - E(p_a))/R)
print("s2: " , s2)
s3 = 29 - 3* unp.sqrt((E_abs - E(p_b))/R)
print("s3: " , s3)

#####                   restlichen Metalle 


####          Zink
#
#
#n_zinmax = np.amax(n_zin)
#n_zinmin = np.amin(n_zin)
#I_zin = n_zinmin + (n_zinmax - n_zinmin)/2
#
#print('Zink', 'min', n_zinmin, 'max', n_zinmax)
#print('I_zink', I_zin)
#
#
#x_zin = np.array([th_zin[6],th_zin[7]])
#y_zin = np.array([n_zin[6], n_zin[7]])
#
#
#params = np.polyfit( x_zin, y_zin, deg =1, cov = False)
#
#a_zin = params[0]
#b_zin = params[1]
#print('a_zin', a_zin)
#print('b_zin', b_zin)
#
#tzin = ufloat(rvsline(I_zin, a_zin, b_zin), 0.05)   
#Ezin = E(tzin)
#Sigma_zin = s(Ezin,30)
#
#print('t_zin', tzin)
#print('E_zin', E(tzin))
#print('Sigma_zink', Sigma_zin)
#print('dif', 1 - 3.56/Sigma_zin.n)
#
#zinplot = np.linspace(th_zin[6], th_zin[7], 1000)













###         lets try the Schleife

theo =      [ 3.56      ,      1.63       ,  3.84     ,   3.95    ,  3.99         ,   4.39    ]
Z =         [ 30        ,      31         ,  35       ,   37      , 38            ,  40       ]
step =      [  [6,7]    ,     [3,4]       ,  [3,5]    , [5,6]     , [5,6]         ,   [4,5]   ]
th =        [  th_zin   ,    th_gal       ,  th_bro   ,th_rub     ,th_str         ,th_zir     ]
n  =        [ n_zin     ,      n_gal      ,  n_bro    ,n_rub      ,n_str          ,n_zir      ]     
nam =       ["Zink"     ,      "Gallium"  ,"Bromium"  ,"Rubidium" ,"Strontium"    ,"Zirkonium"]



for name, th, n , step , Z , theo in zip(nam, th , n , step , Z ,  theo):

    print("-------Auswertung von " + name + " --------")

    n_min = np.min(n)
    n_max = np.max(n)

    I = n_min + ( n_max - n_min)/2
    print("Minimum n von " + name +":", n_min , "Maximum n von " + name +":", n_max)
    print("I_"+name +" :" , I)

    x = np.array( [th[step[0]] , th[step[1]]])
    y = np.array( [n[step[0]]  ,  n[step[1]]])
    plot = np.linspace(th[step[0]] , th[step[1]] , 100)

    params = np.polyfit( x , y , deg = 1 , cov = False )

    a = params[0]
    b = params[1]

    print("a_" + name + " :" , a  , "  b_"  + name + " :" , b )

    t = ufloat(rvsline(I , a , b ), 0.05)
    En = E(t)
    sig = s( En , Z)

    print("t_" + name + " :" , t , "  E_" + name + " :" , En )
    print("Sigma_" + name + " :" , sig , "  diff_" + name + " :" , 1 - theo/sig.n)

    plt.figure()
    plt.scatter(th[np.argmin(n)], [n_min], s=40, marker='x', color='blue', label=r'$I_{min}$')
    plt.scatter(th[np.argmax(n)], [n_max], s=40, marker='x', color='green', label=r'$I_{max}$')
    plt.scatter([t.n], [I], s=40, marker='x', color='red', label=r'$I_{K}$')
    plt.plot(plot, a * plot + b, '-b', label='Verbindungsgerade')
    plt.plot(th, n, 'k.', label='Messwerte '+ name)
    plt.xlabel(r'$ \theta \quad  [deg]$')
    plt.ylabel(r'$ N \quad  [I/s]$')
    plt.legend()
    plt.tight_layout()
    plt.savefig('build/plots/' + name + '.pdf')


sigma = np.array([3.613, 3.67, 3.87, 4.07, 4.11, 4.30 ])
Ord = np.array([30, 31, 35, 37, 38, 40]) 
E_k = np.array([9616, 10326, 13450, 15090, 16000, 17800])

Ek_plot = np.sqrt(E_k)
xplot = np.linspace(90, 140, 1000)

params , ma = np.polyfit(Ek_plot ,Ord, deg =1, cov = True)
errors = np.sqrt(np.diag(ma))
a_ryd = ufloat(params[0], errors[0])
c_ryd = ufloat(params[1], errors[1])
print('1/sqrt(Rh)', a_ryd)
print('c', c_ryd)
Ryd = 1/a_ryd**2
print('R', Ryd)
print('dif', 1 - 13.6/Ryd.n)


####                 Plotting 

plt.figure()
plt.plot(Ek_plot, Ord, 'k.', label='Errechnete Punkte')
plt.plot(xplot, a_ryd.n * xplot + c_ryd.n, 'r-', label='Ausgleichsgerade')
plt.ylabel(r'$Z$')
plt.xlabel(r'$ Einheiten$')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/plots/rydberg.pdf')

### Bragg Bedingung


plt.figure()
plt.plot( th_bra , n_bra , "." , label=" Messdaten Bragg Bedingung")
plt.scatter( th_bra[22] , n_bra[22], s=30 ,  marker='o', color="red" , label="Maximun")
plt.legend()
plt.savefig("build/plots/Bragg.pdf")


### Emissionsspektrum Kupfer

plt.figure()
plt.scatter([11.1], [420.0], s=35, marker='o', color='red')
plt.plot(th_cu, n_cu, "." , label="Messwerte Kupfer")
plt.hlines(y= 799.5, xmin= b_min.n, xmax= b_max.n ,linewidth=1, color='b', label=r'FWHM für $K_{\beta}$')
plt.hlines(y= 2525, xmin=a_min.n, xmax=a_max.n ,linewidth=1, color='g', label=r'FWHM für $K_{\alpha}$')
plt.vlines(x= b_min.n, ymin= 0, ymax= 799.5 ,linewidth=1, color='b')
plt.vlines(x= b_max.n, ymin= 0, ymax= 799.5 ,linewidth=1, color='b')
plt.vlines(x= a_min.n , ymin= 0, ymax= 2525 ,linewidth=1, color='g')
plt.vlines(x= a_max.n , ymin= 0, ymax= 2525 ,linewidth=1, color='g')
#plt.xlabel(r'$ \alpha_{\text{GM}} \quad \mathbin{/} \si{\degree}$')
#plt.ylabel(r'$ N \quad \mathbin{/} \si{Imp\per\second}$')
plt.annotate(r'Bremsberg', 
            xy = (11.1, 420.0), xycoords='data', xytext=(-10, 20),
            textcoords='offset points', fontsize=12, 
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
plt.scatter([20.3], [1599.0], s=20, marker='o', color='red')
plt.annotate(r'$K_{\beta}$',
            xy = (20.3, 1599.0), xycoords='data', xytext=(-50, -25),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
plt.scatter([22.5], [5050.0], s=20, marker='o', color='red')
plt.annotate(r'$K_{\alpha}$',
            xy = (22.5, 5050.0), xycoords='data', xytext=(+10, -2),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
plt.legend()
plt.savefig("build/plots/Kupfer.pdf")





#plt.figure()
#plt.scatter(th_zin[np.argmin(n_zin)], [n_zinmin], s=40, marker='x', color='blue', label=r'$I_{min}$')
#plt.scatter(th_zin[np.argmax(n_zin)], [n_zinmax], s=40, marker='x', color='green', label=r'$I_{max}$')
#plt.scatter([tzin.n], [I_zin], s=40, marker='x', color='red', label=r'$I_{K}$')
#plt.plot(zinplot, a_zin * zinplot + b_zin, '-b', label='Verbindungsgerade')
#plt.plot(th_zin, n_zin, 'k.', label='Messwerte')
#plt.xlabel(r'$ \theta \quad  [deg]$')
#plt.ylabel(r'$ N \quad  [I/s]$')
#plt.legend()
#plt.tight_layout()
#plt.savefig('build//plots/zink.pdf')