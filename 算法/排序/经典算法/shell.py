#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 希尔排序有时又叫做 “缩小间隔排序”，它以插入排序为基础，将原来要排序的列表划分为一些子列表，
# 再对每一个子列表执行插入排序，从而实现对插入排序性能的改进。划分子列的特定方法是希尔排序的关键。
# 我们并不是将原始列表分成含有连续元素的子列，而是确定一个划分列表的增量 “i”，这个i更准确地说，是划分的间隔。
# 然后把每间隔为i的所有元素选出来组成子列表，然后对每个子序列进行插入排序，最后当 i=1 时，对整体进行一次直接插入排序。

# 希尔排序(缩小增量排序)
def shellSort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            gapInsetionSort(alist, i, gap)
        gap = gap // 2
    return alist


# start子数列开始的起始位置， gap表示间隔
def gapInsetionSort(alist, startpos, gap):
    # 希尔排序的辅助函数
    for i in range(startpos + gap, len(alist), gap):
        position = i
        currentvalue = alist[i]
        while position > startpos and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


l = generateRandomArray(10, 1, 1000)
print("before sort:", l)
ret = shellSort(l)
print("sorted:", ret)
testSort(shellSort, l)