#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 归并排序是一种递归算法，它持续地将一个列表分成两半。如果列表是空的或者 只有一个元素，那么根据定义，
# 它就被排序好了（最基本的情况）。如果列表里的元素超过一个，我们就把列表拆分，然后分别对两个部分调用递归排序。
# 一旦这两个部分被排序好了，然后就可以对这两部分数列进行归并了。归并是这样一个过程：
# 把两个排序好了的列表结合在一起组合成一个单一的有序的新列表。有自顶向下（递归法）和自底向上的两种实现方法。

# 合并有序数列alist[start....mid] 和 alist[mid+1...end]，使之成为有序数列
def merge(nums, l, mid, r):
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


# -----------------------------------
# 自顶向下（递归法）方法实现
# 归并排序
def mergeSort(nums):
    merge_sort(nums, 0, len(nums) - 1)
    return nums


def merge_sort(nums, l, r):
    if l == r:
        return
    mid = (l + r) // 2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)
    merge(nums, l, mid, r)


# ---------------------------------------------------------
# 自底向上的归并算法（非递归法）
def mergeSortBU(nums):
    size = 1  # 表示归并的大小
    while size <= len(nums):
        for i in range(0, len(nums) - size, 2 * size):
            merge(nums, i, i + size - 1, min(i + 2 * size - 1, len(nums) - 1))
        size += size
    return nums


l = generateRandomArray(100, 1, 1000)
print("before sort:", l)
ret = mergeSortBU(l)
print("sorted:", ret)
testSort(mergeSortBU, l)
