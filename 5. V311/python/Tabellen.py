import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import sympy

np.savetxt(
    'testTabellen/testKupfermag.txt',
    np.column_stack([I_KupferM, B_KupferM,U_H_KupferM]),
    fmt=['%d','%.3f','%.4f'],       
    delimiter=' & ',
    header='I_KupferM, B_KupferM,U_H_KupferM',
)