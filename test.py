#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2018-04-10  16:21
# @Author  : PengZhw
# @FileName: test.py
# @Software: PyCharm
import math


class Point:
    def __init__(self, x, z, y):
        self.x = x
        self.z = z
        self.y = y
        self.coordinate = [x, z, y]


class Flat:  # 认为平面一定平行于XOZ平面
    def __init__(self, p1, p2, p3, p4):
        """
        四个点必须按相邻顺序传入

        """
        self.y = (p1.y + p2.y + p3.y + p4.y) / 4  # y坐标的平均值作为平板的y
        self.p1, self.p2, self.p3, self.p4 = p1, p2, p3, p4
        self.p1.y, self.p2.y, self.p3.y, self.p4.y = self.y, self.y, self.y, self.y

    def if_cover(self, p):
        # 用余弦定理判断给定点的投影是否在平板内
        def angle(p_a, p_b, p_c):
            a = math.sqrt((p_b.x - p_c.x) ** 2 + (p_b.y - p_c.y) ** 2)
            b = math.sqrt((p_c.x - p_a.x) ** 2 + (p_c.y - p_a.y) ** 2)
            c = math.sqrt((p_b.x - p_a.x) ** 2 + (p_b.y - p_a.y) ** 2)
            alpha = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
            return alpha

        pass


def angle(p_a, p_b, p_c):
    a = math.sqrt((p_b.x - p_c.x) ** 2 + (p_b.z - p_c.z) ** 2)
    b = math.sqrt((p_c.x - p_a.x) ** 2 + (p_c.z - p_a.z) ** 2)
    c = math.sqrt((p_b.x - p_a.x) ** 2 + (p_b.z - p_a.z) ** 2)
    print(a, b, c)
    alpha = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    return alpha


p1 = Point(0, 0, 0)
p2 = Point(3, 0, 0)
p3 = Point(3, 2, 0)
p4 = Point(0, 2, 0)

p = Point(2, 1, 0)

bete = angle(p, p1, p2) + angle(p, p2, p3) + angle(p, p3, p4) + angle(p, p4, p1)
if round(bete, 5) == round(math.pi*2, 5):
    print(round(bete, 5), round(math.pi*2, 5), "点的投影在平板范围内。")

else:
    print(round(bete, 5), round(math.pi*2, 5), "点的投影不在平板范围内。")

for name in ['bob', 'sue', 'joe']:
    print(name, n)
