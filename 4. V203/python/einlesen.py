import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import sympy

#1-15 bar
p_1=np.linspace(1,15,29)
np.save('variables/p_1.npy', p_1, allow_pickle=False)

T_1=np.array([1])
np.save('variables/T_1.npy', T_1, allow_pickle=False)



#bis 1bar
T_2=np.array([5,5])
np.save('variables/T_2.npy', T_2, allow_pickle=False)

p_2=np.array([1,63])
np.save('variables/p_2.npy', p_2, allow_pickle=False)