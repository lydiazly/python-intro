#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017-06-15 written by Lydia
# 2018-01-24 modified by Lydia
from __future__ import division, print_function
from math import *
import numpy as np
import matplotlib.pyplot as plt
from evtk.hl import gridToVTK

ngrid = 200

k1 = pi/10.
k2 = 3.*k1
d1 = 0.2
b1 = 1.
b2 = b1

#### Calculate ########################################################|
x, y, z= (np.linspace(-5, 5, ngrid + 1),
          np.linspace(-5, 5, ngrid + 1),
          np.linspace(0, 10, ngrid + 1),
)  # float64
X, Y, Z = np.mgrid[-5:5:(ngrid + 1)*1j, -5:5:(ngrid + 1)*1j, 0:10:(ngrid + 1)*1j]

# U, V, W
U =   (b1 * np.cos(k1 * X) * np.exp(-k1 * (Z + d1))
     - b2 * np.cos(k2 * X) * np.exp(-k2 * (Z + d1)))
W = (- b1 * np.sin(k1 * X) * np.exp(-k1 * (Z + d1))
     + b2 * np.sin(k2 * X) * np.exp(-k2 * (Z + d1)))
V = 0.5 * U

bmag = np.sqrt(U**2 + V**2 + W**2)

#### Info #############################################################|
print('b(0, 0) = %.6f' % (bmag[ngrid//2, 0, 0]))
print('b_max = %.6f' % (np.max(bmag)))

#### Save to VTK ######################################################|
# generate 'xxx.vtr'
# (to generate 'xxx.vts' should use X, Y, Z )
gridToVTK("./field2d", x, y, z, pointData = dict(bmag=bmag, bvec=(U, V, W)))
print('Data saved: ./field2d.vtr')
