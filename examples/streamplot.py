#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017-06-03 written by Lydia
# 2017-10-29 modified by Lydia
from __future__ import division, print_function
# from math import *
import matplotlib
matplotlib.use('TkAgg')  # 'Qt5Agg', 'TkAgg', 'Agg', ...
import matplotlib.pyplot as plt
import numpy as np

ngrid = 800

k1 = np.pi/10.  # math: pi  numpy: np.pi
k2 = 3.*k1
d1 = 0.2
b1 = 1.
b2 = b1

#### Calculate ########################################################|
x, y = (np.linspace(-5, 5, ngrid + 1), np.linspace(0, 10, ngrid + 1))  # float64

X, Y = np.meshgrid(x, y)

U =   (b1 * np.cos(k1 * X) * np.exp(-k1 * (Y + d1))
     - b2 * np.cos(k2 * X) * np.exp(-k2 * (Y + d1)))
V = (- b1 * np.sin(k1 * X) * np.exp(-k1 * (Y + d1))
     + b2 * np.sin(k2 * X) * np.exp(-k2 * (Y + d1)))

mag = np.sqrt(U**2 + V**2)

print('b(0, 0) = %.6f' % (mag[0, ngrid//2]))
print('b_max = %.6f' % (np.max(mag)))

#### Plot #############################################################|
fig = plt.figure()
ax = fig.add_subplot(111)
ax.streamplot(x, y, U, V, color=V, linewidth=1.5, cmap=plt.cm.autumn, density=1.6, minlength=0.6)
plt.axis([-5, 5, 0, 10])
ax.set_aspect(1)
plt.tight_layout(0.8)

plt.show()
