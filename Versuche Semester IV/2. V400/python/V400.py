import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")



###werte einlesen

#tamp = np.load('python/variables/tamp.npy')
#Uamp = np.load('python/variables/Uamp.npy')




###Konstanten

err=1
d=5.85 e-3 #meter
gam=60 #grad
lamg=532*10-9 #meter
lamr=635*10-9 #meter


###Brechungsindices

nluft=1.000292          #https://www.chemie.de/lexikon/Brechzahl.html
nwasser=1.33
nkron=1.46 #bis 1.65
nplexi=1.49
ndia=2.42



###Reflexion
def lin(x,a,b):
    return (a*x+b)

params, _1 =curve_fit(lin,refl1,refl2,p0=(1,0))
err =np.sqrt(np.diag(_1))
uparams=unp.uarray(params,err)

print(f'\nA:\n= {uparams[0]:.4f}  \n B= {uparams[1]:.4f} \n')


###Brechung
n=unp.sin(brech1)/unp.sin(brech2)


print(f'\nPlexi:\n= {n:.4f}  \n n.sum= {n.sum:.4f} \n')


###Platten

def f1(d,platt1, platt2):
    return(d*unp.sin(platt1-platt2)/unp.cos(platt2))

versatz1=(d*unp.sin(platt1-platt2)/unp.cos(platt2))



entf=d*(unp.tan(platt2)-unp.tan(platt1))
print("entf: ",entf)
versatz2=unp.sin(90-platt1)*entf

print(f'\nversatz1:\n= {versatz1:.4f}  \n versatz2= {versatz2:.4f} \n\nrelative Abweichung: {((versatz1-versatz2/versatz1)*100}%')
###Prisma




###gitter













np.savetxt(
    'build/brechung.txt',
    np.column_stack([brech1, brech2,n]),
    fmt=['%.3f', '%.3f','%.3f'],       
    delimiter=' & ',
    header='einf,ausf,n',
)