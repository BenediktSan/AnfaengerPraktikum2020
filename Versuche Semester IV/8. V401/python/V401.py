import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os
from tabulate import tabulate

lam=635 *10**(-9)   #meter
uebersetzung=1/5.056

mess1=np.array([2957,2950,2966,2943,2634,2936,2964,2961])

s1=np.ones(np.size(mess1))
s1*=5*10**(-3)
s1[3]+=0.05*10**(-3)




V=10**(-3)          #kubikmeter

up=np.array([50,20,39,30,26])
down=np.array([32,31,31,30,30 ])


#####Wellenlängen#######
print("Wellenlängen: \n")

us1=unp.uarray(s1,0.002*10**(-3))
d=us1/uebersetzung

umess1=unp.uarray(mess1,40)
