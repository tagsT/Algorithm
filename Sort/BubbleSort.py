# -*- coding: utf-8 -*-

"""
@author: tag
Created on 2018-03-22

"""

import random


"""
冒泡排序通过比较前后两个数的大小，把最大或最小的数放在最后
loop1 n次，n为列表长度
loop2 n-1-i次，i为loop1的递增位数，因为最大或最小的数在上一轮循环已经放到最后


"""


def bubbleSort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j+1] < l[j]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l

def main():

    l = [random.randint(0,100) for x in range(10)]
    print(l)
    print(bubbleSort(l))

if __name__ == '__main__':
    main()
