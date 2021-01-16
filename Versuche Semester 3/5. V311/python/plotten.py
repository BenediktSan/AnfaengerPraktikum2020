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
plt.plot(I_s_Zink,U_H_Zink_I_Sv*1e3,".",label="Spulestrom Zink")
plt.plot(I_s_Zink,(I_s_Zink*param3[0]+param3[1])*1e3,label="Fit")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Spannung [mV]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,U_H_Kupfer_I_Sv*1e3,".",label="Spulestrom Kupfer")
plt.plot(I_s_Kupfer,(I_s_Kupfer*param4[0]+param4[1])*1e3,label="Fit")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Spannung [mV]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,U_H_Zink_I_Pv*1e3,".",label="Probestrom Zink")
plt.plot(I_p_Zink,(I_p_Zink*param5[0]+param5[1])*1e3,label="Fit") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Spannung [mV]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,U_H_Kupfer_I_Pv*1e3,".",label="Probestrom Kupfer")
plt.plot(I_p_Kupfer,(I_p_Kupfer*param6[0]+param6[1])*1e3,label="Fit") 
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

n_sZink=np.load('python/variables/n_sZink.npy', allow_pickle=True)
n_sKupfer=np.load('python/variables/n_sKupfer.npy', allow_pickle=True)

n_pZink=np.load('python/variables/n_pZink.npy', allow_pickle=True)
n_pKupfer=np.load('python/variables/n_pKupfer.npy', allow_pickle=True)

plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,unumpy.nominal_values(n_sZink),".",label="I_Spule Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Elektronendichte [m^-3]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,unumpy.nominal_values(n_sKupfer),".",label="I_Spule Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Elektronendichte [m^-3]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,unumpy.nominal_values(n_pZink),".",label="I_Probe Zink") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Elektronendichte [m^-3]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,unumpy.nominal_values(n_pKupfer),".",label="I_Probe Kupfer") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Elektronendichte [m^-3]")
plt.legend()
plt.tight_layout()
plt.savefig("build/n.pdf")


Z_sZink = np.load('python/variables/Z_sZink.npy', allow_pickle=True)
Z_sKupfer = np.load('python/variables/Z_sKupfer.npy', allow_pickle=True)

Z_pZink = np.load('python/variables/Z_pZink.npy', allow_pickle=True)
Z_pKupfer = np.load('python/variables/Z_pKupfer.npy', allow_pickle=True)

plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,unumpy.nominal_values(Z_sZink),".",label="I_Spule Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Elektron pro Atom")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,unumpy.nominal_values(Z_sKupfer),".",label="I_Spule Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Elektron pro Atom")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,unumpy.nominal_values(Z_pZink),".",label="I_Probe Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Elektron pro Atom")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,unumpy.nominal_values(Z_pKupfer),".",label="I_Probe Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Elektron pro Atom")
plt.legend()
plt.tight_layout()
plt.savefig("build/Z.pdf")

tau_sZink = np.load('python/variables/tau_sZink.npy', allow_pickle=True)
tau_sKupfer = np.load('python/variables/tau_sKupfer.npy', allow_pickle=True)

tau_pZink = np.load('python/variables/tau_pZink.npy', allow_pickle=True)
tau_pKupfer = np.load('python/variables/tau_pKupfer.npy', allow_pickle=True)

plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,unumpy.nominal_values(tau_sZink),".",label="I_Spule Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("mittlere Flugzeit [s]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,unumpy.nominal_values(tau_sKupfer),".",label="I_Spule Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("mittlere Flugzeit [s]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,unumpy.nominal_values(tau_pZink),".",label="I_Probe Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("mittlere Flugzeit [s]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,unumpy.nominal_values(tau_pKupfer),".",label="I_Probe Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("mittlere Flugzeit [s]")
plt.legend()
plt.tight_layout()
plt.savefig("build/tau.pdf")

vd_sZink = np.load('python/variables/vd_sZink.npy', allow_pickle=True)
vd_sKupfer = np.load('python/variables/vd_sKupfer.npy', allow_pickle=True)

vd_pZink = np.load('python/variables/vd_pZink.npy', allow_pickle=True)
vd_pKupfer = np.load('python/variables/vd_pKupfer.npy', allow_pickle=True)

plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,unumpy.nominal_values(vd_sZink),".",label="I_Spule Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Geschindigkeit [m/s]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,unumpy.nominal_values(vd_sKupfer),".",label="I_Spule Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Geschindigkeit [m/s]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,unumpy.nominal_values(vd_pZink),".",label="I_Probe Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Geschindigkeit [m/s]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,unumpy.nominal_values(vd_pKupfer),".",label="I_Probe Kupfer") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Geschindigkeit [m/s]")
plt.legend()
plt.tight_layout()
plt.savefig("build/Driftgeschwindigkeit.pdf")

Beweg_sZink = np.load('python/variables/Beweg_sZink.npy', allow_pickle=True)
Beweg_sKupfer = np.load('python/variables/Beweg_sKupfer.npy', allow_pickle=True)

Beweg_pZink = np.load('python/variables/Beweg_pZink.npy', allow_pickle=True)
Beweg_pKupfer = np.load('python/variables/Beweg_pKupfer.npy', allow_pickle=True)

plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,unumpy.nominal_values(Beweg_sZink),".",label="I_Spule Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Beweglichleit [As^2/kg]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,unumpy.nominal_values(Beweg_sKupfer),".",label="I_Spule Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Beweglichleit [As^2/kg]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,unumpy.nominal_values(Beweg_pZink),".",label="I_Probe Zink") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Beweglichleit [As^2/kg]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,unumpy.nominal_values(Beweg_pKupfer),".",label="I_Probe Kupfer") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Beweglichleit [As^2/kg]")
plt.legend()
plt.tight_layout()
plt.savefig("build/Beweglichkeit.pdf")

vT_sZink = np.load('python/variables/vT_sZink.npy', allow_pickle=True)
vT_sKupfer = np.load('python/variables/vT_sKupfer.npy', allow_pickle=True)

vT_pZink = np.load('python/variables/vT_pZink.npy', allow_pickle=True)
vT_pKupfer = np.load('python/variables/vT_pKupfer.npy', allow_pickle=True)

plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,unumpy.nominal_values(vT_sZink),".",label="I_Spule Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Totalgeschindigkeit [m/s]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,unumpy.nominal_values(vT_sKupfer),".",label="I_Spule Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Totalgeschindigkeit [m/s]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,unumpy.nominal_values(vT_pZink),".",label="I_Probe Zink") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Totalgeschindigkeit [m/s]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,unumpy.nominal_values(vT_pKupfer),".",label="I_Probe Kupfer") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("Totalgeschindigkeit [m/s]")
plt.legend()
plt.tight_layout()
plt.savefig("build/Totalgeschwindigkeit.pdf")

mWeg_sZink = np.load('python/variables/mWeg_sZink.npy', allow_pickle=True)
mWeg_sKupfer = np.load('python/variables/mWeg_sKupfer.npy', allow_pickle=True)

mWeg_pZink = np.load('python/variables/mWeg_pZink.npy', allow_pickle=True)
mWeg_pKupfer = np.load('python/variables/mWeg_pKupfer.npy', allow_pickle=True)

plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,unumpy.nominal_values(mWeg_sZink),".",label="I_Spule Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("mittlere Weglänge [m]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,unumpy.nominal_values(mWeg_sKupfer),".",label="I_Spule Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("mittlere Weglänge [m]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,unumpy.nominal_values(mWeg_pZink),".",label="I_Probe Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("mittlere Weglänge [m]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,unumpy.nominal_values(mWeg_pKupfer),".",label="I_Probe Kupfer") 
plt.xlabel("Stromstärke [A]")
plt.ylabel("mittlere Weglänge [m]")
plt.legend()
plt.tight_layout()
plt.savefig("build/mittlere_Weglänge.pdf")

FE_sZink= np.load('python/variables/FE_sZink.npy', allow_pickle=True)
FE_sKupfer = np.load('python/variables/FE_sKupfer.npy', allow_pickle=True)

FE_pZink = np.load('python/variables/FE_pZink.npy', allow_pickle=True)
FE_pKupfer = np.load('python/variables/FE_pKupfer.npy', allow_pickle=True)

e0=-1.602e-19

plt.figure()
plt.subplot(2,2,1)
plt.plot(I_s_Zink,unumpy.nominal_values(FE_sZink)/-e0,".",label="I_Spule Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Fermi Energie [eV]")
plt.legend()

plt.subplot(2,2,2)
plt.plot(I_s_Kupfer ,unumpy.nominal_values(FE_sKupfer)/-e0,".",label="I_Spule Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Fermi Energie [eV]")
plt.legend()

plt.subplot(2,2,3)
plt.plot(I_p_Zink,unumpy.nominal_values(FE_pZink)/-e0,".",label="I_Probe Zink")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Fermi Energie [eV]")
plt.legend()

plt.subplot(2,2,4)
plt.plot(I_p_Kupfer ,unumpy.nominal_values(FE_pKupfer)/-e0,".",label="I_Probe Kupfer")
plt.xlabel("Stromstärke [A]")
plt.ylabel("Fermi Energie [eV]")
plt.legend()
plt.tight_layout()
plt.savefig("build/Fermi.pdf")