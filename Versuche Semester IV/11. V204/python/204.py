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

if os.path.exists("build/plots/1") == False:
    os.mkdir("build/plots/1")

if os.path.exists("build/plots/2") == False:
    os.mkdir("build/plots/2")

if os.path.exists("build/plots/3") == False:
    os.mkdir("build/plots/3")

#       Konstanten 

#Querschnittsfächen
A_b = 1.2e-2 * 0.4e-2
A_s = 0.7e-2 * 0.4e-2
#Dichten
r_m = 8520
r_a = 2900
r_e = 8000
#irgendwas mit c
c_m = 385
c_a = 830
c_e = 400
#Wärmeleitfähigkeit
k_m = 120
k_a = 237
k_e = 18

# Funktionen


def dQdt(D , p1 , p2 , A , k ):

    diff = D[p2] - D[p1] / ( 0.03 ) 

    return - k * A * diff


#Plotten

n_1 , T1_1 , T2_1 , T3_1 , T4_1 , T5_1 , T6_1 , T7_1 , T8_1 = np.genfromtxt("python/Daten/GLXportRun1.txt", unpack =True)

Temperaturen = [T1_1 , T2_1 , T3_1 , T4_1 , T5_1 , T6_1 , T7_1 , T8_1 , T7_1 - T8_1 , T2_1 - T1_1]
namen = ["T1_1" , "T2_1" , "T3_1" , "T4_1" , "T5_1" , "T6_1" , "T7_1" , "T8_1" , "T7_1 - T8_1" , "T2_1 - T1_1"]
#x = np.linspace(1, len(T1_1)*5 , len(T1_1))

print(len(n_1))
for  Daten , namen in zip( Temperaturen, namen):

    x = np.linspace(1, len(T1_1)/5/60 , len(T1_1))
    plt.figure()
    plt.plot(x, Daten, label= namen)
    plt.xlabel("Zeit / min")
    plt.ylabel("Temperatur / °")
    plt.legend()
    plt.savefig("build/plots/1/" + namen + ".pdf")


n_2 , T1_2 , T2_2 , T3_2 , T4_2 , T5_2 , T6_2 , T7_2 , T8_2 = np.genfromtxt("python/Daten/GLXportRun2.txt", unpack =True)
Temperaturen = [T1_2 , T2_2 , T3_2 , T4_2 , T5_2 , T6_2 , T7_2 , T8_2]
namen = ["T1_2" , "T2_2" , "T3_2" , "T4_2" , "T5_2" , "T6_2" , "T7_2" , "T8_2"]
#x = np.linspace(1, len(T1_2)*5 , len(T1_2))

for  Daten , namen in zip( Temperaturen, namen):

    x = np.linspace(1, len(T1_2)/2 / 60 , len(T1_2))
    plt.figure()
    plt.plot(x, Daten, label= namen)
    plt.xlabel("Zeit / min")
    plt.ylabel("Temperatur / °")
    plt.legend()
    plt.savefig("build/plots/2/" + namen + ".pdf")




n_3 , T1_3 , T2_3 , T3_3 , T4_3 , T5_3 , T6_3 , T7_3 , T8_3 = np.genfromtxt("python/Daten/GLXportRun3.txt", unpack =True)
Temperaturen = [T1_3 , T2_3 , T3_3 , T4_3 , T5_3 , T6_3 , T7_3 , T8_3]
namen = ["T1_3" , "T2_3" , "T3_3" , "T4_3" , "T5_3" , "T6_3" , "T7_3" , "T8_3"]
#x = np.linspace(1, len(T1_3)*5 , len(T1_3))

for  Daten , namen in zip( Temperaturen, namen):

    x = np.linspace(1, len(T1_3)/2 / 60 , len(T1_3))
    plt.figure()
    plt.plot(x, Daten, label= namen)
    plt.xlabel("Zeit / min")
    plt.ylabel("Temperatur / °")
    plt.legend()
    plt.savefig("build/plots/3/" + namen + ".pdf")



