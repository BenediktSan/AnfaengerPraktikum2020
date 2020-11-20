import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import sympy

#1-15 bar
p_1=np.linspace(1,15,15)
np.save('python/variables/p_1.npy', p_1, allow_pickle=False)

T_1=np.array([118,129.5,141,150,157,163.5,168,172.5,177,181.5,185.5,189,192,195,198.5])
#T_1=np.linspace(1,15,29)
np.save('python/variables/T_1.npy', T_1, allow_pickle=False)

T_kel1=T_1+273.15


#bis 1bar
T_2=np.array([22,26,40,51,58,64,69,73,76,79,83,86,88,91,94,97,98,100,102,104,108])
np.save('python/variables/T_2.npy', T_2, allow_pickle=False)

p_2=np.array([30,50,108,153,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000])
np.save('python/variables/p_2.npy', p_2, allow_pickle=False)

T_kel2=T_2+273.15
p_2pasc= p_2*1e5

#Dateien für Messwerttabelle
np.savetxt(
    'Mess1bar.txt',
    np.column_stack([p_2, T_2,np.log(p_2pasc),1/T_kel2]),
    fmt=['%d', '%d','%.3f','%.5f'],       
    delimiter=' & ',
    header='p_2,T_2,log(p),1/T',
)


np.savetxt(
    'Mess15bar.txt',
    np.column_stack([p_1, T_1, T_kel1]),
    fmt=['%d', '%.1f', '%.1f'],       
    delimiter=' & ',
    header='p_1,T_1,T_kel1',
)