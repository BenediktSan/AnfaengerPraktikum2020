import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import sympy

I_KupferM, B_KupferM, U_H_KupferM = np.genfromtxt("testMesswerte-simon/UHallKupferMagnetfeld.txt", unpack=True)
np.save('python/variables/I_KupferM.npy', I_KupferM, allow_pickle=False)
np.save('python/variables/B_KupferM.npy', B_KupferM, allow_pickle=False)
np.save('python/variables/U_H_KupferM.npy', U_H_KupferM, allow_pickle=False)

I_KupferP, U_H_KupferP = np.genfromtxt("testMesswerte-simon/UHallKupferStrom.txt", unpack=True)
np.save('python/variables/I_KupferP.npy', I_KupferM, allow_pickle=False)
np.save('python/variables/U_H_KupferP.npy', I_KupferM, allow_pickle=False)

B_KupferP= np.ones(6)*823e-3
np.save('python/variables/B_KupferP.npy', I_KupferM, allow_pickle=False)

I_ZinkM, B_ZinkM, U_H_ZinkM = np.genfromtxt("testMesswerte-simon/UHallKupferMagnetfeld.txt", unpack=True)
np.save('python/variables/I_ZinkrM.npy', I_ZinkM, allow_pickle=False)
np.save('python/variables/B_ZinkM.npy', B_ZinkM, allow_pickle=False)
np.save('python/variables/U_H_ZinkM.npy', U_H_ZinkM, allow_pickle=False)


I_ZinkP, U_H_ZinkP = np.genfromtxt("testMesswerte-simon/UHallKupferStrom.txt", unpack=True)
np.save('python/variables/I_ZinkP.npy', I_ZinkP, allow_pickle=False)
np.save('python/variables/U_H_ZinkP.npy', U_H_ZinkP, allow_pickle=False)
B_ZinkP=np.ones(6)*815e-3
np.save('python/variables/U_H_ZinkM.npy', B_ZinkP, allow_pickle=False)

np.savetxt(
    'testTabellen/testKupfermag.txt',
    np.column_stack([I_KupferM, B_KupferM,U_H_KupferM]),
    fmt=['%d','%.3f','%.4f'],       
    delimiter=' & ',
    header='I_KupferM, B_KupferM,U_H_KupferM',
)