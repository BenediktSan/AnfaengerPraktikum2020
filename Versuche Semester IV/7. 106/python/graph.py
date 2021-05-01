import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties import unumpy
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os

if os.path.exists("build") == False:
    os.mkdir("build")


###werte laden

# 1.
T_1_1 = np.load('python/variables/T_1_1', T_1_1 )
T_1_2 = np.load('python/variables/T_1_2', T_1_2 )
T_1_3 = np.load('python/variables/T_1_3', T_1_3 )
T_1_4 = np.load('python/variables/T_1_4', T_1_4 )
T_1_5 = np.load('python/variables/T_1_5', T_1_5 )
T_1_6 = np.load('python/variables/T_1_6', T_1_6 )
T_1_7 = np.load('python/variables/T_1_7', T_1_7 )
T_1_8 = np.load('python/variables/T_1_8', T_1_8 )
T_1_9 = np.load('python/variables/T_1_9', T_1_9 )
T_1_10 = np.load('python/variables/T_1_10', T_1_10)

a = np.linspace(1,5,5)

plt.figure()
plt.plot(a,T_1_1,"x",label="1")
plt.plot(a,T_1_2,"x",label="2")
plt.plot(a,T_1_3,"x",label="3")
plt.plot(a,T_1_4,"x",label="4")
plt.plot(a,T_1_5,"x",label="5")
plt.plot(a,T_1_6,"x",label="6")
plt.plot(a,T_1_7,"x",label="7")
plt.plot(a,T_1_8,"x",label="8")
plt.plot(a,T_1_9,"x",label="9")
plt.plot(a,T_1_10,"x",label="10")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/T_1.pdf")

T_2_1 = np.load('python/variables/T_2_1', T_2_1 )
T_2_2 = np.load('python/variables/T_2_2', T_2_2 )
T_2_3 = np.load('python/variables/T_2_3', T_2_3 )
T_2_4 = np.load('python/variables/T_2_4', T_2_4 )
T_2_5 = np.load('python/variables/T_2_5', T_2_5 )
T_2_6 = np.load('python/variables/T_2_6', T_2_6 )
T_2_7 = np.load('python/variables/T_2_7', T_2_7 )
T_2_8 = np.load('python/variables/T_2_8', T_2_8 )
T_2_9 = np.load('python/variables/T_2_9', T_2_9 )
T_2_10 = np.load('python/variables/T_2_10', T_2_10)

plt.figure()
plt.plot(a,T_2_1,"x",label="1")
plt.plot(a,T_2_2,"x",label="2")
plt.plot(a,T_2_3,"x",label="3")
plt.plot(a,T_2_4,"x",label="4")
plt.plot(a,T_2_5,"x",label="5")
plt.plot(a,T_2_6,"x",label="6")
plt.plot(a,T_2_7,"x",label="7")
plt.plot(a,T_2_8,"x",label="8")
plt.plot(a,T_2_9,"x",label="9")
plt.plot(a,T_2_10,"x",label="10")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/T_2.pdf")

t_1_1 = np.load('python/variables/t_1_1', t_1_1 )
t_1_2 = np.load('python/variables/t_1_2', t_1_2 )
t_1_3 = np.load('python/variables/t_1_3', t_1_3 )
t_1_4 = np.load('python/variables/t_1_4', t_1_4 )
t_1_5 = np.load('python/variables/t_1_5', t_1_5 )
t_1_6 = np.load('python/variables/t_1_6', t_1_6 )
t_1_7 = np.load('python/variables/t_1_7', t_1_7 )
t_1_8 = np.load('python/variables/t_1_8', t_1_8 )
t_1_9 = np.load('python/variables/t_1_9', t_1_9 )
t_1_10 = np.load('python/variables/t_1_10', t_1_10)

plt.figure()
plt.plot(a,t_1_1,"x",label="1")
plt.plot(a,t_1_2,"x",label="2")
plt.plot(a,t_1_3,"x",label="3")
plt.plot(a,t_1_4,"x",label="4")
plt.plot(a,t_1_5,"x",label="5")
plt.plot(a,t_1_6,"x",label="6")
plt.plot(a,t_1_7,"x",label="7")
plt.plot(a,t_1_8,"x",label="8")
plt.plot(a,t_1_9,"x",label="9")
plt.plot(a,t_1_10,"x",label="10")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/t_1.pdf")

t_2_1 = np.load('python/variables/t_2_1', t_2_1 )
t_2_2 = np.load('python/variables/t_2_2', t_2_2 )
t_2_3 = np.load('python/variables/t_2_3', t_2_3 )
t_2_4 = np.load('python/variables/t_2_4', t_2_4 )
t_2_5 = np.load('python/variables/t_2_5', t_2_5 )
t_2_6 = np.load('python/variables/t_2_6', t_2_6 )
t_2_7 = np.load('python/variables/t_2_7', t_2_7 )
t_2_8 = np.load('python/variables/t_2_8', t_2_8 )
t_2_9 = np.load('python/variables/t_2_9', t_2_9 )
t_2_10 = np.load('python/variables/T_2_10', T_2_10)

plt.figure()
plt.plot(a,t_2_1,"x",label="1")
plt.plot(a,t_2_2,"x",label="2")
plt.plot(a,t_2_3,"x",label="3")
plt.plot(a,t_2_4,"x",label="4")
plt.plot(a,t_2_5,"x",label="5")
plt.plot(a,t_2_6,"x",label="6")
plt.plot(a,t_2_7,"x",label="7")
plt.plot(a,t_2_8,"x",label="8")
plt.plot(a,t_2_9,"x",label="9")
plt.plot(a,t_2_10,"x",label="10")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/t_2.pdf")

#2.

T_gleich_1 = np.load('python/variables/T_gleich_1', T_gleich_1)
T_gleich_2 = np.load('python/variables/T_gleich_2', T_gleich_2)
T_gleich_3 = np.load('python/variables/T_gleich_3', T_gleich_3)
T_gleich_4 = np.load('python/variables/T_gleich_4', T_gleich_4)
T_gleich_5 = np.load('python/variables/T_gleich_5', T_gleich_5)

plt.figure()
plt.plot(a,T_gleich_1,"x",label="1")
plt.plot(a,T_gleich_2,"x",label="2")
plt.plot(a,T_gleich_3,"x",label="3")
plt.plot(a,T_gleich_4,"x",label="4")
plt.plot(a,T_gleich_5,"x",label="5")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/T_gleich.pdf")

T_gegen_1 = np.load('python/variables/T_gegen_1', T_gegen_1)
T_gegen_2 = np.load('python/variables/T_gegen_2', T_gegen_2)
T_gegen_3 = np.load('python/variables/T_gegen_3', T_gegen_3)
T_gegen_4 = np.load('python/variables/T_gegen_4', T_gegen_4)
T_gegen_5 = np.load('python/variables/T_gegen_5', T_gegen_5)

plt.figure()
plt.plot(a,T_gegen_1,"x",label="1")
plt.plot(a,T_gegen_2,"x",label="2")
plt.plot(a,T_gegen_3,"x",label="3")
plt.plot(a,T_gegen_4,"x",label="4")
plt.plot(a,T_gegen_5,"x",label="5")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/T_gegen.pdf")

t_gleich_1 = np.load('python/variables/t_gleich_1', t_gleich_1)
t_gleich_2 = np.load('python/variables/t_gleich_2', t_gleich_2)
t_gleich_3 = np.load('python/variables/t_gleich_3', t_gleich_3)
t_gleich_4 = np.load('python/variables/t_gleich_4', t_gleich_4)
t_gleich_5 = np.load('python/variables/t_gleich_5', t_gleich_5)

plt.figure()
plt.plot(a,t_gleich_1,"x",label="1")
plt.plot(a,t_gleich_2,"x",label="2")
plt.plot(a,t_gleich_3,"x",label="3")
plt.plot(a,t_gleich_4,"x",label="4")
plt.plot(a,t_gleich_5,"x",label="5")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/t_gleich.pdf")

t_gegen_1 = np.load('python/variables/t_gegen_1', t_gegen_1)
t_gegen_2 = np.load('python/variables/t_gegen_2', t_gegen_2)
t_gegen_3 = np.load('python/variables/t_gegen_3', t_gegen_3)
t_gegen_4 = np.load('python/variables/t_gegen_4', t_gegen_4)
t_gegen_5 = np.load('python/variables/t_gegen_5', t_gegen_5)

plt.figure()
plt.plot(a,t_gegen_1,"x",label="1")
plt.plot(a,t_gegen_2,"x",label="2")
plt.plot(a,t_gegen_3,"x",label="3")
plt.plot(a,t_gegen_4,"x",label="4")
plt.plot(a,t_gegen_5,"x",label="5")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/t_gegen.pdf")

#3.

T_gekop_schwing_1 = np.load('python/variables/T_gekop_schwing_1', T_gekop_schwing_1)
T_gekop_schwing_2 = np.load('python/variables/T_gekop_schwing_2', T_gekop_schwing_2)
T_gekop_schwing_3 = np.load('python/variables/T_gekop_schwing_3', T_gekop_schwing_3)
T_gekop_schwing_4 = np.load('python/variables/T_gekop_schwing_4', T_gekop_schwing_4)
T_gekop_schwing_5 = np.load('python/variables/T_gekop_schwing_5', T_gekop_schwing_5)

plt.figure()
plt.plot(a,T_gekop_schwing_1,"x",label="1")
plt.plot(a,T_gekop_schwing_2,"x",label="2")
plt.plot(a,T_gekop_schwing_3,"x",label="3")
plt.plot(a,T_gekop_schwing_4,"x",label="4")
plt.plot(a,T_gekop_schwing_5,"x",label="5")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/T_gekop_schwing.pdf")

T_gekop_schweb_1 = np.load('python/variables/T_gekop_schweb_1', T_gekop_schweb_1)
T_gekop_schweb_2 = np.load('python/variables/T_gekop_schweb_2', T_gekop_schweb_2)
T_gekop_schweb_3 = np.load('python/variables/T_gekop_schweb_3', T_gekop_schweb_3)
T_gekop_schweb_4 = np.load('python/variables/T_gekop_schweb_4', T_gekop_schweb_4)
T_gekop_schweb_5 = np.load('python/variables/T_gekop_schweb_5', T_gekop_schweb_5)

plt.figure()
plt.plot(a,T_gekop_schweb_1,"x",label="1")
plt.plot(a,T_gekop_schweb_2,"x",label="2")
plt.plot(a,T_gekop_schweb_3,"x",label="3")
plt.plot(a,T_gekop_schweb_4,"x",label="4")
plt.plot(a,T_gekop_schweb_5,"x",label="5")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/T_gekop_schweb.pdf")

t_gekop_schwing_1 = np.load('python/variables/t_gekop_schwing_1', t_gekop_schwing_1)
t_gekop_schwing_2 = np.load('python/variables/t_gekop_schwing_2', t_gekop_schwing_2)
t_gekop_schwing_3 = np.load('python/variables/t_gekop_schwing_3', t_gekop_schwing_3)
t_gekop_schwing_4 = np.load('python/variables/t_gekop_schwing_4', t_gekop_schwing_4)
t_gekop_schwing_5 = np.load('python/variables/t_gekop_schwing_5', t_gekop_schwing_5)

plt.figure()
plt.plot(a,t_gekop_schwing_1,"x",label="1")
plt.plot(a,t_gekop_schwing_2,"x",label="2")
plt.plot(a,t_gekop_schwing_3,"x",label="3")
plt.plot(a,t_gekop_schwing_4,"x",label="4")
plt.plot(a,t_gekop_schwing_5,"x",label="5")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/t_gekop_schwing.pdf")

t_gekop_schweb_1 = np.load('python/variables/t_gekop_schweb_1', t_gekop_schweb_1)
t_gekop_schweb_2 = np.load('python/variables/t_gekop_schweb_2', t_gekop_schweb_2)
t_gekop_schweb_3 = np.load('python/variables/t_gekop_schweb_3', t_gekop_schweb_3)
t_gekop_schweb_4 = np.load('python/variables/t_gekop_schweb_4', t_gekop_schweb_4)
t_gekop_schweb_5 = np.load('python/variables/t_gekop_schweb_5', t_gekop_schweb_5)

plt.figure()
plt.plot(a,t_gekop_schweb_1,"x",label="1")
plt.plot(a,t_gekop_schweb_2,"x",label="2")
plt.plot(a,t_gekop_schweb_3,"x",label="3")
plt.plot(a,t_gekop_schweb_4,"x",label="4")
plt.plot(a,t_gekop_schweb_5,"x",label="5")
plt.xlabel("n")
plt.ylabel("Schwingungsdauer[s]")
plt.legend()
plt.savefig("build/t_gekop_schweb.pdf")
