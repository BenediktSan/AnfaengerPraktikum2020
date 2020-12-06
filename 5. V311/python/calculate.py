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
Zink_Breite=ufloat(Zink[1],Zink[1]*1e-2)
Zink_Dicke=ufloat(Zink[2],Zink[2]*1e-2)
Kupfer_Breite=ufloat(Kupfer[1],Kupfer[1]*1e-2)
Kupfer_Dicke=ufloat(Kupfer[2],Kupfer[2]*1e-2)
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
np.save('python/variables/R_Zink_array.npy', R_Zink_array, allow_pickle=False)
np.save('python/variables/R_Kupfer_array.npy', R_Kupfer_array, allow_pickle=False)
R_Zink=ufloat(np.mean(R_Zink_array),np.std(R_Zink_array))
R_Kupfer=ufloat(np.mean(R_Kupfer_array),np.std(R_Kupfer_array))

Durch_Zink=ufloat(2.63e-4,2.63e-6)
Durch_Kupfer=ufloat(1.052e-4,1.052e-6)
L_Zink=1.73
L_Kupfer=1.73
spez_R_Zink=np.pi * Durch_Zink**2 * R_Zink /(4* L_Zink)
spez_R_Kupfer=np.pi * Durch_Kupfer**2 * R_Kupfer /(4* L_Kupfer)
print(spez_R_Zink)
print(spez_R_Kupfer)
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
e0=-1.602e-19
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
print(Rel)
np.save('python/variables/param1.npy', param1, allow_pickle=False)
np.save('python/variables/param2.npy', param2, allow_pickle=False)


#Ladungsträger pro Volumen n
#def number(B,I,U_H,d):
#return -B*I/(U_H*e0*d)
#n_Zink = number(I_s_Zink*Rel[0]+Rel[1],8,U_H_Zink_I_Sv,Zink_Dicke)
#n_Kupfer = number(I_s_Kupfer*Rel[0]+Rel[1],10,U_H_Kupfer_I_Sv,Kupfer_Dicke)


n_sZink =  -(I_s_Zink*Rel[0]+Rel[1])*8/(U_H_Zink_I_Sv * e0 * Zink_Dicke)
n_sKupfer= (I_s_Kupfer*Rel[0]+Rel[1])*10/(U_H_Kupfer_I_Sv * e0 * Kupfer_Dicke)

n_pZink = -(5*Rel[0]+Rel[1]) * I_p_Zink / (U_H_Zink_I_Pv* e0 * Zink_Dicke)
n_pKupfer = (3*Rel[0]+Rel[1]) * I_p_Kupfer / (U_H_Kupfer_I_Pv* e0 * Kupfer_Dicke)



np.save('python/variables/n_sZink.npy', n_sZink, allow_pickle=True)
np.save('python/variables/n_sKupfer.npy', n_sKupfer, allow_pickle=True)

np.save('python/variables/n_pZink.npy', n_pZink, allow_pickle=True)
np.save('python/variables/n_pKupfer.npy', n_pKupfer, allow_pickle=True)
# Zahl der Ladungsträger pro Atom z

def Zahl(rho,n,m_mol):
    return ( n * m_mol) / ( rho * NA * 1e6)

Z_sZink = Zahl(7.14,n_sZink,65.38)
Z_sKupfer = Zahl(8.92,n_sKupfer,63.55)

Z_pZink = Zahl(7.14,n_pZink,65.38)
Z_pKupfer = Zahl(8.92,n_pKupfer,63.55)

np.save('python/variables/Z_sZink.npy', Z_sZink, allow_pickle=True)
np.save('python/variables/Z_sKupfer.npy', Z_sKupfer, allow_pickle=True)

np.save('python/variables/Z_pZink.npy', Z_pZink, allow_pickle=True)
np.save('python/variables/Z_pKupfer.npy', Z_pKupfer, allow_pickle=True)

# mittlere Flugzeit tau:

def tau(n,spez_R):
    return (2 * m0 ) / ((e0 ** 2) * n * spez_R)

tau_sZink = tau(n_sZink , spez_R_Zink)
tau_sKupfer = tau(n_sKupfer , spez_R_Kupfer)

tau_pZink = tau(n_pZink , spez_R_Zink)
tau_pKupfer = tau(n_pKupfer , spez_R_Kupfer)
np.save('python/variables/tau_sZink.npy', tau_sZink, allow_pickle=True)
np.save('python/variables/tau_sKupfer.npy', tau_sKupfer, allow_pickle=True)

np.save('python/variables/tau_pZink.npy', tau_pZink, allow_pickle=True)
np.save('python/variables/tau_pKupfer.npy', tau_pKupfer, allow_pickle=True)

# mittlere Driftgeschwindigkeit vd

def mitDrift(n):
    return -1e-6/(e0*n)

vd_sZink = mitDrift(n_sZink)
vd_sKupfer = mitDrift(n_sKupfer)

vd_pZink = mitDrift(n_pZink)
vd_pKupfer = mitDrift(n_pKupfer)

np.save('python/variables/vd_sZink.npy', vd_sZink, allow_pickle=True)
np.save('python/variables/vd_sKupfer.npy', vd_sKupfer, allow_pickle=True)

np.save('python/variables/vd_pZink.npy', vd_pZink, allow_pickle=True)
np.save('python/variables/vd_pKupfer.npy', vd_pKupfer, allow_pickle=True)
#Beweglichkeit mue:

def Beweg(tau):
    return -e0*tau/(2*m0)

Beweg_sZink= Beweg(tau_sZink)
Beweg_sKupfer = Beweg(tau_sKupfer)

Beweg_pZink= Beweg(tau_pZink)
Beweg_pKupfer = Beweg(tau_pZink)

np.save('python/variables/Beweg_sZink.npy', Beweg_sZink, allow_pickle=True)
np.save('python/variables/Beweg_sKupfer.npy', Beweg_sKupfer, allow_pickle=True)

np.save('python/variables/Beweg_pZink.npy', Beweg_pZink, allow_pickle=True)
np.save('python/variables/Beweg_pKupfer.npy', Beweg_pKupfer, allow_pickle=True)

#Totalgeschwindigkeit v:
def Fermi(n):
    return ((h**2)*((3*n)/8*np.pi)**(2/3))/(2*m0)

FE_sZink = Fermi(n_sZink)
FE_sKupfer = Fermi(n_sKupfer)

FE_pZink = Fermi(n_pZink)
FE_pKupfer = Fermi(n_pKupfer)


np.save('python/variables/FE_sZink.npy', FE_sZink, allow_pickle=True)
np.save('python/variables/FE_sKupfer.npy', FE_sKupfer, allow_pickle=True)

np.save('python/variables/FE_pZink.npy', FE_pZink, allow_pickle=True)
np.save('python/variables/FE_pKupfer.npy', FE_pKupfer, allow_pickle=True)

def vTot(Fermi):
    return (2 * Fermi / m0)**0.5

vT_sZink = vTot(FE_sZink)
vT_sKupfer = vTot(FE_sKupfer)

vT_pZink = vTot(FE_pZink)
vT_pKupfer = vTot(FE_pKupfer)

np.save('python/variables/vT_sZink.npy', vT_sZink, allow_pickle=True)
np.save('python/variables/vT_sKupfer.npy', vT_sKupfer, allow_pickle=True)

np.save('python/variables/vT_pZink.npy', vT_pZink, allow_pickle=True)
np.save('python/variables/vT_pKupfer.npy', vT_pKupfer, allow_pickle=True)

#mittlere freie Weglänge l:


def mWeg(tau,vTot):
    return tau*vTot

mWeg_sZink = mWeg(tau_sZink, vT_sZink)
mWeg_sKupfer = mWeg(tau_sKupfer, vT_sKupfer)

mWeg_pZink = mWeg(tau_pZink, vT_pZink)
mWeg_pKupfer = mWeg(tau_pKupfer, vT_pKupfer)

np.save('python/variables/mWeg_sZink.npy', mWeg_sZink, allow_pickle=True)
np.save('python/variables/mWeg_sKupfer.npy', mWeg_sKupfer, allow_pickle=True)

np.save('python/variables/mWeg_pZink.npy', mWeg_pZink, allow_pickle=True)
np.save('python/variables/mWeg_pKupfer.npy', mWeg_pKupfer, allow_pickle=True)

