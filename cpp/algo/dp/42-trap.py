#!/usr/bin/python3
from typing import List


# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 暴力解法
class Solution1:
    def trap(self, height: List[int]) -> int:
        def get_left_right_max(pos):
            if pos == 0 or pos == len(height) - 1:
                return 0, 0
            return max(height[:pos]), max(height[pos + 1:])

        ans = 0
        for i in range(len(height)):
            left_max, right_max = get_left_right_max(i)
            if left_max > 0 and right_max > 0:
                ans += max(min(left_max, right_max) - height[i], 0)
        return ans


# dp
class Solution2:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        max_num = 0
        for i in range(len(height)):
            max_num = max(height[i], max_num)
            left_max.append(max_num)
        max_num = 0
        for i in range(len(height) - 1, -1, -1):
            max_num = max(height[i], max_num)
            right_max.append(max_num)
        right_max = right_max[::-1]
        ans = 0
        for i in range(1, len(height) - 1):
            ans += max(min(left_max[i], right_max[i]) - height[i], 0)
        return ans


# 单调栈
class Solution3:
    def trap(self, height: List[int]) -> int:
        stack, ans = [], 0
        for i, num in enumerate(height):
            if num == 0: continue
            last_height = 0
            while stack and num >= height[stack[-1]]:
                ans += (i - stack[-1] - 1) * (height[stack[-1]] - last_height)
                last_height = max(last_height, height[stack[-1]])
                stack.pop()
            if not stack or num < height[stack[-1]]:
                if stack: ans += (i - stack[-1] - 1) * (num - last_height)
                stack.append(i)
        return ans


print(Solution3().trap([4, 2, 0, 3, 2, 5]))
