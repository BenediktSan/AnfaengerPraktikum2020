import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
from scipy.signal import find_peaks
import sympy
import os
from tabulate import tabulate


n_3 , T1_3 , T2_3 , T3_3 , T4_3 , T5_3 , T6_3 , T7_3 , T8_3 = np.genfromtxt("python/Daten/GLXportRun3.txt", unpack =True)


p = find_peaks(T7_3)
print(p)