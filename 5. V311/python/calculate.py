import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
##      Einlesen der Daten:
#Hallsonde:
I_aufsteigend=np.load('python/variables/I_aufsteigend.npy')
I_abfallend=np.load('python/variables/I_abfallend.npy' )
B_aufsteigend=np.load('python/variables/B_aufsteigend.npy')
B_abfallend=np.load('python/variables/B_abfallend.npy' )
#Abmessung der Proben:
Zink=np.load('python/variables/Zink.npy')
Kupfer=np.load('python/variables/Kupfer.npy')
Zink_Breite=Zink[1]
Zink_Dicke=Zink[2]
Kupfer_Breite=Kupfer[1]
Kupfer_Dicke=Kupfer[2]
# Widerstandsbestimmung:
I_Widerstand=np.load('python/variables/I.npy')
U_Widerstand_Zink=np.load('python/variables/U_Zink.npy')
U_Widerstand_Kupfer=np.load('python/variables/U_Kupfer.npy')
# Messung der Hall-Spannung bei konstantem Probenstrom U_H in mV
Ik_Platte_Zink=8
Ik_Platte_Kupfer=10
I_s_Zink=np.load('python/variables/I_s_Zink.npy')
I_s_Kupfer=np.load('python/variables/I_s_Kupfer.npy')
Zink_Is_U_H_1=np.load('python/variables/Zink_Is_U_H_1.npy')
Kupfer_Is_U_H_1=np.load('python/variables/Kupfer_Is_U_H_1.npy')
# nach Umpolung:
Zink_Is_U_H_2=np.load('python/variables/Zink_Is_U_H_1.npy')
Kupfer_Is_U_H_2=np.load('python/variables/Kupfer_Is_U_H_1.npy')
# Messung der Hall-Spannung bei konstantem Spulenstrom U_H in mV 
Ik_Spule_Zink=5
Ik_Spule_Kupfer=3
I_p_Zink=np.load('python/variables/I_p_Zink.npy')
I_p_Kupfer=np.load('python/variables/I_p_Kupfer.npy')
Zink_Ip_U_H_1=np.load('python/variables/Zink_Ip_U_H_1.npy')
Kupfer_Ip_U_H_1=np.load('python/variables/Kupfer_Ip_U_H_1.npy')
# nach Umpolung:
Zink_Ip_U_H_2=np.load('python/variables/Zink_Ip_U_H_2.npy')
Kupfer_Ip_U_H_2=np.load('python/variables/Kupfer_Ip_U_H_2.npy')

#       a)
#elektrischer Widerstand R:
R_Zink_array = U_Widerstand_Zink[1:10] / I_Widerstand[1:10] 
R_Kupfer_array = U_Widerstand_Kupfer[1:10]  / I_Widerstand[1:10] 
R_Zink=ufloat(np.mean(R_Zink_array),np.std(R_Zink_array))
R_Kupfer=ufloat(np.mean(R_Kupfer_array),np.std(R_Kupfer_array))
#       b)
#Hall-Effekt
U_H_Zink_I_Sv =   0.5*( Zink_Is_U_H_1 +   Zink_Is_U_H_2   )
U_H_Kupfer_I_Sv = 0.5*( Kupfer_Is_U_H_1 + Kupfer_Is_U_H_2 )
U_H_Zink_I_Pv =   0.5*( Zink_Ip_U_H_1 +   Zink_Ip_U_H_2   )
U_H_Kupfer_I_Pv = 0.5*( Kupfer_Ip_U_H_1 + Kupfer_Ip_U_H_2 )
print(U_H_Zink_I_Sv)
print(U_H_Kupfer_I_Sv)
print(U_H_Zink_I_Pv)
print(U_H_Kupfer_I_Pv)
#       c)
##      Naturkonstanten:
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
    return (h**2/2*m0) * np.cbrt((3*number(U_H,B,I,d))/8*pi)**(2)

def tau(U_H,B,I,d,b):
    return (-2*m0*b/(e0*U_H)) * np.sqrt((2*Fermi(U_H,B,I,d))/m0)

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
    return tau(U_H,B,I,d,b)*np.sqrt(2*Fermi(U_H,B,I,d)/m0)



#Plotten

#plt.figure()
#plt.plot(I_KupferM,B_KupferM,"k.",label="B")
#plt.plot(I_KupferM ,U_H_KupferM,".",label="UH") 
#plt.plot(x,f(x, *parameter1),label="Fit zu T1")
#plt.plot(x,g(x, *parameter2),label="Fit zu T2")     
#plt.xlabel("Stromstärke [A]")
#plt.ylabel("Temperatur [K]")
#plt.legend()
#plt.tight_layout()
#plt.savefig("build/plot1.pdf")