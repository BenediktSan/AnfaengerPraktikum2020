import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy

#       a)
#elektrischer Widerstand R:
#R =

#Spannungsabfall U_a:
#U_a=

#geometrische Groeßen:


#       b)
#Hall-Effekt
#Messungen U-+:
#Up=
#Um=

#Hall Spannung
#U_h=


#       c)
# Elementarladung e0:
e0=1.602e-19
# Elektronenmasse m0:
m0=9.109e-31 
#pi:
pi=np.pi
#Planksches Wirkungsquantum h:
h=6.626e-34
#Boltzmannsche Konstante k:
k=1.3806e-23


# zu berechnen:
# Ladungsträger pro Volumen n
def number(U_H,B,I,d):
    return (-1/(U_H*e0)) * (B*I)/d

# Zahl der Ladungsträger pro Atom z
#z= 
#no clue


# mittlere Flugzeit tau:
def Fermi(U_H,B,I,d):
    return h**2/2*m0 * np.cbrt((3*number(U_H,B,I,d))/8*pi)**(2))

def tau(U_H,B,I,d,b):
    return -2*m0*b/(e0*U_H) * np.sqrt((2*Fermi(number(U_H,B,I,d)))/m0)

# mittlere Driftgeschwindigkeit vd
j=1
def mitDrift(U_H,B,I,d):
    return -j/(e0*number(U_H,B,I,d))

#Beweglichkeit mue:
def Beweg(U_H,B,I,d,b):
    return -e0*tau(U_H,B,I,d,b)/(2*m0)

#Totalgeschwindigkeit v:
def vTot(T):
    return np.sqrt(3*k*T/m0)

#mittlere freie Weglänge l:
def mWeg(U_H,B,I,d,b):
    return tau(U_H,B,I,d,b)*np.sqrt(2*number(U_H,B,I,b)/m0)
