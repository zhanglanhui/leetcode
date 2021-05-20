#!/usr/bin/python3
from typing import List


# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 假设你总是可以到达数组的最后一个位置。
#
#  
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 动态规划
# 超时
class Solution1:
    def jump(self, nums: List[int]) -> int:
        def jump22(nums1: List[int], last) -> int:
            if len(nums1) <= 1: return -1
            if len(nums1) == 2: return 1 + last if nums1[0] >= 1 else -1
            if nums1[0] == 0: return -1
            step = len(nums1) - 1
            if nums1[0] >= step: return 1 + last
            ppp = min(nums1[0], len(nums1) - 1)
            ggg = list(filter(lambda x: x >= 0, [jump22(nums1[i::], last + 1) for i in range(1, ppp + 1)]))
            return min(ggg) if ggg else -1

        if len(nums) <= 1: return 0
        return jump22(nums, 0)


# 贪心
class Solution2:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1: return 0
        i, step, end = 0, 0, size - 1
        while True:
            step_len = max_tmp = 0
            for j in range(1, nums[i] + 1):
                if i + j >= size-1:
                    return step + 1
                if j + nums[j + i] > max_tmp:
                    max_tmp = j + nums[j + i]
                    step_len = j
            i += step_len
            step += 1
            if end <= i:
                break
        return step


print(Solution2().jump([2, 3, 1]))
