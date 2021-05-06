#!/usr/bin/python3
from typing import List
import functools
from utils import *


def max_heapify(heap, root, heap_len):
    p = root
    while p * 2 + 1 < heap_len:
        l, r = p * 2 + 1, p * 2 + 2
        if heap_len <= r or heap[r] < heap[l]:
            nex = l
        else:
            nex = r
        if heap[p] < heap[nex]:
            heap[p], heap[nex] = heap[nex], heap[p]
            p = nex
        else:
            break


def build_heap(heap):
    for i in range(len(heap) - 1, -1, -1):
        max_heapify(heap, i, len(heap))


def heap_sort(nums):
    build_heap(nums)
    for i in range(len(nums) - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, 0, i)


def sortArray(nums: List[int]) -> List[int]:
    heap_sort(nums)
    return nums


l = generateRandomArray(10, 1, 1000)
print("before sort:", l)
ret = sortArray(l)
print("sorted:", ret)
testSort(sortArray, l)
