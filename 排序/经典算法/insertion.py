#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 插入排序的算法复杂度仍然是 O(n^2)，但其工作原理稍有不同。
# 它总是保持一个位置靠前的 已排好的子表，然后每一个新的数据项被 “插入” 到前边的子表里，
# 排好的子表增加一项。我们认为只含有一个数据项的列表是已经排好的。
# 每排后面一个数据（从 1 开始到 n-1），这 个的数据会和已排好子表中的数据比较。
# 比较时，我们把之前已经排好的列表中比这个数据大的移到它的右边。
# 当子表数据小于当前数据，或者当前数据已经和子表的所有数据比较了时，就可 以在此处插入当前数据项。


# 插入排序(自己实现的)
def _insert(l, val):
    if (not l) or val < l[0]:
        return [val] + l
    for i in range(0, len(l) - 1):
        if l[i] < val <= l[i + 1]:
            return l[:i + 1] + [val] + l[i + 1:]
    return l + [val]


def insertionSort(alist):
    ret = []
    for x in alist:
        ret = _insert(ret, x)
    return ret


l = generateRandomArray(10, 1, 1000)
print("before sort:", l)
ret = insertionSort(l)
print("sorted:", ret)
testSort(insertionSort, l)
