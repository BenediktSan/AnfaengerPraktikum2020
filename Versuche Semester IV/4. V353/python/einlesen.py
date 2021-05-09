import numpy as np
import os

# Variablen Ordner anlegen

if os.path.exists("build") == False:
    os.mkdir("build")


if os.path.exists("python/variables") == False:
    os.mkdir("python/variables")
  
###Daten
U_0=1

U1=np.array([0.62,0.52,0.42,0.34,0.29,0.24,0.2,0.17,0.125,0.1,0.085,0.07,0.06,0.05,0.04,0.03,0.02,0.01,0.001]) #Volt
t=np.array([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,36,46]) * 10**-3 ###sekunden


U2=np.array([0.32,0.33,0.305,0.28,0.26,0.19,0.145,0.1,0.068,0.052,0.021,0.011,0.00505,0.004,0.003,0.001])   #Volt
f1=np.array([10,25,50,75,100,200,300,500,750,1000,2500,5000,10000,15000,20000,50000])   #Hz

a=np.array([1,1.2,0.9,0.6,0.38,0.27,0.21,0.15,0.1,0.058,0.04,0.029,0.024,0.015,0.011]) *10**-3 #sekunden
f2=np.array([25,50,100,250,500,750,1000,1500,2000,4000,6000,8000,10000,15000,20000]) #Hz


phi=a*f2*np.pi*2







###  Vorgegebene Daten einlesen und einspeichern


np.save('python/variables/U1.npy', U1, allow_pickle=False)
np.save('python/variables/t.npy', t, allow_pickle=False)
np.save('python/variables/u2.npy', U2, allow_pickle=False)
np.save('python/variables/f1.npy', f1, allow_pickle=False)
np.save('python/variables/phi.npy', phi, allow_pickle=False)
np.save('python/variables/f2.npy', f2, allow_pickle=False)

np.savetxt(
    'build/ln.txt',
    np.column_stack([U1, np.log(U1/U_0), t]),
    fmt=['%.3f', '%.3f', '%.3f'],       
    delimiter=' & ',
    header='U1,ln(u/u0),t',
)

np.savetxt(
    'build/f.txt',
    np.column_stack([U2,U2/U2[0], f1]),
    fmt=['%.3f', '%.3f', '%.3f'],       
    delimiter=' & ',
    header='U2,U/U0,f',
)

np.savetxt(
    'build/phi.txt',
    np.column_stack([a*10**3,phi, f2]),
    fmt=['%.3f','%.3f', '%.3f'],       
    delimiter=' & ',
    header='a,phi in rad,f2',
)