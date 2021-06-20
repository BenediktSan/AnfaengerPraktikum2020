import numpy as np
import os

# Variablen Ordner anlegen

if os.path.exists("python/variables") == False:
    os.mkdir("python/variables")
  
###  Vorgegebene Daten einlesen und einspeichern

print("a) 1.", 332 * (542/ 458))
print("a) 2.", 664 * (370/630))

print("b) 1. R_x : " , 205 * (580/420))
print("b) 1. C_x : " , 750e-9 * (420/580))

print("b) 2. R_x : " , 503 * (451/549))
print("b) 2. C_x : " , 399e-9 * (548/452))


print('c) R_x:' ,  104 * (775/225))
print('c) L_x' , 14.6 *(225/775))

print(' d) R_x: ' , 1000 * 64 / 638)
print('d) L_x: ' , 1000 * 64 * 399e-9)


print("f) 1. v_0 :" , 1/ (1000 * 295e-9 * 2 * np.pi))