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

# Get info on click
def onclick(event):
    import matplotlib.transforms as mtransforms
    xdata, ydata = (event.xdata, event.ydata)
    ax = plt.gca()
    im = plt.gci()
    # https://github.com/joferkington/mpldatacursor/blob/master/mpldatacursor/pick_info.py
    xmin, xmax, ymin, ymax = im.get_extent()
    if im.origin == 'upper':
        ymin, ymax = ymax, ymin
    data_extent = mtransforms.Bbox([[ymin, xmin], [ymax, xmax]])
    array_extent = mtransforms.Bbox([[0, 0], im.get_array().shape[:2]])
    trans = (mtransforms.BboxTransformFrom(data_extent)  # linearly transforms points from a given Bbox to the unit bounding box.
            + mtransforms.BboxTransformTo(array_extent))  # linearly transforms points from the unit bounding box to a given Bbox.
    i, j = trans.transform_point([ydata, xdata]).astype(int)
    print('x={:g}, y={:g}, c={:g}'.format(
          xdata, ydata, im.get_array()[i, j]))

fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()