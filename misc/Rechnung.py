import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os


###Konstanten

# Elementarladung e0:
e0=const.elementary_charge
# Elektronenmasse m0:
m0=const.m_e
m_p=const.m_p
m_n=const.m_n
#pi:
pi=np.pi
#Planksches Wirkungsquantum h:
h=const.h
hbar=const.hbar
#Boltzmannsche Konstante k:
k=const.k
#Avogadro-Konstante:
NA=const.Avogadro

c=const.chemie



##Rechnung:

