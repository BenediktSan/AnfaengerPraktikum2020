import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import sympy

#1-15 bar
p_1=np.linspace(1,15,29)
np.save('python/variables/p_1.npy', p_1, allow_pickle=False)

#T_1=np.array([1])
T_1=np.linspace(1,15,29)
np.save('python/variables/T_1.npy', T_1, allow_pickle=False)



#bis 1bar
T_2=np.array([5,5])
np.save('python/variables/T_2.npy', T_2, allow_pickle=False)

p_2=np.array([1,63])
np.save('python/variables/p_2.npy', p_2, allow_pickle=False)


#Dateien für Messwerttabelle
np.savetxt(
    'Mess1bar.txt',
    np.column_stack([p_2, T_2]),
    fmt=['%.5f', '%.5f'],       
    delimiter=' & ',
    header='p_2,T_2',
)


np.savetxt(
    'Mess15bar.txt',
    np.column_stack([p_1, T_1]),
    fmt=['%.5f', '%.5f'],       
    delimiter=' & ',
    header='p_1,T_1',
)