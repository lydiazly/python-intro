#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function
# import matplotlib
# matplotlib.use('TkAgg')  # 'Qt5Agg', 'TkAgg', 'Agg', ...
import matplotlib.pyplot as plt
import numpy as np

x, y = np.mgrid[-1:1:10j, -1:1:10j]
z = (x + y) * np.exp(-6.0 * (x * x + y * y))

fig = plt.figure(1, (8, 5))  # num=1, figsize=(8, 5)
ax = fig.add_subplot(111)

im = plt.imshow(z, cmap='viridis', extent=(-1, 1, -1, 1),
                origin='lower',
                aspect=0.8,
                interpolation='spline16')
                # {'nearest', 'bilinear', 'spline16'}

plt.colorbar();  # aspect/='auto'时如果colorbar对不齐, 调整figsize比例即可

# 随鼠标显示数据
# pip install mpldatacursor
# https://github.com/joferkington/mpldatacursor
try:
    from mpldatacursor import datacursor
    datacursor(im, hover=True, bbox=dict(alpha=0.8, fc='w'));
except:
    pass

plt.show()  # 一般在jupyter notebook中不需要这一行(除非发现无法显示图像)