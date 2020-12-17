import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os



if os.path.exists("python/tabellen") == False:
    os.mkdir("python/tabellen")

###werte einlesen

tamp = np.load('python/variables/tamp.npy')
Uamp = np.load('python/variables/Uamp.npy')

Rap = np.load('python/variables/Rap.npy')

Uu0 = np.load('python/variables/Uu0.npy')
fc = np.load('python/variables/fc.npy')

dt = np.load('python/variables/dt.npy')
fd = np.load('python/variables/fd.npy')





np.savetxt(
    'python/tabellen/Amplitude.txt',
    np.column_stack([Uamp,tamp*10**6]),
    fmt=['%.1f', '%.2f'],       
    delimiter=' & ',
    header='Uamp,tamp *10^-6',
)

np.savetxt(
    'python/tabellen/Uu0.txt',
    np.column_stack([Uu0,fc]),
    fmt=['%.2f', '%.d'],       
    delimiter=' & ',
    header='U/U0,f',
)

np.savetxt(
    'python/tabellen/phi.txt',
    np.column_stack([fd,dt*10**6,(dt*fd*2*np.pi)]),
    fmt=['%.d', '%.1f','%.3f'],       
    delimiter=' & ',
    header='fd,dt*10^-6,phi',
)