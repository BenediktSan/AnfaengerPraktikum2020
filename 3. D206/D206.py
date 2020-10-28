import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import sympy

        #Daten auslesen
Data=np.genfromtxt("Daten.txt")
t=Data[0:36]
#print(t)
T1=Data[36:72]
#print(T1)
p1=Data[72:108]
#print(p1)
T2=Data[108:144]
#print(T2)
p2=Data[144:180]
#print(p2)
N=Data[180:216]
#print(N)

mkck=750
m1=4
c1=4.184
m1c1=m1*c1
#print(m1c1)

        #fitten der Daten
def f(x,A,B,C):
    return A*x**2 + B*x + C
def g(x,A,B,C):
    return A/(1+ B*x**C)

parameter1, _ =curve_fit(f,t,T1)
parameter2, _ =curve_fit(g,t,T2,p0=(15,0.001,1.6))
for names ,value in zip("ABC", parameter1):
    print(f"{names}={value:.3f}")
for names , value in zip("DEF", parameter2):
    print(f"{names}={value:.3f}")

        #differenzieren
t_v=sympy.var("t_v")

#F=A*t_v**2+B*t_v+C
#G=A/(1+B*t_v**C)

#print(F.diff(t_v))
#print(G.diff(t_v))

        #Plotten
x= np.linspace(0,37,50)
plt.plot(t,T1,"k.",label="T1")
plt.plot(t,T2,".",label="T2") 
plt.plot(x,f(x, *parameter1),label="Fit zu T1")
plt.plot(x,g(x, *parameter2),label="Fit zu T2")     

plt.legend()
plt.savefig("plot.pdf")
#plt.show()