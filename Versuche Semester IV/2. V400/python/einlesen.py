import numpy as np
import os

# Variablen Ordner anlegen

#if os.path.exists("python/variables") == False:
#    os.mkdir("python/variables")
  
###  Vorgegebene Daten einlesen und einspeichern

if os.path.exists("build") == False:
    os.mkdir("build")
#Reflexion

refl1=np.array([0,20,30,40,50,60,70]) #in grad
refl2=np.array([0,20,30,40,51,61,70])
err=0.5

#FOTOS!!!!!!!!!!!!!


#Brechung
brech1=np.array([10,20,30,40,50,60,70]) #in grad
brech2=np.array([7,14,20,26,31,36,39.5])



#Paralelle Platten
d=5.85e-3




#Prisma
gam=60 #grad

green1=np.array([30,35,40,50,60]) 
green2=np.array([76.5,66.5,58.5,47,38]) 

red2=np.array([75,75.5,57.8,46,37.5]) 

#Beugung am Gitter


max1=np.array([0,0,0,0,0,0,0,-23.5,0,23.50,0,0,0,0,0,0,0]) 
max2=np.array([0,0,0,0,0,-35,-22.5,-11,0,35,22.5,11,0,0,0,0,0]) 
max3=np.array([-32,-27.2,-23,-19,-15,-11.3,-7.5,-4,0,3.8,7.2,11,15,19,23,27.2,32]) 
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
    'build/prisma.txt',
    np.column_stack([green1, green2, red2]),
    fmt=['%.3f', '%.3f', '%.3f'],       
    delimiter=' & ',
    header='einf(green & red),ausf',
)

np.savetxt(
    'build/gitter.txt',
    np.column_stack([max1, max2, max3]),
    fmt=['%.3f', '%.3f','%.3f'],       
    delimiter=' & ',
    header='maxima 600promm, maxima 300promm, maxima 100promm',
)