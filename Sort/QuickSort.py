# -*- coding: utf-8 -*-

"""
@author: tag
Created on 2018-03-22

"""

import random

"""
快速排序通过分治法进行区域排序
首先选取一个值，比值大的放在右边，比值小的放左边
递归左右两个区域，直到指针重叠

时间复杂度O(n log n)
空间复杂度O(log n)

"""

class QuickSort:
    l = None

    def __init__(self, l):
        self.l = l

    def run(self):
        self.divide(0, len(self.l)-1)

    def divide(self, left, right):
        if type(left) != int or type(right) != int:
            raise Exception("Para error::left or right must be Integer.")
        if left >= right:
            return
        keyvalue = self.l[left]
        low = left
        high = right
        while(left < right):
            while(left<right and self.l[right]>keyvalue):
                right -= 1
            self.l[left] = self.l[right]
            while(left<right and self.l[left]<keyvalue):
                left += 1
            self.l[right] = self.l[left]
        self.l[left] = keyvalue
        self.divide(low, left-1)
        self.divide(right+1, high)




def main():
    l = [random.randint(0,100) for x in range(10)]
    print(l)
    # print(quickSort(l))
    quickSort = QuickSort(l)
    quickSort.run()
    print(quickSort.l)

if __name__ == '__main__':
    main()
