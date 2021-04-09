import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os



if os.path.exists("python/tabellen") == False:
    os.mkdir("python/tabellen")


#       Laden der woanders eingelesenen Daten:

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

#2.

T_gleich_1 = np.load('python/variables/T_gleich_1', T_gleich_1)
T_gleich_2 = np.load('python/variables/T_gleich_2', T_gleich_2)
T_gleich_3 = np.load('python/variables/T_gleich_3', T_gleich_3)
T_gleich_4 = np.load('python/variables/T_gleich_4', T_gleich_4)
T_gleich_5 = np.load('python/variables/T_gleich_5', T_gleich_5)

T_gegen_1 = np.load('python/variables/T_gegen_1', T_gegen_1)
T_gegen_2 = np.load('python/variables/T_gegen_2', T_gegen_2)
T_gegen_3 = np.load('python/variables/T_gegen_3', T_gegen_3)
T_gegen_4 = np.load('python/variables/T_gegen_4', T_gegen_4)
T_gegen_5 = np.load('python/variables/T_gegen_5', T_gegen_5)

t_gleich_1 = np.load('python/variables/t_gleich_1', t_gleich_1)
t_gleich_2 = np.load('python/variables/t_gleich_2', t_gleich_2)
t_gleich_3 = np.load('python/variables/t_gleich_3', t_gleich_3)
t_gleich_4 = np.load('python/variables/t_gleich_4', t_gleich_4)
t_gleich_5 = np.load('python/variables/t_gleich_5', t_gleich_5)

t_gegen_1 = np.load('python/variables/t_gegen_1', t_gegen_1)
t_gegen_2 = np.load('python/variables/t_gegen_2', t_gegen_2)
t_gegen_3 = np.load('python/variables/t_gegen_3', t_gegen_3)
t_gegen_4 = np.load('python/variables/t_gegen_4', t_gegen_4)
t_gegen_5 = np.load('python/variables/t_gegen_5', t_gegen_5)

#3.

T_gekop_schwing_1 = np.load('python/variables/T_gekop_schwing_1', T_gekop_schwing_1)
T_gekop_schwing_2 = np.load('python/variables/T_gekop_schwing_2', T_gekop_schwing_2)
T_gekop_schwing_3 = np.load('python/variables/T_gekop_schwing_3', T_gekop_schwing_3)
T_gekop_schwing_4 = np.load('python/variables/T_gekop_schwing_4', T_gekop_schwing_4)
T_gekop_schwing_5 = np.load('python/variables/T_gekop_schwing_5', T_gekop_schwing_5)

T_gekop_schweb_1 = np.load('python/variables/T_gekop_schweb_1', T_gekop_schweb_1)
T_gekop_schweb_2 = np.load('python/variables/T_gekop_schweb_2', T_gekop_schweb_2)
T_gekop_schweb_3 = np.load('python/variables/T_gekop_schweb_3', T_gekop_schweb_3)
T_gekop_schweb_4 = np.load('python/variables/T_gekop_schweb_4', T_gekop_schweb_4)
T_gekop_schweb_5 = np.load('python/variables/T_gekop_schweb_5', T_gekop_schweb_5)

t_gekop_schwing_1 = np.load('python/variables/t_gekop_schwing_1', t_gekop_schwing_1)
t_gekop_schwing_2 = np.load('python/variables/t_gekop_schwing_2', t_gekop_schwing_2)
t_gekop_schwing_3 = np.load('python/variables/t_gekop_schwing_3', t_gekop_schwing_3)
t_gekop_schwing_4 = np.load('python/variables/t_gekop_schwing_4', t_gekop_schwing_4)
t_gekop_schwing_5 = np.load('python/variables/t_gekop_schwing_5', t_gekop_schwing_5)

t_gekop_schweb_1 = np.load('python/variables/t_gekop_schweb_1', t_gekop_schweb_1)
t_gekop_schweb_2 = np.load('python/variables/t_gekop_schweb_2', t_gekop_schweb_2)
t_gekop_schweb_3 = np.load('python/variables/t_gekop_schweb_3', t_gekop_schweb_3)
t_gekop_schweb_4 = np.load('python/variables/t_gekop_schweb_4', t_gekop_schweb_4)
t_gekop_schweb_5 = np.load('python/variables/t_gekop_schweb_5', t_gekop_schweb_5)


#       Tabellen erstellen

np.savetxt(
    'python/tabellen/T_1.txt',
    np.column_stack([T_1_1,T_1_2,T_1_3,T_1_4,T_1_5,T_1_6,T_1_7,T_1_8,T_1_9,T_1_10]),
    fmt=['%.4f', '%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f'],       
    delimiter=' & ',
    header='T_1',
)

np.savetxt(
    'python/tabellen/T_2.txt',
    np.column_stack([T_2_1,T_2_2,T_2_3,T_2_4,T_2_5,T_2_6,T_2_7,T_2_8,T_2_9,T_2_10]),
    fmt=['%.4f', '%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f'],       
    delimiter=' & ',
    header='T_2',
)

np.savetxt(
    'python/tabellen/t_1.txt',
    np.column_stack([t_1_1,t_1_2,t_1_3,t_1_4,t_1_5,t_1_6,t_1_7,t_1_8,t_1_9,t_1_10]),
    fmt=['%.4f', '%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f'],       
    delimiter=' & ',
    header='t_1',
)

np.savetxt(
    'python/tabellen/t_2.txt',
    np.column_stack([t_2_1,t_2_2,t_2_3,t_2_4,t_2_5,t_2_6,t_2_7,t_2_8,t_2_9,t_2_10]),
    fmt=['%.4f', '%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f'],       
    delimiter=' & ',
    header='t_2',
)

np.savetxt(
    'python/tabellen/T_gleich.txt',
    np.column_stack([T_gleich_1,T_gleich_2,T_gleich_3,T_gleich_4,T_gleich_5,t_gleich_1,t_gleich_2,t_gleich_3,t_gleich_4,t_gleich_5]),
    fmt=['%.4f', '%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f'],       
    delimiter=' & ',
    header='T_gleich, t_gleich',
)

np.savetxt(
    'python/tabellen/T_gegen.txt',
    np.column_stack([T_gegen_1,T_gegen_2,T_gegen_3,T_gegen_4,T_gegen_5,t_gegen_1,t_gegen_2,t_gegen_3,t_gegen_4,t_gegen_5]),
    fmt=['%.4f', '%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f'],       
    delimiter=' & ',
    header='T_gleich, t_gleich',
)

np.savetxt(
    'python/tabellen/T_gekop_schwing.txt',
    np.column_stack([T_gekop_schwing_1,T_gekop_schwing_2,T_gekop_schwing_3,T_gekop_schwing_4,T_gekop_schwing_5,t_gekop_schwing_1,t_gekop_schwing_2,t_gekop_schwing_3,t_gekop_schwing_4,t_gekop_schwing_5]),
    fmt=['%.4f', '%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f'],       
    delimiter=' & ',
    header='T_gekop_schwing,t_gekop_schwing',
)

np.savetxt(
    'python/tabellen/T_gekop_schweb.txt',
    np.column_stack([T_gekop_schweb_1,T_gekop_schweb_2,T_gekop_schweb_3,T_gekop_schweb_4,T_gekop_schweb_5,t_gekop_schweb_1,t_gekop_schweb_2,t_gekop_schweb_3,t_gekop_schweb_4,t_gekop_schweb_5]),
    fmt=['%.4f', '%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f','%.4f'],       
    delimiter=' & ',
    header='T_gekop_schweb,t_gekop_schweb',
)