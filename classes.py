#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2018-04-10  15:02
# @Author  : PengZhw

# @Software: PyCharm

import math


class Point:
    """
    一个点对象，只有坐标信息和刷新函数
    """

    def __init__(self, x: float, z: float, y: float):
        self.x = x
        self.z = z
        self.y = y
        self.coordinate = [self.x, self.y, self.z]

    def refresh(self):
        self.coordinate = [self.x, self.y, self.z]


class Flat:  # 认为平面一定平行于XOZ平面
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        """
        四个点必须按相邻顺序传入

        """
        self.y = (p1.y + p2.y + p3.y + p4.y) / 4  # y坐标的平均值作为平板的y
        self.p1, self.p2, self.p3, self.p4 = p1, p2, p3, p4
        self.p1.y, self.p2.y, self.p3.y, self.p4.y = self.y, self.y, self.y, self.y

    def tell_corner(self):
        self.p1.refresh()
        self.p2.refresh()
        self.p3.refresh()
        self.p4.refresh()
        print("平面的四个顶点分别是：", self.p1.coordinate, self.p2.coordinate, self.p3.coordinate, self.p4.coordinate)

    def if_cover(self, p):
        # 用余弦定理判断给定点的投影是否在平板内
        def angle(p_a, p_b, p_c):
            a = math.sqrt((p_b.x - p_c.x) ** 2 + (p_b.z - p_c.z) ** 2)
            b = math.sqrt((p_c.x - p_a.x) ** 2 + (p_c.z - p_a.z) ** 2)
            c = math.sqrt((p_b.x - p_a.x) ** 2 + (p_b.z - p_a.z) ** 2)
            if (b ** 2 + c ** 2 - a ** 2) / (2 * b * c) > 1:
                return math.acos(1)
            elif (b ** 2 + c ** 2 - a ** 2) / (2 * b * c) < -1:
                return math.acos(-1)
            alpha = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))

            return alpha

        bete = angle(p, self.p1, self.p2) + angle(p, self.p2, self.p3) + angle(p, self.p3, self.p4) + angle(p, self.p4,
                                                                                                            self.p1)
        if round(bete, 5) == round(math.pi * 2, 5):
            # print(round(bete, 5), round(math.pi * 2, 5))
            return True
        else:
            # print(round(bete, 5), round(math.pi * 2, 5))
            return False


class Box:  # 每N个石墨烯片层能得到N-1个Box实例，但有些情况下会舍弃某片层
    def __init__(self, flat_1: Flat, flat_2: Flat):
        """

        :param flat_1: y值小的平面
        :param flat_2: y值大的平面
        """
        if flat_1.y > flat_2.y:
            self.flat_1, self.flat_2 = flat_2, flat_1
        elif flat_1.y < flat_2.y:
            self.flat_1, self.flat_2 = flat_1, flat_2

    def if_inside(self, p):
        # print("\n读入点", p.coordinate, "...")
        if p.y > self.flat_2.y or p.y < self.flat_1.y:  # 如果点p的y坐标不在两片层之间，返回否
            # print("点", p.coordinate, "的y坐标不在两片层之间。")
            return False
        elif not self.flat_1.if_cover(p):  # 如果下平面没有覆盖到点p，返回否
            # print("下平面没有覆盖到点", p.coordinate, "。")
            return False

        elif not self.flat_2.if_cover(p):
            # print("上平面没有覆盖到点", p.coordinate, "。")
            return False
        # print("点", p.coordinate, "的y坐标在两片层之间，且投影被上下平面均覆盖到。")
        return True  # 否则就只能在两片层之间了咯


class GrapheneC(Point):
    def __init__(self, x, z, y, n, name):
        Point.__init__(self, x, z, y)
        self.n = n  # n是指这是第几片石墨烯里面的碳
        self.name = name  # 名字（pdb里面的总序号）


class CO2C(Point):
    def __init__(self, x, z, y, name, mol_n):
        Point.__init__(self, x, z, y)
        self.name = name  # 名字（pdb里面的总序号）
        self.mol_n = mol_n


class GraShp(Flat):
    def __init__(self, c1, c2, c3, c4):
        Flat.__init__(self, c1, c2, c3, c4)


def main():
    print("==========================================\n测试内容开始\n")
    grac = GrapheneC(0, 0, 0.2, 1, None)
    print(grac.coordinate)

    P1 = Point(0, 0, 0.2)
    P2 = Point(3, 0, -0.1)
    P3 = Point(3, 2, 0.1)
    P4 = Point(0, 2, 0)

    P5 = Point(1, 0, 2.8)
    P6 = Point(2, 0, 3.1)
    P7 = Point(2, 3, 3.4)
    P8 = Point(0, 3, 2.9)

    FLAT_1 = Flat(P1, P2, P3, P4)
    FLAT_1.tell_corner()

    FLAT_2 = Flat(P5, P6, P7, P8)
    FLAT_2.tell_corner()

    box = Box(FLAT_1, FLAT_2)
    result = box.if_inside(Point(1.5, 1, 2))
    print(result)

    result_1 = box.if_inside(Point(0.1, 0, 0))
    print(result_1)
    print("\n测试内容结束\n==========================================")


if __name__ == '__main__':
    main()
