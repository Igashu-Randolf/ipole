import matplotlib.pyplot as plt
import numpy as np
import pyharm
import pandas as pd

#Constant
dump = pyharm.load_dump("torus.out0.05999.h5")

dim = dump['u^r'].shape

N1 = dim[0]
N2 = dim[1]
N3 = dim [2]

eta = 0.1; # arbitrary parameter
a = 0.9375

z1 = 1 + (1 - a ** 2) ** (1/3) * (1 + a) ** (1/3) + (1 - a) ** (1/3)
z2 = (3 * a ** 2 + z1 ** 2) ** 0.5
r_isco = 3 + z2 - ((3 - z1) * (3 + z1 + 2 * z2)) ** 0.5

#load dump
dx = dump['dx']
#plt.plot(dump['r1d'], pyharm.shell_avg(dump, 'u^phi'))
df = pd.DataFrame({'r': np.log(dump['r1d']), 'uphi': pyharm.shell_avg(dump, 'u3'), 'ur':pyharm.shell_avg(dump, 'u1')})


dydx = np.gradient(df['uphi'], dx[1])
qshear = np.array(- df['r'] * dydx / df['uphi'])

#qshear_the = (1 - 2 / df['r'] + a ** 2 / df['r'] ** 2) / (1 - 3 / df['r'] + 2 * a * df['r'] ** -1.5)
#plt.plot(df['r'], qshear_the, label='Gammie, 2004')

#nR against r


nR = np.log(df['ur'] / eta) / np.log(r_isco / df['r'])