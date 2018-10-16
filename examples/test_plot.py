#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function
# import matplotlib
# matplotlib.use('TkAgg')  # 'Qt5Agg', 'TkAgg', 'Agg', ...
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0., 6., 10)
y = np.sin(x)

# 如果点数少, 插值到更细的格点
from scipy.interpolate import interp1d
x2 = np.linspace(x[0], x[-1], 100)
f = interp1d(x, y, kind='cubic')  # {'linear', 'cubic'}
y2 = f(x2)

fig = plt.figure(1, (6, 10), dpi=100)  # (num, size(*dpi))
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412, sharex=ax1)  # 共用x坐标
ax3 = fig.add_subplot(413, sharex=ax1)
ax4 = fig.add_subplot(414, sharex=ax1)
axlist = (ax1, ax2, ax3, ax4)  # 方便下面调整外观

ax1.plot(x, y, '-')

ax2.plot(x, y, 'o', x2, y2, '-')  # 此时后画的图层在上

ax3.plot(x, y, 'x', color='navy', ms=8, mew=2, zorder=2)  # zorder控制图层上下
ax3.plot(x2, y2, '-', color='plum', lw=4, zorder=1)

ax4.plot(x2, y2, 'g--', lw=3, label='interp1d')  # label用于legend
ax4.plot(x, y, 'o', ms=10, mfc=(1,1,1,0.5), mec='m', mew=2, label='data')
ax4.plot(x2, 0.*x2, 'k-', alpha=0.6)
# markers默认在最上图层
ax4.legend(loc='upper right', fontsize=14)

fig.subplots_adjust(hspace=0.06)  # 设置 subplots 间隔

ax1.set_title('Fig. 1', fontsize=16, y=1.02);
# `;` 仅需在jupyter notebook使用
ax1.set_ylabel(r"$f_1(x)$", fontsize=14)
ax2.set_ylabel(r"$f_2(x)$", fontsize=14)
ax3.set_ylabel(r"$f_3(x)$", fontsize=14)
ax4.set_ylabel(r"$f_4(x)$", fontsize=14)
axlist[-1].set_xlabel(r"$x$", fontsize=14)
ax1.set_xlim((0., 6.))

for ax in axlist:
    ax.yaxis.set_label_position("right")  # y 轴 labal 位置
    ax.tick_params(direction='in')  # ticks 朝向内部
for ax in axlist[:-1]:
    # remove xticks
    plt.setp(ax.get_xticklabels(), visible=False)
    # remove the fist ytick
    yticks = ax.yaxis.get_major_ticks()
    yticks[0].label1.set_visible(False) # label1: 左侧的y轴

# 存图
# fig.savefig('figname.pdf', bbox_inches='tight')
# fig.savefig('figname.png', dpi=200, bbox_inches='tight')

# 跨多个图的随鼠标移动的竖线
from matplotlib.widgets import MultiCursor
cursor = MultiCursor(fig.canvas, axlist, useblit=True, color='gray', lw=1)

plt.show()  # 一般在jupyter notebook中不需要这一行(除非发现无法显示图像)