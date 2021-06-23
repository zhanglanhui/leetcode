#!/usr/bin/python
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] <= arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

print(Solution().peakIndexInMountainArray([0,2,1,0]))