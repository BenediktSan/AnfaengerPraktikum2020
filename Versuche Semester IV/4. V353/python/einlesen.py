import numpy as np
import os

# Variablen Ordner anlegen

if os.path.exists("python/variables") == False:
    os.mkdir("python/variables")
  
###Daten
U_0=0

U1=np.array([1])
t=np.array([1])


U2=np.array([1])
f1=np.array([1])

phi=np.array([1])
f2=np.array([1])






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
    np.column_stack([U2, f1]),
    fmt=['%.3f', '%.3f'],       
    delimiter=' & ',
    header='U2,f',
)

np.savetxt(
    'build/phi.txt',
    np.column_stack([phi, f2]),
    fmt=['%.3f', '%.3f'],       
    delimiter=' & ',
    header='phi in rad,f2',
)