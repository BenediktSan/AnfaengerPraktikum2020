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

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")

lamtheo=635 *10**(-9)   #meter
uebersetzung=5.056

mess1=np.array([2957,2950,2966,2943,2634,2936,2964,2961])

s1=np.ones(np.size(mess1))
s1*=5*10**(-3)
s1[3]+=0.05*10**(-3)




V=5*10**(-3)          #kubikmeter

up=np.array([50,20,39,30,26])
down=np.array([32,31,31,30,30 ])


#####Wellenlängen#######
print("Wellenlängen: \n")

us1=unp.uarray(s1,0.002*10**(-3))
d=us1/uebersetzung

umess1=unp.uarray(mess1,40)



lam= 2*d/umess1
print("Lambda in nano meter:")
for i in range(0, np.size(lam)):
    print(f"{unp.nominal_values(d[i]):.5f} &{mess1[i]}& {unp.nominal_values(lam[i]) *10**9:.3f} & {unp.std_devs(lam[i]) *10**9:.3f} \\\\")

print(f"{unp.std_devs(d[1])*10**6:.5f}")
print(unp.std_devs(umess1[1]))


umean= unp.uarray(np.mean(unp.nominal_values(lam)),np.std(unp.nominal_values(lam)))

print(f'\nmean: {np.mean(unp.nominal_values(lam))*10**9:.3f} +- {np.std(unp.nominal_values(lam))*10**9:.3f}')
print(f'Theo: {lamtheo*10**9:.4}\nrel abw:{((lamtheo-umean)/lamtheo)*100 }')



########next#######

print("\n\n###########next##########")
for i in range(0, np.size(down)):
    print(f"{down[i]} &{up[i]} \\\\")


T_0 = 273.15
T = T_0 + 21
p_0=101320
dp=600/0.0075006157584566

b = 0.05

data =np.array([50,20,39,30,26,32,31,31,30,30 ])
udata=unp.uarray(np.mean(data),np.std(data))
print(f'udata: {udata}\n')

deln=(udata*lamtheo)/(2*b)


n=1+deln*(T/T_0)*(p_0/(dp))










print(f'deln = {deln} ')
#dn_lit = .00027316
#print(f'delntheo = {dn_lit} ')
#print(f'relativer Felhger = {(deln - dn_lit) / dn_lit}\n')





print(f"Brechungsindex: {n}")
n_lit = 1.00027316
print(f'Relativer Fehler: {((n_lit-n)/n_lit)*100}')