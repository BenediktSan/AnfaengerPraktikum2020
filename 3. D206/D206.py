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
p1+=1
#print(p1)
T2=Data[108:144]
print(T2)
p2=Data[144:180]
p2+=1
print(p2)
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

        #Verdampfungswärme

p0=p1[0]
P1=np.log(p1/p0)
parameter3, _ = np.polyfit(1/T1,P1, deg=1, cov=True)
L1=-1*parameter3[0]*8.314
print("L1=",L1)

P2=np.log(p2/p0)
parameter4, _ = np.polyfit(1/T2[5:30],P2[5:30], deg=1, cov=True)
L2=-1*parameter4[0]*8.314
print("L2=",L2)

        #Massendurchsatz
mdt=((mkck+m1c1)*Fdt(7*i))/L1
print("Massendurchsatz= ",mdt)

        #mechanische Leistung
def N_mech(k,pa,pb,roh,mdt):
    return 1/(k-1)*(pb*np.sqrt(pa/pb)-pa)*(1/roh)*mdt

for i in range(1,5):
    print(f"Die mechanische Leistung zu Minute{7*i} beträgt:{N_mech(1.14, p2[7*i -1], p1[7*i -1], 5.51, 10)}")
        #Plotten
x= np.linspace(0,2100,50)
x2=np.linspace(0.02,0.05,50)
x3=np.linspace(0.05,0.35,50)
plt.subplot(2,1,1)
plt.plot(t,T1,"k.",label="T1")
plt.plot(t,T2,".",label="T2") 
plt.plot(x,f(x, *parameter1),label="Fit zu T1")
plt.plot(x,g(x, *parameter2),label="Fit zu T2")     

#plt.legend()
#plt.savefig("build/plot.pdf")
plt.subplot(2,1,2)
plt.plot(1/T1,P1,".",label="Daten1")
plt.plot(x2,parameter3[0]*x2+parameter3[1],label="regression1")
plt.plot(1/T2[5:30],P2[5:30],".",label="Daten2")
plt.plot(x3,parameter4[0]*x2+parameter4[1],label="regression2")
plt.legend()
plt.savefig("build/plot.pdf")

#plt.show()