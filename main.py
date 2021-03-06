#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2018-04-11  15:34
# @Author  : PengZhw
# @Software: PyCharm
import os
from typing import List
from for_simulation.classes import *
from sys import argv
from for_simulation.classes import Point, Flat
from os import path
import csv
import re

"""

"""
# 自身文件名，数据文件路径，石墨烯规格，输出文件名
self = argv[0]
FILE_PATH = argv[1]
FILE_PREFIX = argv[2]
SIZE = argv[3]
OUTPUT_NAME = argv[4]


# 列表：所有待处理的文件，用re来获取
FILE_LIST = []
for file in os.listdir(FILE_PATH):
    match = re.match(FILE_PREFIX + '[01][0-9]\.txt', file)
    if str(match) != 'None':
        print(match.group())
        FILE_LIST.append(FILE_PATH + match.group())
print(FILE_LIST)

# 测试
# main()

# 定义石墨烯片层列表
GRAPHENES: List[Flat] = []

# 定义石墨烯片层间隙列表
GRABOXES: List[Box] = []

# 定义碳原子列表
GRACS: list = []

# 定义二氧化碳列表
CO2CS = []

# 记录溶剂分子的个数
SOLV_NUM = []


def read_data(file_path):
    with open(file_path, 'r') as FILE_IN:
        file_lines = FILE_IN.readlines()

    s = 1
    sheep_c_list = []

    for line in file_lines:
        sl = line.split()  # sl = sl，切割后的一行，是一个list

        # 将石墨烯碳原子的信息存入list里面
        if (sl[0] == 'ATOM') and (sl[2] == 'C'):
            if int(sl[4]) == s:
                sheep_c_list.append(
                    GrapheneC(float(sl[5]), float(sl[7]), float(sl[6]), s, float(sl[1])))  # x, z, y, 第几层, 名字（pdb里面的总序号）

            elif int(sl[4]) > s:
                s = int(sl[4])
                GRACS.append(sheep_c_list)
                sheep_c_list = []
        elif (sl[0] == 'ATOM') and (sl[2] != 'C'):
            GRACS.append(sheep_c_list)
            break

    for line in file_lines:
        sl = line.split()  # sl = sl，切割后的一行，是一个list

        # 将二氧化碳碳原子的信息存入list里面
        if (sl[0] == 'ATOM') and (sl[2] == 'CO'):
            CO2CS.append(CO2C(float(sl[5]), float(sl[7]), float(sl[6]), float(sl[1]), int(sl[4])))

    print("石墨烯片层数：", len(GRACS))
    print("第一片石墨烯上第一个碳原子坐标[x, z, y] =", GRACS[0][0].coordinate)

    print("二氧化碳的个数：", len(CO2CS))
    print("第二个二氧化碳中碳原子坐标[x, z, y] =", CO2CS[1].coordinate)

# 石墨烯片层中六边形的边长为1.451A
L = 1.451


# print(type(GRACS[1][1]))


def corner_3(cl: list) -> list:
    """
    接收单层石墨烯的碳原子列表，计算得到四个Point对象
    :param cl: 单层石墨烯的碳原子列表，相当于前面的{list}sheep_c_list、{list}GRACS[X]
    :return: 四个Point对象的list
    """
    k = len(cl)  # 这一层有k个碳原子
    c3 = cl[2]  # 第3个碳原子
    c8 = cl[7]  # 第8个碳原子
    cn3 = cl[k - 3]  # 倒数第3个碳原子
    cn8 = cl[k - 8]  # 倒数第8个碳原子
    pa = Point(c3.x - (c8.x - c3.x) / 2, c3.z - (c8.z - c3.z) / 2, c3.y - (c8.y - c3.y) / 2)
    pb = Point(c8.x - (c3.x - c8.x) / 8, c8.z - (c3.z - c8.z) / 8, c8.y - (c3.y - c8.y) / 8)
    pc = Point(cn3.x - (cn8.x - cn3.x) / 2, cn3.z - (cn8.z - cn3.z) / 2, cn3.y - (cn8.y - cn3.y) / 2)
    pd = Point(cn8.x - (cn3.x - cn8.x) / 8, cn8.z - (cn3.z - cn8.z) / 8, cn8.y - (cn3.y - cn8.y) / 8)
    point_list = [pa, pb, pc, pd]  # 用来盛放四个角点并返回
    return point_list


def corner_5(cl: list) -> list:
    """
    接收单层石墨烯的碳原子列表，计算得到四个Point对象
    :param cl: 单层石墨烯的碳原子列表，相当于前面的{list}sheep_c_list、{list}GRACS[X]
    :return: 四个Point对象的list
    """
    k = len(cl)  # 这一层有k个碳原子
    c3 = cl[2]  # 第3个碳原子
    c16 = cl[15]  # 第16个碳原子
    cn3 = cl[k - 3]  # 倒数第3个碳原子
    cn16 = cl[k - 16]  # 倒数第16个碳原子
    pa = Point(c3.x - (c16.x - c3.x) / 5, c3.z - (c16.z - c3.z) / 5, c3.y - (c16.y - c3.y) / 5)
    pb = Point(c16.x - (c3.x - c16.x) / 20, c16.z - (c3.z - c16.z) / 20, c16.y - (c3.y - c16.y) / 20)
    pc = Point(cn3.x - (cn16.x - cn3.x) / 5, cn3.z - (cn16.z - cn3.z) / 5, cn3.y - (cn16.y - cn3.y) / 5)
    pd = Point(cn16.x - (cn3.x - cn16.x) / 20, cn16.z - (cn3.z - cn16.z) / 20, cn16.y - (cn3.y - cn16.y) / 20)
    point_list = [pa, pb, pc, pd]  # 用来盛放四个角点并返回
    return point_list


def corner_10(cl: list) -> list:
    """
    接收单层石墨烯的碳原子列表，计算得到四个Point对象
    :param cl: 单层石墨烯的碳原子列表，相当于前面的{list}sheep_c_list、{list}GRACS[X]
    :return: 四个Point对象的list
    """
    k = len(cl)  # 这一层有k个碳原子
    c3 = cl[2]  # 第3个碳原子
    c36 = cl[35]  # 第36个碳原子
    cn3 = cl[k - 3]  # 倒数第3个碳原子
    cn36 = cl[k - 36]  # 倒数第36个碳原子
    pa = Point(c3.x - (c36.x - c3.x) / 12.5, c3.z - (c36.z - c3.z) / 12.5, c3.y - (c36.y - c3.y) / 12.5)
    pb = Point(c36.x - (c3.x - c36.x) / 50, c36.z - (c3.z - c36.z) / 50, c36.y - (c3.y - c36.y) / 50)
    pc = Point(cn3.x - (cn36.x - cn3.x) / 12.5, cn3.z - (cn36.z - cn3.z) / 12.5, cn3.y - (cn36.y - cn3.y) / 12.5)
    pd = Point(cn36.x - (cn3.x - cn36.x) / 50, cn36.z - (cn3.z - cn36.z) / 50, cn36.y - (cn3.y - cn36.y) / 50)
    point_list = [pa, pb, pc, pd]  # 用来盛放四个角点并返回
    return point_list


corner_list: list = []  # {list}corner_list是二维list，第一维是几个石墨烯片层，第二维是每一层的四个角点Point对象


def read_3():
    for i in range(len(GRACS)):
        l: List[Point] = corner_3(GRACS[i])
        corner_list.append(l)
    # print('a')


def read_5():
    for i in range(len(GRACS)):
        l: List[Point] = corner_5(GRACS[i])
        corner_list.append(l)
    # print('a')


def read_10():
    for i in range(len(GRACS)):
        l: List[Point] = corner_10(GRACS[i])
        corner_list.append(l)
    # print('a')


read_data(FILE_PATH + 'npt02-d-55-6-6.pdb')


if SIZE == '3':
    read_3()
elif SIZE == '5':
    read_5()
elif SIZE == '10':
    read_10()
else:
    print("错误: 没有正确输入石墨烯尺寸参数。")

# print("第一层石墨烯有%d个碳原子" % len(GRACS[0]))

"""
for i in range(len(corner_list)):
    for j in range(4):
        print(corner_list[i][j].coordinate)
"""
for i in range(len(corner_list)):
    GRAPHENES.append(Flat(corner_list[i][0], corner_list[i][1], corner_list[i][2], corner_list[i][3]))

print(len(GRAPHENES))
# GRAPHENES[0].tell_corner()

outlines = []

for i in range(len(GRAPHENES) - 1):
    GRABOXES.append(Box(GRAPHENES[i], GRAPHENES[i + 1]))
    print("\r第%d、%d层石墨烯构成了一个盒子。" % (i + 1, i + 2))
    outlines.append("\r\r\r[  Box%d  ]" % (i + 1))
    outlines.append("\r#第%d、%d层石墨烯构成的一个盒子。" % (i + 1, i + 2))

    outlines.append("\r%12s%12s%12s%12s%12s"
                    % ('an', 'rn', 'x', 'y', 'z'))
    n = 0
    for j in range(len(CO2CS)):
        if GRABOXES[i].if_inside(CO2CS[j]):
            n += 1
            print("原子序号%d，残基序号%d，坐标[x, z, y] = %s。"
                  % (CO2CS[j].name,
                     CO2CS[j].mol_n,
                     str(CO2CS[j].coordinate)))

            outlines.append("\r%12d%12d%12.3f%12.3f%12.3f"
                            % (CO2CS[j].name,
                               CO2CS[j].mol_n,
                               CO2CS[j].x,
                               CO2CS[j].y,
                               CO2CS[j].z))
    outlines[-n - 2] = '\r#总溶剂分子数%12s' % str(n) + outlines[-n - 2]
    SOLV_NUM.append(n)

with open(OUTPUT_NAME, "w+") as FILE_OUT:
    FILE_OUT.writelines(outlines)
    print("成功输出文件%s" % OUTPUT_NAME, path.isfile(OUTPUT_NAME))

with open(OUTPUT_NAME, 'r') as f:
    print(f.read(), os.getcwd())

print(SOLV_NUM)
with open(r'test.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(SOLV_NUM)
