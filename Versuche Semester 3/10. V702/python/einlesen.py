import numpy as np
import os

# Variablen Ordner anlegen

if os.path.exists("python/variables") == False:
    os.mkdir("python/variables")
  
###  Vorgegebene Daten einlesen und einspeichern


np.save('python/variables/I_aufsteigend.npy', I_aufsteigend, allow_pickle=False)

