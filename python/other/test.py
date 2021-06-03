# # i = 0
# for i in range(0, 5):
#     print("aaaa",i)
#     i += 10
#     print("bbbb",i)

# import random
# alist = [1,2,3,4,5]
# def randoms():
#     return 0.2
# random.shuffle(alist,randoms)
# print(alist)
# !/usr/bin/python3
from typing import List

# a = [1, 2, 3, [4, 5, 6]]
# b = a[:] # 与copy作用相同
# b[3].append(7)
# print("a:", a)
# print("b:", b)
# print("--------------------")
# b.append(8)
# print("a:", a)
# print("b:", b)


from collections import OrderedDict

t = OrderedDict()
for x in range(0, 10):
    t[x] = x
print(t)

from random import randint


def heapSort(nums: List[int]) -> List[int]:
    # build_heap
    for i in range(len(nums) - 1, -1, -1):
        max_heapify(nums, i, len(nums))
    # sort_heap
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


# print(Solution().sortArray([5, 4, 3, 2, 1]))
