#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 归并排序是一种递归算法，它持续地将一个列表分成两半。如果列表是空的或者 只有一个元素，那么根据定义，
# 它就被排序好了（最基本的情况）。如果列表里的元素超过一个，我们就把列表拆分，然后分别对两个部分调用递归排序。
# 一旦这两个部分被排序好了，然后就可以对这两部分数列进行归并了。归并是这样一个过程：
# 把两个排序好了的列表结合在一起组合成一个单一的有序的新列表。有自顶向下（递归法）和自底向上的两种实现方法。

# 自顶向下（递归法）方法实现
# 归并排序
# TODO:注意：这里进行小的优化，当数列的长度小于等于15的时候，我们一般认为数列此时基本有序，这时候采用直接插入排序非常快。
def mergeSort(alist):
    n = len(alist)
    __mergeSort(alist, 0, n - 1)
    return alist


# 对arr[l...r]的范围进行排序
def __mergeSort(alist, start, end):
    # 当数列的大小比较小的时候，数列近乎有序的概率较大
    if (end - start <= 15):
        insertionSortHelp(alist, start, end)
        return

    if start >= end:
        return
    # 存在风险，start+end可能越界
    mid = (start + end) // 2
    # mid = start + (end - start) // 2
    __mergeSort(alist, start, mid)
    __mergeSort(alist, mid + 1, end)
    # 优化
    if alist[mid] > alist[mid + 1]:
        merge(alist, start, mid, end)


# 合并有序数列alist[start....mid] 和 alist[mid+1...end]，使之成为有序数列
def merge(alist, start, mid, end):
    # 复制一份
    blist = alist[start:end + 1]
    l = start
    k = mid + 1
    pos = start

    while pos <= end:
        if (l > mid):
            alist[pos] = blist[k - start]
            k += 1
        elif (k > end):
            alist[pos] = blist[l - start]
            l += 1
        elif blist[l - start] <= blist[k - start]:
            alist[pos] = blist[l - start]
            l += 1
        else:
            alist[pos] = blist[k - start]
            k += 1
        pos += 1


def insertionSortHelp(alist, l, r):
    for i in range(l + 1, r + 1):
        currentvalue = alist[i]
        position = i
        while alist[position - 1] > currentvalue and position > l:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentvalue
    return alist


# ---------------------------------------------------------
# 自底向上（非递归法）方法
# 自底向上的归并算法
def mergeBU(alist):
    n = len(alist)
    # 表示归并的大小
    size = 1
    while size <= n:
        for i in range(0, n - size, size + size):
            merge(alist, i, i + size - 1, min(i + size + size - 1, n - 1))
        size += size
    return alist


l = generateRandomArray(100, 1, 1000)
print("before sort:", l)
ret = mergeBU(l)
print("sorted:", ret)
testSort(mergeBU, l)
