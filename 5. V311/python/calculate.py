import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties import unumpy
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

Durch_Zink=2.63e-4
Durch_Kupfer=1.052e-4
L_Zink=1.73
L_Kupfer=1.73
spez_R_Zink=np.pi * Durch_Zink**2 * R_Zink / L_Zink
spez_R_Kupfer=np.pi * Durch_Kupfer**2 * R_Kupfer / L_Kupfer
#       b)
###         Hall-Effekt
U_H_Zink_I_Sv =   0.5*( Zink_Is_U_H_1 +   Zink_Is_U_H_2   )
U_H_Kupfer_I_Sv = 0.5*( Kupfer_Is_U_H_1 + Kupfer_Is_U_H_2 )
U_H_Zink_I_Pv =   0.5*( Zink_Ip_U_H_1 +   Zink_Ip_U_H_2   )
U_H_Kupfer_I_Pv = 0.5*( Kupfer_Ip_U_H_1 + Kupfer_Ip_U_H_2 )

np.save('python/variables/U_H_Zink_I_Sv.npy', U_H_Zink_I_Sv, allow_pickle=False)
np.save('python/variables/U_H_Kupfer_I_Sv.npy', U_H_Kupfer_I_Sv, allow_pickle=False)
np.save('python/variables/U_H_Zink_I_Pv.npy', U_H_Zink_I_Pv, allow_pickle=False)
np.save('python/variables/U_H_Kupfer_I_Pv.npy', U_H_Kupfer_I_Pv, allow_pickle=False)
##konstanter Proben Strom
#Fit
param3, _3 = np.polyfit(I_s_Zink,U_H_Zink_I_Sv, deg=1, cov=True)
param4, _4 = np.polyfit(I_s_Kupfer,U_H_Kupfer_I_Sv, deg=1, cov=True)
err3 = np.sqrt(np.diag(_3))
err4 = np.sqrt(np.diag(_4))
Fit_U_Hall_Is_Zink=unumpy.uarray([param3[0],param3[1]] , [err3[0],err3[1]])
Fit_U_Hall_Is_Kupfer=unumpy.uarray([param4[0],param4[1]], [err4[0],err4[1]])
np.save('python/variables/param3.npy', param3, allow_pickle=False)
np.save('python/variables/param4.npy', param4, allow_pickle=False)

param5, _5 = np.polyfit(I_p_Zink,U_H_Zink_I_Pv, deg=1, cov=True)
param6, _6 = np.polyfit(I_p_Kupfer,U_H_Kupfer_I_Pv, deg=1, cov=True)
err5 = np.sqrt(np.diag(_5))
err6 = np.sqrt(np.diag(_6))
Fit_U_Hall_Ip_Zink=unumpy.uarray([param5[0],param5[1]] , [err5[0],err5[1]])
Fit_U_Hall_Ip_Kupfer=unumpy.uarray([param6[0],param6[1]], [err6[0],err6[1]])

np.save('python/variables/param5.npy', param5, allow_pickle=False)
np.save('python/variables/param6.npy', param6, allow_pickle=False)

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
#Avogadro-Konstante:
NA=6.0221e23
# Dichte Kupfer g/cm^3:
rho_K=8.92 
#Molare Masse Kupfer g/mol:
m_mol_K=63.55  
# Dichte Zink g/cm^3:
rho_Z=7.14
#Molare Masse Zink g/mol:
m_mol_Z=65.38 


# zu berechnen:

#Relation Stromstärke und B-Feld

param1, _1 = np.polyfit(I_abfallend,B_abfallend, deg=1, cov=True)
param2, _2 = np.polyfit(I_aufsteigend,B_aufsteigend, deg=1, cov=True)
err1 = np.sqrt(np.diag(_1))
err2 = np.sqrt(np.diag(_2))
Rel_Auf=unumpy.uarray([param1[0],param1[1]],[err1[0],err1[1]])
Rel_Ab=unumpy.uarray([param2[0],param2[1]],[err2[0],err2[1]])
Rel=1/2*(Rel_Auf+Rel_Ab)
np.save('python/variables/param1.npy', param1, allow_pickle=False)
np.save('python/variables/param2.npy', param2, allow_pickle=False)


#Ladungsträger pro Volumen n
def number(U_H,B,I,d):
    return -B*I/(U_H*e0*d)
n_Zink = number(U_H_Zink_I_Sv,I_s_Zink*Rel[0]+Rel[1],8,Zink_Breite)
n_Kupfer = number(U_H_Kupfer_I_Sv,I_s_Kupfer*Rel[0]+Rel[1],10,Kupfer_Breite)
#print(n_Kupfer)
# Zahl der Ladungsträger pro Atom z
def Zahl(rho,n,m_mol):
    return ( n * m_mol) / ( rho * 6.0221e23 )
Z_Zink = Zahl(7.14,n_Zink,65.38)
Z_Kupfer = Zahl(8.92,n_Kupfer,63.55 )


# mittlere Flugzeit tau:
def Fermi(U_H,B,I,d):
    return (h**2/2*m0) * np.cbrt((3*number(U_H,B,I,d))/8*pi)**(2)

def tau(U_H,B,I,d,b):
    return (-2*m0*b/(e0*U_H)) * np.sqrt((2*Fermi(U_H,B,I,d))/m0)

# mittlere Driftgeschwindigkeit vd

def mitDrift(U_H,B,I,d):
    return -1/(e0*number(U_H,B,I,d))

#Beweglichkeit mue:
def Beweg(U_H,B,I,d,b):
    return -e0*tau(U_H,B,I,d,b)/(2*m0)

#Totalgeschwindigkeit v:
def vTot(T):
    return np.sqrt(3*k*T/m0)

#mittlere freie Weglänge l:
def mWeg(U_H,B,I,d,b):
    return tau(U_H,B,I,d,b)*np.sqrt(2*Fermi(U_H,B,I,d)/m0)


