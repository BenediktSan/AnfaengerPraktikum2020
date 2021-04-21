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
red2=green2=np.array([75,75.5,57.8,46,37.5]) 



max1=np.array([-23.5,0,23.5]) 
max2=np.array([-35,-22.5,-11,0,35,22.5,11]) 
max3=np.array([-32,-27.2,-23,-19,-15,-11.3,-7.5,-4,0,3.8,7.2,11,15,19,23,27.2,32]) 



###Konstanten

err=0.5
d=5.85e-3 #meter
gam=60*const.pi/180.0 #rad
lamg=532*10-9 #meter
lamr=635*10-9 #meter

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


###Brechung
ubrech1=unp.uarray(brech1,0.5)
ubrech2=unp.uarray(brech2,0.5)
#n=unp.sin(ubrech1*const.pi/180.0)/unp.sin(ubrech2*const.pi/180.0)
n=unp.sin(brech1*const.pi/180.0)/unp.sin(brech2*const.pi/180.0)



un=unp.uarray(n.mean(),np.std(n, ddof=1) / np.sqrt(len(n)))
print("n: ",n)
print(f'\nPlexi:= {un:.4f}  \nc= {const.c/un:.4f} \n')



###Platten

def f1(d,platt1, platt2):
    return(d*unp.sin(platt1-platt2)/unp.cos(platt2))

versatz1=(d*unp.sin(brech1-brech2)/unp.cos(brech2))



entf=d*(unp.tan(brech2)-unp.tan(brech1))
print("entf: ",entf)
versatz2=unp.sin(90-brech1)*entf

print(f'\nversatz1:= {versatz1}  \nversatz2= {versatz2} \n\nrelative Abweichung: {((versatz1-versatz2)/versatz1)*100}%')


###Prisma

def delta(a,b):
    return (a*const.pi/180.0+b*const.pi/180.0)-(np.arcsin(np.sin(a*const.pi/180.0)/nkron)-(gam -np.arcsin(np.sin(a*const.pi/180.0)/nkron)))
    
    
    
    
delg=unp.uarray((delta(green1,green2)).mean(),np.std(delta(green1,green2), ddof=1) / np.sqrt(len(delta(green1,green2))))
delr=unp.uarray((delta(green1,red2)).mean(),np.std(delta(green1,red2), ddof=1) / np.sqrt(len(delta(green1,red2))))
print(f'\ndeltagrün:= {delg}  \ndeltarot= {delr}')


table ={'alpha1': green1, 'alphag': green2, 'alphar': red2, 'delg':delta(green1,green2), 'delr':delta(green1,red2)}
print("\n ",tabulate (table, tablefmt="latex"))

###gitter





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







np.savetxt(
    'build/brechung.txt',
    np.column_stack([brech1, brech2,n]),
    fmt=['%.3f', '%.3f','%.3f'],       
    delimiter=' & ',
    header='einf,ausf,n',
)