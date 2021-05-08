#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 选择排序提高了冒泡排序的性能，它每遍历一次列表只交换一次数据，即进行一次遍历时找 到最大的项，
# 完成遍历后，再把它换到正确的位置。和冒泡排序一样，第一次遍历后，最大的数 据项就已归位，
# 第二次遍历使次大项归位。这个过程持续进行，一共需要 n-1 次遍历来排好 n 个数 据，因为最后一个数据必须在第 n-1 次遍历之后才能归位。

# 选择排序
def selectionSort(nums):
    size = len(nums)
    for i in range(size):
        min_ind, min_val = i, nums[i]
        for j in range(i, size):
            if nums[j] < min_val:
                min_ind, min_val = j, nums[j]
        nums[i], nums[min_ind] = min_val, nums[i]
    return nums


l = generateRandomArray(100, 1, 1000)
selectionSort(l)
print(l)
testSort(selectionSort, l)
