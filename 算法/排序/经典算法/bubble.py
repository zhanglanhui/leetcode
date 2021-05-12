#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 冒泡排序要对一个列表多次重复遍历。它要比较相邻的两项，并且交换顺序排错的项。每对 列表实行一次遍历，
# 就有一个最大项排在了正确的位置。大体上讲，列表的每一个数据项都会在 其相应的位置 “冒泡”。
# 如果列表有 n 项，第一次遍历就要比较 n-1 对数据。需要注意，
# 一旦列 表中最大(按照规定的原则定义大小)的数据是所比较的数据对中的一个，它就会沿着列表一直 后移，直到这次遍历结束。
def bubble(l):
    if len(l) < 2:
        return l
    flag, first = 0, 1
    while first or flag:
        first, flag = 0, 0
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                flag = 1
    return l


def bubbleSort2(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 因为冒泡排序必须要在最终位置找到之前不断交换数据项，所以它经常被认为是最低效的排 序方法。
# 这些 “浪费式” 的交换操作消耗了许多时间。但是，由于冒泡排序要遍历整个未排好的 部分，
# 它可以做一些大多数排序方法做不到的事。尤其是如果在整个排序过程中没有交换，
# 我们就可断定列表已经排好。因此可改良冒泡排序，使其在已知列表排好的情况下提前结束。
# 这就是说，如果一个列表只需要几次遍历就可排好，冒泡排序就占有优势：它可以在发现列表已排好时立刻结束。
# TODO:标准代码
def bubbleSort3(nums):
    for i in range(len(nums) - 1, 0, -1):
        exchange = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                exchange = True
        if not exchange:
            break
    return nums


def bubbleSort4(arr):
    for i in range(0, len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


l = generateRandomArray(100, 1, 1000)
bubbleSort2(l)
print(l)
testSort(bubbleSort3, l)
