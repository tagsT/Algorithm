# -*- coding: utf-8 -*-

"""
@author: tag
Created on 2018-03-22

"""

import random

"""
选择排序通过指针位上的数据和后面数据进行比较，把最小或最大的数放在最前
loop1 n次，n为列表长度
loop2 从loop1的递增位数i开始，因为最小或最大数已经在前面

"""


def selectSort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[j] < l[i]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l

def main():

    l = [random.randint(0,100) for x in range(10)]
    print(l)
    print(selectSort(l))

if __name__ == '__main__':
    main()
