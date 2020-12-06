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

if os.path.exists("build/Tabellen") == False:
    os.mkdir("build/Tabellen")

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


np.savetxt(
    'build/Tabellen/Hallsonde.txt',
    np.column_stack([I_aufsteigend, B_aufsteigend, I_abfallend, B_abfallend]),
    fmt="%-12s",       
    delimiter=' & ',
    header='I_aufsteigend, B_aufsteigend, I_abfallend, B_abfallend',
)

#Dim=["Höhe","Breite","Dicke"]
#
#np.savetxt(
#    'build/Tabellen/Abmessungen.txt',
#    np.column_stack([Dim, Zink, Kupfer]),
#    fmt="%-12s",       
#    delimiter=' & ',
#    header='Dimensionen, Zink, Kupfer',
#)

np.savetxt(
    'build/Tabellen/Widerstand.txt',
    np.column_stack([I_Widerstand, U_Widerstand_Zink, U_Widerstand_Kupfer]),
    fmt="%-12s",       
    delimiter=' & ',
    header='I_Widerstand, U_Widerstand_Zink, U_Widerstand_Kupfer',
)

np.savetxt(
    'build/Tabellen/U_Hall_konst_Probe_Zink.txt',
    np.column_stack([I_s_Zink, Zink_Is_U_H_1, Zink_Is_U_H_2]),
    fmt=['%.2f','%.6f','%.6f',],       
    delimiter=' & ',
    header='I_s_Zink, Zink_Is_U_H_1, Zink_Is_U_H_2',
)

np.savetxt(
    'build/Tabellen/U_Hall_konst_Probe_Kupfer.txt',
    np.column_stack([I_s_Kupfer, Kupfer_Is_U_H_1, Kupfer_Is_U_H_2]),
    fmt=['%.2f','%.6f','%.6f',],       
    delimiter=' & ',
    header='I_s_Kupfer, Kupfer_Is_U_H_1, Kupfer_Is_U_H_2',
)

np.savetxt(
    'build/Tabellen/U_Hall_konst_Spule_Zink.txt',
    np.column_stack([I_p_Zink, Zink_Ip_U_H_1, Zink_Ip_U_H_2]),
    fmt=['%.2f','%.6f','%.6f',],       
    delimiter=' & ',
    header='I_s_Zink, Zink_Is_U_H_1, Zink_Is_U_H_2',
)

np.savetxt(
    'build/Tabellen/U_Hall_konst_Spule_Kupfer.txt',
    np.column_stack([I_p_Kupfer, Kupfer_Ip_U_H_1, Kupfer_Ip_U_H_2]),
    fmt=['%.2f','%.6f','%.6f',],       
    delimiter=' & ',
    header='I_s_Kupfer, Kupfer_Is_U_H_1, Kupfer_Is_U_H_2',
)

R_Zink_array = np.load('python/variables/R_Zink_array.npy', allow_pickle=False)
R_Kupfer_array = np.load('python/variables/R_Kupfer_array.npy', allow_pickle=False)

np.savetxt(
    'build/Tabellen/R_Erg.txt',
    np.column_stack([R_Zink_array, R_Kupfer_array]),
    fmt="%-4s",       
    delimiter=' & ',
    header='R_Zink_array, R_Kupfer_array',
)
n_sZink=np.load('python/variables/n_sZink.npy', allow_pickle=True)
n_sKupfer=np.load('python/variables/n_sKupfer.npy', allow_pickle=True)
app=unumpy.uarray([0,0,0],[0,0,0])
n_sKupfer = np.append(n_sKupfer,app,axis=0)

n_pZink=np.load('python/variables/n_pZink.npy', allow_pickle=True)
n_pKupfer=np.load('python/variables/n_pKupfer.npy', allow_pickle=True)

np.savetxt(
    'build/Tabellen/nwerte.txt',
    np.column_stack([unumpy.nominal_values(n_sZink)/1e24,unumpy.std_devs(n_sZink)/1e24
     ,unumpy.nominal_values(n_sKupfer)/1e24, unumpy.std_devs(n_sKupfer)/1e24
     ,unumpy.nominal_values(n_pZink)/1e24,unumpy.std_devs(n_pZink)/1e24
     ,unumpy.nominal_values(n_pKupfer)/1e24,unumpy.std_devs(n_pKupfer)/1e24
     ]),

    fmt=['%.3f','%.3f','%.3f','%.3f','%.3f','%.3f','%.3f','%.3f'],       
    delimiter=' & ',
    header='n_sZinkvalue, n_sZinkerror, n_sZinkerror, n_sZinkerror'
)

Z_sZink = np.load('python/variables/Z_sZink.npy', allow_pickle=True)
Z_sKupfer = np.load('python/variables/Z_sKupfer.npy', allow_pickle=True)
app=unumpy.uarray([0,0,0],[0,0,0])
Z_sKupfer = np.append(Z_sKupfer,app,axis=0)
Z_pZink = np.load('python/variables/Z_pZink.npy', allow_pickle=True)
Z_pKupfer = np.load('python/variables/Z_pKupfer.npy', allow_pickle=True)

np.savetxt(
    'build/Tabellen/Z.txt',
    np.column_stack([unumpy.nominal_values(Z_sZink),unumpy.std_devs(Z_sZink)
     ,unumpy.nominal_values(Z_sKupfer), unumpy.std_devs(Z_sKupfer)
     ,unumpy.nominal_values(Z_pZink),unumpy.std_devs(Z_pZink)
     ,unumpy.nominal_values(Z_pKupfer),unumpy.std_devs(Z_pKupfer)
     ]),

    fmt=['%.5f','%.5f','%.5f','%.5f','%.5f','%.5f','%.5f','%.5f'],       
    delimiter=' & ',
    header='n_sZinkvalue, n_sZinkerror, n_sZinkerror, n_sZinkerror'
)

tau_sZink = np.load('python/variables/tau_sZink.npy', allow_pickle=True)
tau_sKupfer = np.load('python/variables/tau_sKupfer.npy', allow_pickle=True)
tau_sKupfer =np.append(tau_sKupfer,app,axis=0)
tau_pZink = np.load('python/variables/tau_pZink.npy', allow_pickle=True)
tau_pKupfer = np.load('python/variables/tau_pKupfer.npy', allow_pickle=True)

np.savetxt(
    'build/Tabellen/tau.txt',
    np.column_stack([unumpy.nominal_values(tau_sZink)*1e9,unumpy.std_devs(tau_sZink)*1e9
     ,unumpy.nominal_values(tau_sKupfer)*1e9, unumpy.std_devs(tau_sKupfer)*1e9
     ,unumpy.nominal_values(tau_pZink)*1e9,unumpy.std_devs(tau_pZink)*1e9
     ,unumpy.nominal_values(tau_pKupfer)*1e9,unumpy.std_devs(tau_pKupfer)*1e9
     ]),

    fmt=['%.5f','%.5f','%.5f','%.5f','%.5f','%.5f','%.5f','%.5f'],       
    delimiter=' & ',
    header='n_sZinkvalue, n_sZinkerror, n_sZinkerror, n_sZinkerror'
)

vd_sZink = np.load('python/variables/vd_sZink.npy', allow_pickle=True)
vd_sKupfer = np.load('python/variables/vd_sKupfer.npy', allow_pickle=True)
vd_sKupfer = np.append(vd_sKupfer,app,axis=0)

vd_pZink = np.load('python/variables/vd_pZink.npy', allow_pickle=True)
vd_pKupfer = np.load('python/variables/vd_pKupfer.npy', allow_pickle=True)

np.savetxt(
    'build/Tabellen/vd.txt',
    np.column_stack([unumpy.nominal_values(vd_sZink)*1e15,unumpy.std_devs(vd_sZink)*1e15
     ,unumpy.nominal_values(vd_sKupfer)*1e15, unumpy.std_devs(vd_sKupfer)*1e15
     ,unumpy.nominal_values(vd_pZink)*1e15,unumpy.std_devs(vd_pZink)*1e15
     ,unumpy.nominal_values(vd_pKupfer)*1e15,unumpy.std_devs(vd_pKupfer)*1e15
     ]),

    fmt=['%.3f','%.3f','%.3f','%.3f','%.3f','%.3f','%.3f','%.3f'],       
    delimiter=' & ',
    header='n_sZinkvalue, n_sZinkerror, n_sZinkerror, n_sZinkerror'
)

Beweg_sZink = np.load('python/variables/Beweg_sZink.npy', allow_pickle=True)
Beweg_sKupfer = np.load('python/variables/Beweg_sKupfer.npy', allow_pickle=True)
Beweg_sKupfer = np.append(Beweg_sKupfer,app,axis=0)

Beweg_pZink = np.load('python/variables/Beweg_pZink.npy', allow_pickle=True)
Beweg_pKupfer = np.load('python/variables/Beweg_pKupfer.npy', allow_pickle=True)

np.savetxt(
    'build/Tabellen/vd.txt',
    np.column_stack([unumpy.nominal_values(vd_sZink)*1e15,unumpy.std_devs(vd_sZink)*1e15
     ,unumpy.nominal_values(vd_sKupfer)*1e15, unumpy.std_devs(vd_sKupfer)*1e15
     ,unumpy.nominal_values(vd_pZink)*1e15,unumpy.std_devs(vd_pZink)*1e15
     ,unumpy.nominal_values(vd_pKupfer)*1e15,unumpy.std_devs(vd_pKupfer)*1e15
     ]),

    fmt=['%.3f','%.3f','%.3f','%.3f','%.3f','%.3f','%.3f','%.3f'],       
    delimiter=' & ',
    header='n_sZinkvalue, n_sZinkerror, n_sZinkerror, n_sZinkerror'
)