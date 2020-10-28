import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import sympy

        #Daten auslesen
Data=np.genfromtxt("Daten.txt")
t=Data[0:36]
t= t*60
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
    return A/(1+ B*(x**C))

parameter1, _ =curve_fit(f,t,T1)
parameter2, _ =curve_fit(g,t,T2,p0=(12,0.00006,1.2))
for names ,value in zip("ABC", parameter1):
    print(f"{names}={value:.8f}")
for names , value in zip("DEF", parameter2):
    print(f"{names}={value:.8f}")

A=-0.00000322
B=0.02027984
C=21.82008061
D=21.58061064
E=0.00000095
F=1.97775836
        #differenzieren
t_v=sympy.var("t_v")

F2=A*t_v**2+B*t_v+C
G=D/(1+E*(t_v**F))

#print("F/dt= ",F.diff(t_v))
#print("G/dt= ",G.diff(t_v))
def Fdt(t):
    F1=F2.diff(t_v)
    return F1.evalf(subs={t_v:t}) 

def Gdt(t):
    G1=G.diff(t_v)
    return G1.evalf(subs={t_v:t}) 

for i in range(1,5):
    print(f"Fdt({7*i})=",Fdt(7*i))
    print(f"Gdt({7*i})=",Gdt(7*i))


        #Güteziffer
for i in range(1,5):
    print("vreal(",7*i,")=",((mkck+m1c1)*Fdt(7*i))/(N[(7*i)-1]),
     "videal(",7*i,")=",T1[(7*i)-1]/(T1[(7*i)-1]-T2[(7*i)-1]))
    print(N[7*i-1])

        #Plotten
x= np.linspace(0,2100,50)
plt.plot(t,T1,"k.",label="T1")
plt.plot(t,T2,".",label="T2") 
plt.plot(x,f(x, *parameter1),label="Fit zu T1")
plt.plot(x,g(x, *parameter2),label="Fit zu T2")     

plt.legend()
plt.savefig("build/plot.pdf")
#plt.show()