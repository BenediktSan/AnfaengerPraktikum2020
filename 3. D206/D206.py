import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import sympy

        #Daten auslesen
Data=np.genfromtxt("Daten.txt")
t=Data[0:36]
t= t*60
#t in sekunde
#print(t)
T1=Data[36:72]
T1+=273.15
#print(T1)
#Temperatur in K
p1=Data[72:108]
p1+=1
#print(p1)
#Druck in bar
T2=Data[108:144]
T2+=273.15
#print(T2)
#Temperatur in K
p2=Data[144:180]
p2+=1
#print(p2)
#Druck in bar
N=Data[180:216]
#print(N)
#Leistung in Watt

dT=0.1*np.ones(36)
mkck=750
m1=4
c1=4183
m1c1=m1*c1
#print(m1c1)

        #fitten der Daten
def f(x,A,B,C):
    return A*x**2 + B*x + C
def g(x,A,B,C):
    return A/(1+ B*(x**C))

parameter1 , _1 = curve_fit(f,t,T1)
parameter2, _2 =curve_fit(g,t,T2,p0=(240,0.00006,1.2))

uncertainties1 = np.sqrt(np.diag(_1))
uncertainties2 = np.sqrt(np.diag(_2))

for names ,value, unsicherheit in zip("ABC", parameter1,uncertainties1):
    print(f"{names}={value:.8f} +- {unsicherheit:.8f}")
for names ,value, unsicherheit in zip("DEF", parameter2,uncertainties2):
    print(f"{names}={value:.8f} +- {unsicherheit:.8f}")


A=-0.00000322 
B=0.02027984 
C=294.97008058 
D=295.98505139 
E=0.00006346 
F=0.91797063

for names ,value, unsicherheit in zip("HIJ", parameter1,uncertainties1):
    names= ufloat(value,unsicherheit)
    #print(f"HIJ={names:.9f}")
for names ,value, unsicherheit in zip("KLM", parameter2,uncertainties2):
    names= ufloat(value,unsicherheit)
    #print(f"KLM={names:.9f} ")


H= ufloat(-0.00000322 , 0.00000004)
I= ufloat(0.02027984 , 0.00009110)
J= ufloat(294.97008058 , 0.04134538)
K= ufloat(295.98505139 , 0.37244804)
L= ufloat(0.00006346 ,0.00002117)
M= ufloat(0.91797063 ,0.04248507)

print("H = ", H)
print("I = ", I)
print("J = ", J)
print("K = ", K)
print("L = ", L)
print("M = ", M)

        #differenzieren
t_v=sympy.var("t_v")

F2 = A*t_v**2 + B*t_v + C
#F2 = H * t_v**2 + I * t_v + J
G = D / (1 + E * (t_v**F))
#G = K / (1 + L * (t_v**M))
#print("F/dt= ",F2.diff(t_v))
#print("G/dt= ",G.diff(t_v))


        #Test
a_v, b_v , c_v, d_v , e_v , f_v =sympy.var("a_v b_v c_v d_v e_v f_v")

T1test= a_v *t_v**2 + b_v *t_v + c_v

T2test= d_v / (1 + e_v * (t_v**f_v))

#print(T1test.diff(t_v))
#print(T2test.diff(t_v))


def Fdt(t):
    F1=T1test.diff(t_v)
    Fdt_value = F1.evalf(subs={t_v:t,a_v:H.n, b_v:I.n , c_v:J.n })
    Fdt_error = F1.evalf(subs={t_v:t,a_v:H.n, b_v:I.n , c_v:J.n })-F1.evalf(subs={t_v:t,a_v:H.n+H.s, b_v:I.n+I.s , c_v:J.n+J.s})
    
    return ufloat(Fdt_value, -Fdt_error)

def Gdt(t):
    G1=T2test.diff(t_v)
    Gdt_value = G1.evalf(subs={t_v:t,d_v:K.n, e_v:L.n , f_v:M.n })
    Gdt_error = G1.evalf(subs={t_v:t,d_v:K.n, e_v:L.n , f_v:M.n })-G1.evalf(subs={t_v:t,d_v:K.n+K.s, e_v:L.n+L.s , f_v:M.n+M.s})

    return ufloat(Gdt_value, Gdt_error)

for i in range(1,5):
    print(f"Fdt({7*i})={Fdt(t[7*i+1]):.4f}", f"  Gdt({7*i})={Gdt(t[7*i+1]):.4f}")


        #Güteziffer


def v_ideal_error(T1,T2,dT1,dT2):
    return np.sqrt(((-T2/((T1-T2)**2))*dT1)**2+(T1/(((T1-T2)**2))*dT2)**2)       
for i in range(1,5):
    print(f"v_real({7*i})={((mkck+m1c1)*Fdt(7*i))/(N[(7*i)+1]):.4f} v_ideal({7*i})={ufloat(T1[(7*i)+1]/(T1[(7*i)+1]-T2[(7*i)+1]),v_ideal_error(T1[7*i+1],T2[7*i+1],0.1,0.1))}")
 
        



for i in range(1,5):
    print(f"v_ideal_error in Minute {7*i} ist: {v_ideal_error(T1[7*i+1],T2[7*i+1],0.1,0.1):.5f}")


        #Verdampfungswärme L[Joule/mol] R[Joule/mol*K]


P1=np.log(p1)
parameter3, _3 = np.polyfit(1/T1,P1, deg=1, cov=True)
#L1=-1*parameter3[0]*8.314
#print("Parameter3=",parameter3)
#print(f"L1={L1:.4f}")

P2=np.log(p2)
parameter4, _4 = np.polyfit(1/T2,P2, deg=1, cov=True)
L2_v=-1*parameter4[0]*8.314

#print("Parameter4=",parameter4)


uncertainties4 = np.sqrt(np.diag(_4))
L2_e=-1*uncertainties4[0]*8.314
L2 = ufloat(L2_v, -1*L2_e)
print(f"L2={L2:.4f}")

print("Fehler a =", uncertainties4)
#L2_f= ufloat(-1*parameter4[0]*8.314,1*uncertainties4[0]*8.314 )


        #Massendurchsatz
def mdt(i):
    mdtn=((mkck+m1c1)*Gdt(t[7*i+1]).n)/L2.n
    mdts=(((mkck+m1c1)*Gdt(t[7*i+1]).n)/(L2.n-L2.s))-(((mkck+m1c1)*Gdt(t[7*i+1]).n)/L2.n)
    return ufloat(mdtn,-1*mdts)

for i in range(1,5):
    print(f"Massendurchsatz in minute({7*i})={mdt(i):.5f}")

        #mechanische Leistung
def N_mech(k,pa,pb,roh,mdt):
    return (1/(k-1))*(pb*((pa/pb)**(1/k))-pa)*(1/roh)*mdt

for i in range(1,5):
    print(f"Die mechanische Leistung in Minute {7*i} beträgt:{N_mech(1.14, p2[7*i +1], p1[7*i +1], 5.51, mdt(i)):.4f}")

        #Gründe für schlechte Güteziffer
print("In der Realität ist es leider nicht möglich die ideale Güteziffer für eine Wärmepumpe zu erreichen, da es bei dem gesamtem Prozess viele Wege gibt um Energie zu \"verlieren\"."
"Zum einen entstehen bei den ganzen mechanischen Bauteilen der Pumpe durch Reibung Energieverluste und gerade beim Transport der Kühlflüssigkeit wird auch eine Menge Energie an die Umwelt abgegeben. "
"Das sind beides Energieverluste die man auch mit großen Aufwand, realistisch nicht entfernen kann.")
  

        #Plotten
x = np.linspace(0,2100,50)
x2=np.linspace(0.0031,0.0034,50)
x3=np.linspace(0.00339,0.00363,50)

plt.figure()
plt.plot(t,T1,"k.",label="T1")
plt.plot(t,T2,".",label="T2") 
plt.plot(x,f(x, *parameter1),label="Fit zu T1")
plt.plot(x,g(x, *parameter2),label="Fit zu T2")     
plt.xlabel("Zeit [s]")
plt.ylabel("Temperatur [K]")
plt.legend()
plt.tight_layout()
plt.savefig("build/plot1.pdf")


plt.figure()
plt.plot(1/T1,P1,".",label="Werte von T1")
plt.plot(x2, parameter3[0]*x2 + parameter3[1], label="Regression zu 1")
plt.plot(1/T2,P2,".",label="Werte von T2")
plt.plot(x3, parameter4[0]*x3 + parameter4[1], label="Regression zu 2")
plt.xlabel("1/T [1/K]")
plt.ylabel("log(p/p0)")
plt.tight_layout()
plt.legend()
plt.savefig("build/plot2.pdf")

#plt.show()