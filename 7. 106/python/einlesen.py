import numpy as np
from uncertainties import ufloat
import os

# Variablen Ordner anlegen

if os.path.exists("python/variables") == False:
    os.mkdir("python/variables")

# Daten 

# 1.

T_1_1   = np.array([])
T_1_2   = np.array([])
T_1_3   = np.array([])
T_1_4   = np.array([])
T_1_5   = np.array([])
T_1_6   = np.array([])
T_1_7   = np.array([])
T_1_8   = np.array([])
T_1_9   = np.array([])
T_1_10  = np.array([])

np.save('python/variables/T_1_1', T_1_1, allow_pickle=False)
np.save('python/variables/T_1_2', T_1_2, allow_pickle=False)
np.save('python/variables/T_1_3', T_1_3, allow_pickle=False)
np.save('python/variables/T_1_4', T_1_4, allow_pickle=False)
np.save('python/variables/T_1_5', T_1_5, allow_pickle=False)
np.save('python/variables/T_1_6', T_1_6, allow_pickle=False)
np.save('python/variables/T_1_7', T_1_7, allow_pickle=False)
np.save('python/variables/T_1_8', T_1_8, allow_pickle=False)
np.save('python/variables/T_1_9', T_1_9, allow_pickle=False)
np.save('python/variables/T_1_10', T_1_10, allow_pickle=False)

T_2_1   =np.array([])
T_2_2   =np.array([])
T_2_3   =np.array([])
T_2_4   =np.array([])
T_2_5   =np.array([])
T_2_6   =np.array([])
T_2_7   =np.array([])
T_2_8   =np.array([])
T_2_9   =np.array([])
T_2_10  =np.array([])

np.save('python/variables/T_2_1', T_2_1, allow_pickle=False)
np.save('python/variables/T_2_2', T_2_2, allow_pickle=False)
np.save('python/variables/T_2_3', T_2_3, allow_pickle=False)
np.save('python/variables/T_2_4', T_2_4, allow_pickle=False)
np.save('python/variables/T_2_5', T_2_5, allow_pickle=False)
np.save('python/variables/T_2_6', T_2_6, allow_pickle=False)
np.save('python/variables/T_2_7', T_2_7, allow_pickle=False)
np.save('python/variables/T_2_8', T_2_8, allow_pickle=False)
np.save('python/variables/T_2_9', T_2_9, allow_pickle=False)
np.save('python/variables/T_2_10', T_2_10, allow_pickle=False)

# zweiter Durchlauf

t_1_1   =np.array([])
t_1_2   =np.array([])
t_1_3   =np.array([])
t_1_4   =np.array([])
t_1_5   =np.array([])
t_1_6   =np.array([])
t_1_7   =np.array([])
t_1_8   =np.array([])
t_1_9   =np.array([])
t_1_10  =np.array([])

np.save('python/variables/t_1_1', t_1_1, allow_pickle=False)
np.save('python/variables/t_1_2', t_1_2, allow_pickle=False)
np.save('python/variables/t_1_3', t_1_3, allow_pickle=False)
np.save('python/variables/t_1_4', t_1_4, allow_pickle=False)
np.save('python/variables/t_1_5', t_1_5, allow_pickle=False)
np.save('python/variables/t_1_6', t_1_6, allow_pickle=False)
np.save('python/variables/t_1_7', t_1_7, allow_pickle=False)
np.save('python/variables/t_1_8', t_1_8, allow_pickle=False)
np.save('python/variables/t_1_9', t_1_9, allow_pickle=False)
np.save('python/variables/t_1_10', t_1_10, allow_pickle=False)

t_2_1   =np.array([])
t_2_2   =np.array([])
t_2_3   =np.array([])
t_2_4   =np.array([])
t_2_5   =np.array([])
t_2_6   =np.array([])
t_2_7   =np.array([])
t_2_8   =np.array([])
t_2_9   =np.array([])
t_2_10  =np.array([])

np.save('python/variables/t_2_1', t_2_1, allow_pickle=False)
np.save('python/variables/t_2_2', t_2_2, allow_pickle=False)
np.save('python/variables/t_2_3', t_2_3, allow_pickle=False)
np.save('python/variables/t_2_4', t_2_4, allow_pickle=False)
np.save('python/variables/t_2_5', t_2_5, allow_pickle=False)
np.save('python/variables/t_2_6', t_2_6, allow_pickle=False)
np.save('python/variables/t_2_7', t_2_7, allow_pickle=False)
np.save('python/variables/t_2_8', t_2_8, allow_pickle=False)
np.save('python/variables/t_2_9', t_2_9, allow_pickle=False)
np.save('python/variables/t_2_10', t_2_10, allow_pickle=False)

#2.

T_gleich_1  =np.array([])
T_gleich_2  =np.array([])
T_gleich_3  =np.array([])
T_gleich_4  =np.array([])
T_gleich_5  =np.array([])

np.save('python/variables/T_gleich_1', T_gleich_1, allow_pickle=False)
np.save('python/variables/T_gleich_2', T_gleich_2, allow_pickle=False)
np.save('python/variables/T_gleich_3', T_gleich_3, allow_pickle=False)
np.save('python/variables/T_gleich_4', T_gleich_4, allow_pickle=False)
np.save('python/variables/T_gleich_5', T_gleich_5, allow_pickle=False)

T_gegen_1    =np.array([])
T_gegen_2    =np.array([])
T_gegen_3    =np.array([])
T_gegen_4    =np.array([])
T_gegen_5    =np.array([])

np.save('python/variables/T_gegen_1', T_gegen_1, allow_pickle=False)
np.save('python/variables/T_gegen_2', T_gegen_2, allow_pickle=False)
np.save('python/variables/T_gegen_3', T_gegen_3, allow_pickle=False)
np.save('python/variables/T_gegen_4', T_gegen_4, allow_pickle=False)
np.save('python/variables/T_gegen_5', T_gegen_5, allow_pickle=False)

# zweiter Durchlauf

t_gleich_1  =np.array([])
t_gleich_2  =np.array([])
t_gleich_3  =np.array([])
t_gleich_4  =np.array([])
t_gleich_5  =np.array([])

np.save('python/variables/t_gleich_1', t_gleich_1, allow_pickle=False)
np.save('python/variables/t_gleich_2', t_gleich_2, allow_pickle=False)
np.save('python/variables/t_gleich_3', t_gleich_3, allow_pickle=False)
np.save('python/variables/t_gleich_4', t_gleich_4, allow_pickle=False)
np.save('python/variables/t_gleich_5', t_gleich_5, allow_pickle=False)

t_gegen_1    =np.array([])
t_gegen_2    =np.array([])
t_gegen_3    =np.array([])
t_gegen_4    =np.array([])
t_gegen_5    =np.array([])

np.save('python/variables/t_gegen_1', t_gegen_1, allow_pickle=False)
np.save('python/variables/t_gegen_2', t_gegen_2, allow_pickle=False)
np.save('python/variables/t_gegen_3', t_gegen_3, allow_pickle=False)
np.save('python/variables/t_gegen_4', t_gegen_4, allow_pickle=False)
np.save('python/variables/t_gegen_5', t_gegen_5, allow_pickle=False)

#3.

T_gekop_schwing_1    =np.array([])
T_gekop_schwing_2    =np.array([])
T_gekop_schwing_3    =np.array([])
T_gekop_schwing_4    =np.array([])
T_gekop_schwing_5    =np.array([])

np.save('python/variables/T_gekop_schwing_1', T_gekop_schwing_1, allow_pickle=False)
np.save('python/variables/T_gekop_schwing_2', T_gekop_schwing_2, allow_pickle=False)
np.save('python/variables/T_gekop_schwing_3', T_gekop_schwing_3, allow_pickle=False)
np.save('python/variables/T_gekop_schwing_4', T_gekop_schwing_4, allow_pickle=False)
np.save('python/variables/T_gekop_schwing_5', T_gekop_schwing_5, allow_pickle=False)

T_gekop_schweb_1    =np.array([])
T_gekop_schweb_2    =np.array([])
T_gekop_schweb_3    =np.array([])
T_gekop_schweb_4    =np.array([])
T_gekop_schweb_5    =np.array([])

np.save('python/variables/T_gekop_schweb_1', T_gekop_schweb_1, allow_pickle=False)
np.save('python/variables/T_gekop_schweb_2', T_gekop_schweb_2, allow_pickle=False)
np.save('python/variables/T_gekop_schweb_3', T_gekop_schweb_3, allow_pickle=False)
np.save('python/variables/T_gekop_schweb_4', T_gekop_schweb_4, allow_pickle=False)
np.save('python/variables/T_gekop_schweb_5', T_gekop_schweb_5, allow_pickle=False)

# zweiter Durchlauf

t_gekop_schwing_1    =np.array([])
t_gekop_schwing_2    =np.array([])
t_gekop_schwing_3    =np.array([])
t_gekop_schwing_4    =np.array([])
t_gekop_schwing_5    =np.array([])

np.save('python/variables/t_gekop_schwing_1', t_gekop_schwing_1, allow_pickle=False)
np.save('python/variables/t_gekop_schwing_2', t_gekop_schwing_2, allow_pickle=False)
np.save('python/variables/t_gekop_schwing_3', t_gekop_schwing_3, allow_pickle=False)
np.save('python/variables/t_gekop_schwing_4', t_gekop_schwing_4, allow_pickle=False)
np.save('python/variables/t_gekop_schwing_5', t_gekop_schwing_5, allow_pickle=False)

t_gekop_schweb_1    =np.array([])
t_gekop_schweb_2    =np.array([])
t_gekop_schweb_3    =np.array([])
t_gekop_schweb_4    =np.array([])
t_gekop_schweb_5    =np.array([])

np.save('python/variables/t_gekop_schweb_1', t_gekop_schweb_1, allow_pickle=False)
np.save('python/variables/t_gekop_schweb_2', t_gekop_schweb_2, allow_pickle=False)
np.save('python/variables/t_gekop_schweb_3', t_gekop_schweb_3, allow_pickle=False)
np.save('python/variables/t_gekop_schweb_4', t_gekop_schweb_4, allow_pickle=False)
np.save('python/variables/t_gekop_schweb_5', t_gekop_schweb_5, allow_pickle=False)

