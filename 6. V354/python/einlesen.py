import numpy as np
from uncertainties import ufloat
import os

# Variablen Ordner anlegen

if os.path.exists("python/variables") == False:
    os.mkdir("python/variables")
  
###  Vorgegebene Daten einlesen und einspeichern

##einlesen und umrechnen

#Bauteildaten

L=ufloat(16.78,0.09) *(10**-3) #in henry
C=ufloat(2.066,0.066) *(10**-9) #in farrad
R1=ufloat(67.2,0.2) #in ohm
R2=ufloat(682,1 )#in ohm




#zeitabhängige amplitude
Uamp=np.array([14,-11.5,10.5,-8.3,7.8,-6,5.8,-4.2,4.1,-3,3.1,-2.2,2.5]) #in V
tamp=np.array([0,0.7,1.38,2.1,2.7,3.4,4.1,4.75,5.4,6.1,6.8,7.5,8.15]) * (20*10**-6) #in s


#aperiodischer Grenzfall
Rap=np.array([5*0.385])*1000 #in ohm

#Frequenzanhängigkeit der Kondensatorspannung
fc=np.array([5,10,15,20,21,23,24,25,26,27,28.5,30,33,35,40,45,50]) *1000 #in Hz
Uu0=np.array([1.08,1.24,1.44,2.16,2.4,3,3.4,3.72,3.8,3.64,3.12,2.44,1.6,1.24,0.84,0.6,0.44]) 

#frequenzabhängigkeit der phase zwischen cond und und erreger

fd=np.array([5,10,12,14,20,25,30,35,35.75,36.25,36.75,37.5,38,38.25,38.75,40,42.5,45]) *1000 #in Hz
dt=np.array([0,1,1.5,1.5,0,0.5,1,1.5,3,4,6,8,10,11,11,11,11.5,11]) *(10**-6) #in s





##speichern
#Gerätedaten

#a
np.save('python/variables/Uamp.npy', Uamp, allow_pickle=False)
np.save('python/variables/tamp.npy', tamp, allow_pickle=False)

#b
np.save('python/variables/Rap.npy', Rap, allow_pickle=False)

#c
np.save('python/variables/fc.npy', fc, allow_pickle=False)
np.save('python/variables/Uu0.npy', Uu0, allow_pickle=False)

#d
np.save('python/variables/fd.npy', fd, allow_pickle=False)
np.save('python/variables/dt.npy',dt, allow_pickle=False)

