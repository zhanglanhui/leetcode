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


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def randomized_partition(nums, low, high):
            if low >= high: return
            pivot = get_privot(nums, low, high)
            randomized_partition(nums, low, pivot - 1)
            randomized_partition(nums, pivot + 1, high)
            return

        def get_privot(nums, low, high):
            p = randint(low, high)
            nums[p], nums[high] = nums[high], nums[p]
            i = low
            for j in range(low, high):
                if nums[j] < nums[high]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        if not nums: return nums
        randomized_partition(nums, 0, len(nums) - 1)
        return nums


print(Solution().sortArray([5,4,3,2,1]))