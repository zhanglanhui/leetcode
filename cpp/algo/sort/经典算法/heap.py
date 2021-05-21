#!/usr/bin/python3
from typing import List
import functools
from utils import *


def heapSort(nums: List[int]) -> List[int]:
    # build_heap
    for i in range(len(nums) - 1, -1, -1):
        max_heapify(nums, i, len(nums))
    for i in range(len(nums) - 1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, 0, i)
    return nums


def max_heapify(heap, root, heap_len):
    p = root
    while p * 2 + 1 < heap_len:
        l, r = p * 2 + 1, p * 2 + 2
        if heap_len <= r or heap[r] < heap[l]:
            _next = l
        else:
            _next = r
        if heap[p] < heap[_next]:
            heap[p], heap[_next] = heap[_next], heap[p]
            p = _next
        else:
            break


l = generateRandomArray(1000, 1, 1000)
print("before sort:", l)
ret = heapSort(l)
print("sorted:", ret)
testSort(heapSort, l)
