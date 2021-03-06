#!/usr/bin/python3
from typing import List
import functools


# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
#  
#
# 示例 1：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：
#
# 输入：nums = [1], target = 0
# 输出：-1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target: return mid
            if nums[l] == target: return l
            if nums[r] == target: return r
            if nums[l] <= nums[r]:
                if nums[mid] < target: l = mid + 1
                if nums[mid] > target: r = mid - 1
            else:
                if nums[mid] < target:
                    if nums[r] > target:
                        l = mid + 1
                    elif nums[l] > target and nums[r] < target:
                        return -1
                    elif nums[l] < target and nums[r] < target:
                        if nums[mid] >= nums[l]:
                            l = mid + 1
                        if nums[mid] <= nums[r]:
                            r = mid - 1
                if nums[mid] > target:
                    if nums[r] > target:
                        if nums[mid] >= nums[l]:
                            l = mid + 1
                        if nums[mid] <= nums[r]:
                            r = mid - 1
                    elif nums[l] > target and nums[r] < target:
                        return -1
                    elif nums[l] < target and nums[r] < target:
                        r = mid - 1
        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target: return mid
            if nums[l] == target: return l
            if nums[r] == target: return r
            if nums[l] <= nums[r]:
                if nums[mid] < target: l = mid + 1
                if nums[mid] > target: r = mid - 1
            else:
                if nums[l] < target:
                    if nums[mid] < target and nums[mid] >= nums[l]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    if (nums[mid] > target and nums[mid] <= nums[r]):
                        r = mid - 1
                    else:
                        l = mid + 1
        return -1


class Solution3:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left, right = 0, size - 1
        while left <=  right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            elif nums[mid] > target:
                if nums[mid] < nums[right] or (target > nums[left]):
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                if nums[left] <= nums[mid] or target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


print(Solution3().search([1], 1))
