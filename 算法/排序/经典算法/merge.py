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
def mergeSort(nums):
    n = len(nums)
    __mergeSort(nums, 0, n - 1)
    return nums


# 对arr[l...r]的范围进行排序
def __mergeSort(nums, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    __mergeSort(nums, l, mid)
    __mergeSort(nums, mid + 1, r)
    tmp = []
    i, j = l, mid + 1
    while i <= mid or j <= r:
        if i > mid or (j <= r and nums[j] < nums[i]):
            tmp.append(nums[j])
            j += 1
        else:
            tmp.append(nums[i])
            i += 1
    nums[l: r + 1] = tmp


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
ret = mergeSort(l)
print("sorted:", ret)
testSort(mergeSort, l)
