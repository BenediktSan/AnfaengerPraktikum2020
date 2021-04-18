import numpy as np
import os

# Variablen Ordner anlegen

#if os.path.exists("python/variables") == False:
#    os.mkdir("python/variables")
  
###  Vorgegebene Daten einlesen und einspeichern

if os.path.exists("build") == False:
    os.mkdir("build")
#Reflexion

refl1=np.array([1,2,3,4,5,6,7]) #in grad
refl2=np.array([1,2,3,4,5,6,7])
err=1

#FOTOS!!!!!!!!!!!!!


#Brechung
brech1=np.array([1,2,3,4,5,6,7]) #in grad
brech2=np.array([1,2,3,4,5,6,7])



#Paralelle Platten
d=5.85e-3


platt1=np.array([1,2,3,4,5]) 
platt2=np.array([1,2,3,4,5]) 



#Prisma
gam=60 #grad

green1=np.array([1,2,3,4,5]) 
green2=np.array([1,2,3,4,5]) 

red1=green1
red2=green2=np.array([1,2,3,4,5]) 



#Beugung am Gitter

maxgreen=np.array([1,2,3,4,5]) 
maxred=np.array([1,2,3,4,5]) 


#np.save('python/variables/refl1.npy', refl1, allow_pickle=False)
#np.save('python/variables/refl2.npy', refl2, allow_pickle=False)


np.savetxt(
    'build/reflektion.txt',
    np.column_stack([refl1, refl2]),
    fmt=['%.3f', '%.3f'],       
    delimiter=' & ',
    header='einf,ausf',
)

np.savetxt(
    'build/reflektion.txt',
    np.column_stack([refl1, refl2]),
    fmt=['%.3f', '%.3f'],       
    delimiter=' & ',
    header='einf,ausf',
)

np.savetxt(
    'build/brechung.txt',
    np.column_stack([brech1, brech2]),
    fmt=['%.3f', '%.3f'],       
    delimiter=' & ',
    header='einf,ausf',
)

np.savetxt(
    'build/platten.txt',
    np.column_stack([platt1, platt2]),
    fmt=['%.3f', '%.3f'],       
    delimiter=' & ',
    header='einf,ausf',
)

np.savetxt(
    'build/prisma.txt',
    np.column_stack([green1, green2, red2]),
    fmt=['%.3f', '%.3f', '%.3f'],       
    delimiter=' & ',
    header='einf(green & red),ausf',
)

np.savetxt(
    'build/prisma.txt',
    np.column_stack([maxgreen, maxred]),
    fmt=['%.3f', '%.3f'],       
    delimiter=' & ',
    header='maxima grün, max rot',
)