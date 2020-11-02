import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import sympy




np.savetxt(
    'data.txt',
    np.column_stack([n, x]),
    fmt=['%d', '%.6f'],      
    delimiter=',',
    header='n,x',
)