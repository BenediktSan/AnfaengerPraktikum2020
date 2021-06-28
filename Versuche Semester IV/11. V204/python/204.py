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
from scipy.signal import find_peaks

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


#       Daten
n_1 , T1_1 , T2_1 , T3_1 , T4_1 , T5_1 , T6_1 , T7_1 , T8_1 = np.genfromtxt("python/Daten/GLXportRun1.txt", unpack =True)

print("Temperaturen bei t = 700s")
print('T1_1 at 700s:', T1_1[3487])
print('T4_1 at 700s:', T4_1[3487])
print('T5_1 at 700s:', T5_1[3487])
print('T8_1 at 700s:', T8_1[3487])
print(len(n_1))

#Messing breit
A = 0.012 *0.004 
k = 120 #watt pro meter kelvin
#print(" \n Messing breit")
dQ_100 = -A*k*((T1_1[20*25]-T2_1[20*25])/0.03)
dQ_200 = -A*k*((T1_1[40*25]-T2_1[40*25])/0.03)
dQ_350 = -A*k*((T1_1[70*25]-T2_1[70*25])/0.03)
dQ_450 = -A*k*((T1_1[90*25]-T2_1[90*25])/0.03)
dQ_600 = -A*k*((T1_1[120*25]-T2_1[120*25])/0.03)
#print('dQ:', dQ_100, dQ_200, dQ_350, dQ_450, dQ_600)

#messing schmal
#print("\n Messing schmal")
A = 0.007 *0.004 
k = 120 #watt pro meter kelvin
dQ_100 = A*k*((T3_1[20*25]-T4_1[20*25])/0.03)
dQ_200 = A*k*((T3_1[40*25]-T4_1[40*25])/0.03)
dQ_350 = A*k*((T3_1[70*25]-T4_1[70*25])/0.03)
dQ_450 = A*k*((T3_1[90*25]-T4_1[90*25])/0.03)
dQ_600 = A*k*((T3_1[120*25]-T4_1[120*25])/0.03)
#print('dQ:', dQ_100, dQ_200, dQ_350, dQ_450, dQ_600)

#aluminium
#print("\n Aluminium")
A = 0.012 *0.004 
k = 237 #watt pro meter kelvin
dQ_100 = -A*k*((T5_1[20*25]-T6_1[20*25])/0.03)
dQ_200 = -A*k*((T5_1[40*25]-T6_1[40*25])/0.03)
dQ_350 = -A*k*((T5_1[70*25]-T6_1[70*25])/0.03)
dQ_450 = -A*k*((T5_1[90*25]-T6_1[90*25])/0.03)
dQ_600 = -A*k*((T5_1[120*25]-T6_1[120*25])/0.03)
#print('dQ:', dQ_100, dQ_200, dQ_350, dQ_450, dQ_600)

#edelstahl
#print("\n Edelstahl")
A = 0.012 *0.004 
k = 15 #watt pro milli kelvin
dQ_100 = A*k*((T7_1[20*25]-T8_1[20*25])/0.03)
dQ_200 = A*k*((T7_1[40*25]-T8_1[40*25])/0.03)
dQ_350 = A*k*((T7_1[70*25]-T8_1[70*25])/0.03)
dQ_450 = A*k*((T7_1[90*25]-T8_1[90*25])/0.03)
dQ_600 = A*k*((T7_1[120*25]-T8_1[120*25])/0.03)
#print('dQ:', dQ_100, dQ_200, dQ_350, dQ_450, dQ_600)
#       Konstanten 



#Querschnittsfächen)
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

## Plotten



t1 = np.linspace(1, len(T1_1)/5/60 , len(T1_1))
plt.figure()
plt.plot(t1, T1_1, 'b', label='Messing (breit) - T1')
plt.plot(t1, T4_1, 'r', label='Messing (schmal) - T4')
plt.plot(t1, T5_1, 'k', label='Aluminium - T5')
plt.plot(t1, T8_1, 'g', label='Edelstahl - T8')
plt.xlabel(r'$t \quad  / \quad  min $')
plt.ylabel(r'$T \quad  / \quad ° $')
plt.legend()
plt.tight_layout()
plt.savefig('build/plots/stat_plot.pdf')

plt.figure()
DT78 = T7_1-T8_1
DT21 = T2_1-T1_1
plt.plot(t1, DT78, 'k', label='Temperaturdifferenz Edelstahl')
plt.plot(t1, DT21, 'r', label='Temperaturdifferenz Messing (breit)')

plt.xlabel(r'$t \quad  / \quad  min $')
plt.ylabel(r'$T \quad  / \quad ° $')

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/plots/plot_diff.pdf')

##################### Dynamische Methode 


n_2 , T1_2 , T2_2 , T3_2 , T4_2 , T5_2 , T6_2 , T7_2 , T8_2 = np.genfromtxt("python/Daten/GLXportRun2.txt", unpack =True)
###namen = ["T1_2" , "T2_2" , "T3_2" , "T4_2" , "T5_2" , "T6_2" , "T7_2" , "T8_2"]

t2 = np.linspace(1, len(T1_2)/2 / 60 , len(T1_2))

plt.figure()
plt.plot(t2, T1_2, 'k', label=r'$T_{fern}$')
plt.plot(t2, T2_2, 'r', label=r'$T_{nah}}$')
plt.xlabel(r'$t \quad  / \quad  min $')
plt.ylabel(r'$T \quad  / \quad ° $')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/plots/plot_messing.pdf')

plt.figure()
plt.plot(t2, T5_2, 'k', label=r'$T_{fern}$')
plt.plot(t2, T6_2, 'r',label=r'$T_{nah}$')
plt.xlabel(r'$t \quad  / \quad  min $')
plt.ylabel(r'$T \quad  / \quad ° $')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/plots/plot_aluminium.pdf')

##dynamische methode
#messing
A_fern = np.array([35.45-24.52, 42.91-34.90, 48.28-41.51, 52.66-46.23, 56.24-50.86, 58.82-53.53, 61.08-55.97, 62.97-58.05, 64.75-59.90, 66.17-61.52])
A_nah = np.array([45.62-25.81, 52.36-36.29, 57.26-42.09, 60.84-46.26, 64.68-51.13, 67.22-53.24, 69.45-55.69, 71.25-57.70, 73.00-59.54, 74.45-61.18])
#print('A_fern ', A_fern)
#print('A_nah ', A_nah)
D = np.log(A_nah/A_fern)
print('ln() für Messing', D)
print( np.mean(D), np.std(D)/10)

dt = np.array([22, 16, 16, 20, 14, 12, 12, 12, 12, 12])
print('dt', np.mean(dt), np.std(dt)/10)


# Aluminium 

A_fern = np.array([41.68-24.77, 50.07-38.58, 55.14-45.13, 58.88-49.29, 62.47-54.05, 64.67-56.01, 66.76-58.25, 68.43-60.15, 70.08-61.85, 71.43-63.35])
A_nah = np.array([49.70-25.74, 57.34-38.15, 62.06-44.10, 65.34-48.07, 69.11-52.86, 71.33-54.62, 73.35-56.92, 75.11-58.88, 76.79-60.57, 78.07-62.06])
print('A_fern ', A_fern)
print('A_nah ', A_nah)
D = np.log(A_nah/A_fern)
print('ln() für Aluminium', D)
print( np.mean(D), np.std(D)/10)

dt = np.array([12, 8, 8, 14, 6, 8, 6, 6, 6, 8])
print('dt', np.mean(dt), np.std(dt)/10)

k = (2800*830*(0.03**2))/(2*dt*D)
#print('k', k)
#print('k=', np.mean(k), np.std(k)/10)

lam = 2*np.pi / np.sqrt((2*np.pi*dt*D)/(80* 0.03**2))
#print('lambda = ', np.mean(lam), '+- ', np.std(lam)/10)



n_3 , T1_3 , T2_3 , T3_3 , T4_3 , T5_3 , T6_3 , T7_3 , T8_3 = np.genfromtxt("python/Daten/GLXportRun3.txt", unpack =True)
t3 = np.linspace(1, len(T1_3)/2 / 60 , len(T1_3))
p7 = find_peaks(T7_3,distance=200)
print(p7)
np7 = find_peaks(-T7_3,distance=200)
p8 = find_peaks(T8_3,distance=200)
print(p8)
np8 = find_peaks(-T8_3,distance=200)

print("Edelstahl : \n \n")
print(T7_3[p7[0]] )
print(T7_3[np7[0]])
print(T8_3[p8[0]] )
print(T8_3[np8[0]])
plt.figure()
plt.plot(t3, T8_3  , 'k', label=r'$T_{fern}$')
plt.plot(t3, T7_3  , 'r',label=r'$T_{nah}$')
plt.xlabel(r'$t \quad  / \quad  min $')
plt.ylabel(r'$T \quad  / \quad ° $')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig('build/plots/plot_edelstahl.pdf')

A_fern = np.array([40.91-35.25 ,  44.09-39.99 , 48.4-43.42 , 52.06-47.59 , 54.87-50.94 , 57.01-53.49])
A_nah = np.array([62.46-38.66 , 65.31-45.06 , 70.17-48.62 , 74.04-53.22 , 76.75-56.07 , 78.88-59.07])
print('A_fern ', A_fern)
print('A_nah ', A_nah)
D = np.log(A_nah/A_fern)
print('ln() für Edelstahl', D)
print( np.mean(D), np.std(D)/6)

dt = np.array([(331-216)/2 , (738-616)/2 , (1141-1017)/2 , (1533-1417)/2 , (1926-1816)/2 , (2320-2216)/2])
print('dt', dt)
print('dt', np.mean(dt), np.std(dt)/6)

k = (8000*400*(0.03**2))/(2*dt*D)
print('k', k)
print('k=', np.mean(k), np.std(k)/6)

lam = 2*np.pi / np.sqrt((2*np.pi*dt*D)/(80* 0.03**2))
print('lambda = ', np.mean(lam), '+- ', np.std(lam)/6)



####Testen der Daten
###
####Plotten
###
###n_1 , T1_1 , T2_1 , T3_1 , T4_1 , T5_1 , T6_1 , T7_1 , T8_1 = np.genfromtxt("python/Daten/GLXportRun1.txt", unpack =True)
###
###Temperaturen = [T1_1 , T2_1 , T3_1 , T4_1 , T5_1 , T6_1 , T7_1 , T8_1 , T7_1 - T8_1 , T2_1 - T1_1]
###namen = ["T1_1" , "T2_1" , "T3_1" , "T4_1" , "T5_1" , "T6_1" , "T7_1" , "T8_1" , "T7_1 - T8_1" , "T2_1 - T1_1"]
####x = np.linspace(1, len(T1_1)*5 , len(T1_1))
###
###print(len(n_1))
###for  Daten , namen in zip( Temperaturen, namen):
###
###    x = np.linspace(1, len(T1_1)/5/60 , len(T1_1))
###    plt.figure()
###    plt.plot(x, Daten, label= namen)
###    plt.xlabel("Zeit / min")
###    plt.ylabel("Temperatur / °")
###    plt.legend()
###    plt.savefig("build/plots/1/" + namen + ".pdf")
###
###
###n_2 , T1_2 , T2_2 , T3_2 , T4_2 , T5_2 , T6_2 , T7_2 , T8_2 = np.genfromtxt("python/Daten/GLXportRun2.txt", unpack =True)
###Temperaturen = [T1_2 , T2_2 , T3_2 , T4_2 , T5_2 , T6_2 , T7_2 , T8_2]
###namen = ["T1_2" , "T2_2" , "T3_2" , "T4_2" , "T5_2" , "T6_2" , "T7_2" , "T8_2"]
####x = np.linspace(1, len(T1_2)*5 , len(T1_2))
###
###for  Daten , namen in zip( Temperaturen, namen):
###
###    x = np.linspace(1, len(T1_2)/2 / 60 , len(T1_2))
###    plt.figure()
###    plt.plot(x, Daten, label= namen)
###    plt.xlabel("Zeit / min")
###    plt.ylabel("Temperatur / °")
###    plt.legend()
###    plt.savefig("build/plots/2/" + namen + ".pdf")
###
###
###
###
###n_3 , T1_3 , T2_3 , T3_3 , T4_3 , T5_3 , T6_3 , T7_3 , T8_3 = np.genfromtxt("python/Daten/GLXportRun3.txt", unpack =True)
###Temperaturen = [T1_3 , T2_3 , T3_3 , T4_3 , T5_3 , T6_3 , T7_3 , T8_3]
###namen = ["T1_3" , "T2_3" , "T3_3" , "T4_3" , "T5_3" , "T6_3" , "T7_3" , "T8_3"]
####x = np.linspace(1, len(T1_3)*5 , len(T1_3))
###
###for  Daten , namen in zip( Temperaturen, namen):
###
###    x = np.linspace(1, len(T1_3)/2 / 60 , len(T1_3))
###    plt.figure()
###    plt.plot(x, Daten, label= namen)
###    plt.xlabel("Zeit / min")
###    plt.ylabel("Temperatur / °")
###    plt.legend()
###    plt.savefig("build/plots/3/" + namen + ".pdf")



