import datetime
import time
import numpy as np
import statistics as stat
from numpoisson.numpoisson import NumPoissonGeometry

npg = NumPoissonGeometry(3, 'x')
P_so3 = {(1, 2): 'x3', (1, 3): '-x2', (2, 3): 'x1'}

num_bivector_res = dict()
for i in [2, 3, 4, 5, 6, 7, 8]
    Qmesh_10_3 = np.random.rand(10**i, 3)
    tiempos = dict()
    for k in range(25):
        A = datetime.datetime.now()
        npg.num_bivector(P_so3, Qmesh_10_3, pt_output=True)
        B = datetime.datetime.now()
        tiempos[k] = (B - A).total_seconds()
    num_bivector_res[f'10**{i}'] = tiempos

print(num_bivector_res)