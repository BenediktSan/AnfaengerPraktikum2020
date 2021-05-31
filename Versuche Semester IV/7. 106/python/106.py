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

## Einlesen der Werte
g = const.g
l_1 = 0.25
l_2 = 0.35

gl_1_1 , gl_2_1 , geg_1 , gl_1_2 , gl_2_2 , geg_2 = np.genfromtxt("python/Data1.dat", unpack=True)
gek_t_1 , gek_s_1 , gek_t_2 , gek_s_2 = np.genfromtxt("python/Data2.dat", unpack=True)


## Schwingungs/Schwebungsdauern auf eine Schwingung reduzieren
gl_1_1 *= 0.2
gl_2_1 *= 0.2
geg_1  *= 0.2
gl_1_2 *= 0.2
gl_2_2 *= 0.2
geg_2  *= 0.2

gek_t_1 *= 0.5
gek_t_2 *= 0.5


## Berechnung der Fehler/ Mittelwerte
gl_1_1  = ufloat(np.mean(gl_1_1 ), np.std(gl_1_1  ))
gl_2_1  = ufloat(np.mean(gl_2_1 ), np.std(gl_2_1  ))
gl_1    = (gl_1_1 + gl_2_1) / 2
geg_1   = ufloat(np.mean(geg_1  ), np.std(geg_1   ))
gl_1_2  = ufloat(np.mean(gl_1_2 ), np.std(gl_1_2  ))
gl_2_2  = ufloat(np.mean(gl_2_2 ), np.std(gl_2_2  ))
gl_2    = (gl_1_2 + gl_2_2) / 2
geg_2   = ufloat(np.mean(geg_2  ), np.std(geg_2   ))

gek_t_1 = ufloat(np.mean(gek_t_1), np.std(gek_t_1 ))
gek_s_1 = ufloat(np.mean(gek_s_1), np.std(gek_s_1 ))
gek_t_2 = ufloat(np.mean(gek_t_2), np.std(gek_t_2 ))
gek_s_2 = ufloat(np.mean(gek_s_2), np.std(gek_s_2 ))


print("gl_1_1 ",gl_1_1 )
print("gl_2_1 ",gl_2_1 )
print("gl_1 ",gl_1 )
print("geg_1  ",geg_1  )
print("gl_1_2 ",gl_1_2 )
print("gl_2_2 ",gl_2_2 )
print("gl_2 ",gl_2 )
print("geg_2  ",geg_2  )

print("gek_t_1",gek_t_1)
print("gek_s_1",gek_s_1)
print("gek_t_2",gek_t_2)
print("gek_s_2",gek_s_2)

#T_p_1 = 2 * np.pi * np.sqrt(l_1 / g)
#T_p_2 = 2 * np.pi * np.sqrt(l_2 / g)

#print(T_p_1)
#print(T_p_2)


#### Berechnung der Theoretischen Werte 

## Berechnung von K nach der Foreml aus der Gegenphasigen Schwingung
K_1_1 = l_1 * 2 * np.pi ** 2 / (geg_1 ** 2) - g/2
print("K_1_1" , K_1_1)

K_1_2 = l_2 * 2 * np.pi ** 2 / (geg_2 ** 2) - g/2
print("K_1_2" , K_1_2)

## Berechnung von K nach der Formel aus den beiden Schwingingsdauern
K_2_1 = gl_1 ** 2 - geg_1 **2 / (gl_1 ** 2 + geg_1 **2)
print("K_2_1" , K_2_1)

K_2_2 = gl_2 ** 2 - geg_2 **2 / (gl_2 ** 2 + geg_2 **2)
print("K_2_2" , K_2_2)


## Berechnung der Theoretischen Schwebungsdauern aus den beiden Schwingungsdauern
T_s_1 = gl_1  * geg_1  / (gl_1 - geg_1 )
print("T_s_1", T_s_1)

T_s_2 = gl_2  * geg_2  / (gl_2 - geg_2 )
print("T_s_2", T_s_2)

## Berechnung der Theoretischen Frequenzen

w_p_1_1 = np.sqrt(g / l_1)
print("w_p_1_1", w_p_1_1)

w_p_1_2 = np.sqrt(g / l_2)
print("w_p_1_2 " , w_p_1_2)

w_m_1_1 = unp.sqrt(g / l_1 + (2 * K_2_1)/(l_1))
print("w_m_1_1" , w_m_1_1)

w_m_1_2 = unp.sqrt(g / l_2 + (2 * K_2_2)/(l_2))
print("w_m_1_2" , w_m_1_2)

w_s_1_1 = w_p_1_1 - w_m_1_1
print("w_s_1_1" , w_s_1_1)

w_s_1_2 = w_p_1_2 - w_m_1_2
print("w_s_1_2" , w_s_1_2)

## Berechnung der Frequenzen aus den gemessenen Schwingungsdauern

w_p_2_1 = 2 * np.pi / gl_1
print("w_p_2_1" , w_p_2_1)

w_p_2_2 = 2 * np.pi / gl_2
print("w_p_2_2" , w_p_2_2)

w_m_2_1 = 2 * np.pi / geg_1
print("w_m_2_1" , w_m_2_1)

w_m_2_2 = 2 * np.pi / geg_2
print("w_m_2_2" , w_m_2_2)

w_s_2_1 = 2 * np.pi / gek_s_1
print("w_s_2_1" , w_s_2_1)

w_s_2_2 = 2 * np.pi / gek_s_2
print("w_s_2_2" , w_s_2_2)


#### Diskussion