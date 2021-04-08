#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 算法步骤
# 从数列中挑出一个元素，称为"基准"（pivot）。
# 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
def quickSort(alist):
    n = len(alist)
    __quickSort(alist, 0, n - 1)
    return alist


def __quickSort(alist, l, r):
    # 当数列的大小比较小的时候，数列近乎有序的概率较大
    # if (r - l <= 15):
    #     insertionSortHelp(alist, l, r)
    #     return
    if l >= r:
        return
    # p = partition(alist, l, r)
    p = partition(alist, l, r)
    __quickSort(alist, l, p - 1)
    __quickSort(alist, p + 1, r)


# 在alist[l...r]中寻找j,使得alist[l...j] <= alist[l], alist[j+1...r] >alist[l]
def partition(alist, l, r):
    pos = randint(l, r)
    alist[pos], alist[l] = alist[l], alist[pos]
    v = alist[l]
    j = l
    i = l + 1
    while i <= r:
        if alist[i] <= v:
            alist[j + 1], alist[i] = alist[i], alist[j + 1]
            j += 1
        i += 1
    alist[l], alist[j] = alist[j], alist[l]
    return j


# 快速排序一些可以优化的点:
# 当数列近乎有序的时，由于每次选取的都是第一个数，所以造成数列分割的极其不等，此时快排蜕化成O(n^2) 的算法， 此时只要随机选取基准点即可
# 当数列中包含大量的重复元素的时候，这一版的代码也会造成"分割不等“的问题，此时需要将重复元素均匀的分散的自数列旁
# 使用三路快排
l = generateRandomArray(100, 1, 1000)
print("before sort:", l)
ret = quickSort(l)
print("sorted:", ret)
testSort(quickSort, l)
