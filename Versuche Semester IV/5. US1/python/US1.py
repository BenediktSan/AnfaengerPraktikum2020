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

if os.path.exists("python/tabellen") == False:
    os.mkdir("python/tabellen")

# Bestimmung der Schallgeschwindigkeit

N, s, t, V = np.genfromtxt("python/data.txt", unpack = True)


def selection_sort(x, y , z):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
        (y[i], y[swap]) = (y[swap], y[i])
        (z[i], z[swap]) = (z[swap], z[i])
    return x

selection_sort(s,t,V)

s*=1e-3
t*=1e-6

params, covariance_matrix = np.polyfit(t, s, deg =1 , cov = True)
errors = np.sqrt(np.diag(covariance_matrix))

print(params)
print(errors)

c =2 * ufloat(params[0] , errors[0])

print(c)

x = np.linspace( 0 , 6.5e-5 , 200 )


plt.figure()
plt.plot( t , s , "k." , label="Messdaten" ) 
plt.plot(x, params[0] * x + params[1] , "r" , label="Ausgleichsgerade")
plt.xlabel( r'$t \quad / \quad s$')
plt.ylabel( r'$s \quad / \quad m$'   )
plt.legend()
plt.tight_layout()
plt.savefig("build/plots/Schallgeschwindigkeit.pdf")


#Bestimmung des Absorptionskoeffizient

s2 = c * t

#print(s2)

def I(x, A , B):
    return A * np.exp(B * x)


parameter , _1 = curve_fit(I , unp.nominal_values(s2) , V )



uncertainties = np.sqrt(np.diag(_1))


for names ,value, unsicherheit in zip("AB", parameter,uncertainties):
    print(f"{names}={value:.8f} +- {unsicherheit:.8f}")

plt.figure()
plt.plot(unp.nominal_values(s2) ,V , ".", label="Messdaten")
plt.plot(unp.nominal_values(s2), I(unp.nominal_values(s2), *parameter), label="Exponential-Fit")
plt.xlabel( r'$s \quad / \quad m $')
plt.ylabel( r'$U \quad / \quad V $' )
plt.legend()
plt.savefig("build/plots/Daempfung.pdf")

# Bestimmung der Abstände im Auge

C_L = 2500
C_GK = 1410

t1 = 17.4e-6
t2 = 18.2e-6
t3 = 31.1e-6

S_I = t1 * C_GK * 0.5
print(S_I*1e3)

S_L = S_I + (t2-t1)* C_L *0.5
print(S_L*1e3)

S_R = S_L + (t3-t2)* C_GK *0.5

print(S_R *1e3)



print(1 - 2730/c)