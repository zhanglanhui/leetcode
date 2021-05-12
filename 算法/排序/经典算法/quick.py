#!/usr/bin/python3
from typing import List
import functools
from utils import *


# 算法步骤
# 从数列中挑出一个元素，称为"基准"（pivot）。
# 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
# TODO:标准代码
def quickSort(nums):
    randomized_quicksort(nums, 0, len(nums) - 1)
    return nums


def randomized_quicksort(nums, low, high):
    if low >= high:
        return
    pivot = randomized_partition(nums, low, high)
    randomized_quicksort(nums, low, pivot - 1)
    randomized_quicksort(nums, pivot + 1, high)


# 在nums[l...r]中寻找j,使得nums[l...j] <= nums[l], nums[j+1...r] >nums[l]
def randomized_partition(nums, low, high):
    pivot = randint(low, high)
    nums[pivot], nums[high] = nums[high], nums[pivot]
    i = low
    for j in range(low, high):
        if nums[j] < nums[high]:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i


# 快速排序一些可以优化的点:
# 当数列近乎有序的时，由于每次选取的都是第一个数，所以造成数列分割的极其不等，此时快排蜕化成O(n^2) 的算法， 此时只要随机选取基准点即可
# 当数列中包含大量的重复元素的时候，这一版的代码也会造成"分割不等“的问题，此时需要将重复元素均匀的分散的自数列旁
# 使用三路快排
l = generateRandomArray(10, 1, 1000)
# print(l)
# print(partition(l, 1, 5))
# print(l)
print("before sort:", l)
ret = quickSort(l)
print("sorted:", ret)
testSort(quickSort, l)
