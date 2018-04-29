#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2018-04-10  10:20
# @Author  : PengZhw
# @FileName: regression_test.py
# @Software: PyCharm

import numpy as np
from scipy.optimize import leastsq
import pylab as pl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 注意用numpy的数组而不是python内建的list
points = [[1.2, 1.2, 4.26], [1.7, 0.2, 4.0], [6.5, 3.0, 14.56], [3.5, 5.0, 13.26]]
x_list = np.array([1.2, 1.7, 6.5, 3.5])
y_list = np.array([1.2, 0.2, 3.0, 5.0])
z_list = np.array([4.26, 4.0, 14.56, 13.26])


def func(x, y, p,):
    """
    拟合所用函数：z = ax+by+c

    :param x:
    :param y:
    :param p:
    :return:
    """
    a, b, c = p
    return a*x+b*y+c


def residuals(p, x, y, z):
    """
    实验数据x,y,z和拟合函数之间的差，p为拟合需要找到的系数
    :param p:
    :param z:
    :param x:
    :param y:
    :return:
    """
    return z - func(x, y, p)


p0 = [1.3, 1, 1]    # 第一次猜测的拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
plsq = leastsq(residuals, p0, args=(x_list, y_list, z_list))

print("拟合参数", plsq[0])


fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-2, 4, 0.25)
X, Y = np.meshgrid(X, Y)
Z = plsq[0][0] * X + plsq[0][1] * Y + plsq[0][2]
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha = 0.3)

plt.show()
