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



###werte einlesen

#tamp = np.load('python/variables/tamp.npy')
#Uamp = np.load('python/variables/Uamp.npy')

refl1=np.array([0,20,30,40,50,60,70]) #in grad
refl2=np.array([0,20,30,40,51,61,70])




brech1=np.array([10,20,30,40,50,60,70]) #in grad
brech2=np.array([7,14,20,26,31,36,39.5])




green1=np.array([30,35,40,50,60]) 
green2=np.array([76.5,66.5,58.5,47,38]) 
red2=np.array([75,75.5,57.8,46,37.5]) 



max1=np.array([-23.5,0,23.5]) 
max2=np.array([-35,-22.5,-11,0,11,22.5,35]) 
max3=np.array([-32,-27.2,-23,-19,-15,-11.3,-7.5,-4,0,3.8,7.2,11,15,19,23,27.2,32]) 



###Konstanten

err=0.5
d=5.85e-3 #meter
gam=60*const.pi/180.0 #rad
lamg=532e-9 #meter
lamr=6.35e-7 #meter

#pip install tabulate
###Brechungsindices

nluft=1.000292          #https://www.chemie.de/lexikon/Brechzahl.html
nwasser=1.33
nkron=1.46 #bis 1.65
nplexi=1.49
ndia=2.42



###Reflexion
def lin(x,a,b):
    return (a*x+b)

params1, _1 =curve_fit(lin,refl1,refl2,p0=(1,0))
err =np.sqrt(np.diag(_1))
uparams=unp.uarray(params1,err)

print(f'\nA= {uparams[0]:.4f}  \nB= {uparams[1]:.4f} \n')
print("rel abw: ",(1-uparams[0])*100)
###Brechung


#n=unp.sin(ubrech1*const.pi/180.0)/unp.sin(ubrech2*const.pi/180.0)
n=unp.sin(brech1*const.pi/180.0)/unp.sin(brech2*const.pi/180.0)



un=unp.uarray(n.mean(),np.std(n, ddof=1) / np.sqrt(len(n)))
cplexi=const.c/nplexi
print(f'\nPlexi:= {un:.4f}  \nc= {const.c/un:.4f}\nctheo= {cplexi:.4f} \nrelative Abweichung: {((cplexi-(const.c/un))/cplexi)*100}%\n')



###Platten

def f1(d,platt1, platt2):
    return(d*unp.sin((platt1-platt2)*const.pi/180.0)/unp.cos(platt2*const.pi/180.0)) 

#versatz1=(d*unp.sin((brech1-brech2)*const.pi/180.0)/unp.cos(brech2*const.pi/180.0))
versatz1=f1(d,brech1,brech2)
beta_=unp.arcsin(unp.sin(brech1*const.pi/180.0)/unp.nominal_values(un))
print("beta ",beta_)
versatz2=f1(d,brech1,beta_)

ver1=unp.uarray(versatz1.mean(),np.std(versatz1, ddof=1) / np.sqrt(len(versatz1)))
ver2=unp.uarray((unp.nominal_values(versatz2)).mean(),np.std(unp.nominal_values(versatz2), ddof=1) / np.sqrt(len(versatz1))) ###funk geht wieder nicht
print(f'\nversatz1:= {ver1}  \nversatz2= {ver2} \nrelative Abweichung: {unp.nominal_values(((ver1-ver2)/ver1)*100)} {unp.std_devs(((ver1-ver2)/ver1)*100)}%')

table ={'beta1': brech2*(const.pi/180), 'versatz': versatz1, 'beta': beta_, 'zweiter versatz': versatz2}
print("\n ",tabulate (table, tablefmt="latex"))


###Prisma

def delta(a,b):
    return (a*const.pi/180.0+b*const.pi/180.0)-(np.arcsin(np.sin(a*const.pi/180.0)/nkron)-(gam -np.arcsin(np.sin(a*const.pi/180.0)/nkron)))
    
    
    
    
delg=unp.uarray((delta(green1,green2)).mean(),np.std(delta(green1,green2), ddof=1) / np.sqrt(len(delta(green1,green2))))
delr=unp.uarray((delta(green1,red2)).mean(),np.std(delta(green1,red2), ddof=1) / np.sqrt(len(delta(green1,red2))))
print(f'\ndeltagrün:= {delg}  \ndeltarot= {delr}')

print("\ndeltagrün\tdeltarot ")
table ={ 'delg':delta(green1,green2), 'delr':delta(green1,red2)}
print("\n ",tabulate (table, tablefmt="latex"))

###gitter
g1=1/600e3
g2=1/300e3
g3=1/100e3

tst=np.array([10,15,3])

def neu(a):
    b=np.zeros(int((len(a))/2))
    for i in range(int((len(a)-1)/2)):
        b[i]=(-a[i]+a[-(i+1)])/2
    return b

max1neu=neu(max1)
print("\nmax1neu: ",max1neu)
max2neu=neu(max2)
print("\nmax2neu: ",max2neu)
max3neu=neu(max3)
print("\nmax3neu: ",max3neu)

def lam(a,g):
    b=np.zeros(len(a))
    for i in range(len(a)):
        b[i-1]=g*((np.sin(a[-(i)]*const.pi/180.0))/(i+1))
    return b

lam1=lam(max1neu,g1)
lam2=lam(max2neu,g2)
lam3=lam(max3neu,g3)

lam1_=unp.uarray(lam1.mean(),0)
lam2_=unp.uarray(lam2.mean(),np.std(lam2, ddof=1) / np.sqrt(len(lam2)))
lam3_=unp.uarray(lam3.mean(),np.std(lam3, ddof=1) / np.sqrt(len(lam3)))
print(lam2)
print("\nTheo: ",lamr)
print(f'lamda1:= {lam1_}  \nrelative Abweichung: {((lamr-lam1_)/lamr)*100}%')
print(f'lamda2:= {unp.nominal_values(lam2_)} {unp.std_devs(lam2_)}  \nrelative Abweichung: {unp.nominal_values(((lamr-lam2_)/lamr)*100)} {unp.std_devs(((lamr-lam2_)/lamr)*100)}%')
print(f'lamda3:= {unp.nominal_values(lam3_)} {unp.std_devs(lam3_)}  \nrelative Abweichung: {unp.nominal_values(((lamr-lam3_)/lamr)*100)} {unp.std_devs(((lamr-lam3_)/lamr)*100)}%')

table ={'a': lam1, 'b': lam2,  'c': lam3}
print("\n ",tabulate (table, tablefmt="latex"))



###PLOTS
x1=np.linspace(0,75,100)

plt.figure()
plt.plot(x1, x1*params1[0]+params1[1],label= "fit")
plt.plot(refl2,refl2,".", label="Messwerte")
plt.xlabel(r'$\alpha_1$ in Grad')
plt.ylabel(r'$\alpha_2$ in Grad')
plt.legend()
plt.tight_layout()
plt.savefig("build/plots/plot1.pdf")


plt.figure()
plt.plot(green1*const.pi/180, delta(green1,green2), "g.", label="Ablenkung des grünen Lasers")
plt.plot(green1*const.pi/180,delta(green1,red2), 'r.', label="Ablenkung des roten Lasers")
plt.xlabel(r"$\alpha$ [rad]")
plt.ylabel(r"$\delta$ [rad]")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plots/plot2.pdf')






np.savetxt(
    'build/brechung.txt',
    np.column_stack([brech1, brech2,n]),
    fmt=['%.3f', '%.3f','%.3f'],       
    delimiter=' & ',
    header='einf,ausf,n',
)