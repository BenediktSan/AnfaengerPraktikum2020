import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties import unumpy
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os

if os.path.exists("build") == False:
    os.mkdir("build")

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


param1=np.load('python/variables/param1.npy')
param2=np.load('python/variables/param2.npy')
param3=np.load('python/variables/param3.npy')
param4=np.load('python/variables/param4.npy')
param5=np.load('python/variables/param5.npy')
param6=np.load('python/variables/param6.npy')

U_H_Zink_I_Sv   = np.load('python/variables/U_H_Zink_I_Sv.npy')
U_H_Kupfer_I_Sv = np.load('python/variables/U_H_Kupfer_I_Sv.npy') 
U_H_Zink_I_Pv   = np.load('python/variables/U_H_Zink_I_Pv.npy')
U_H_Kupfer_I_Pv = np.load('python/variables/U_H_Kupfer_I_Pv.npy')


plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,U_H_Zink_I_Sv,".",label="Spule Zink")
plt.plot(I_s_Zink,I_s_Zink*param3[0]+param3[1],label="Fit zu Spule")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Spannung [mV]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_p_Zink,U_H_Zink_I_Pv,".",label="Probe Zink")
plt.plot(I_p_Zink,I_p_Zink*param5[0]+param5[1],label="Fit zu Probe") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Spannung [mV]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_s_Kupfer ,U_H_Kupfer_I_Sv,".",label="Spule Kupfer")
plt.plot(I_s_Kupfer,I_s_Kupfer*param4[0]+param4[1],label="Fit zu Spule")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Spannung [mV]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,U_H_Kupfer_I_Pv,".",label="Probe Kupfer")
plt.plot(I_p_Kupfer,I_p_Kupfer*param6[0]+param6[1],label="Fit zu Probe") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Spannung [mV]")
plt.legend()
plt.tight_layout()
plt.savefig("build/Hall.pdf")



plt.figure()
plt.plot(I_abfallend ,B_abfallend,".",label="Spule Kupfer")
plt.plot(I_abfallend,I_abfallend*param1[0]+param1[1],label="Fit zu Spule")
plt.plot(I_aufsteigend ,B_aufsteigend,".",label="Probe Kupfer")
plt.plot(I_aufsteigend,I_aufsteigend*param2[0]+param2[1],label="Fit zu Probe") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Magnetfeld [mT]")
plt.legend()
plt.tight_layout()
plt.savefig("build/Magnetfeld.pdf")

n_sZink=np.load('python/variables/n_sZink.npy')
n_sKupfer=np.load('python/variables/n_sKupfer.npy')

n_pZink=np.load('python/variables/n_pZink.npy')
n_pKupfer=np.load('python/variables/n_pKupfer.npy')