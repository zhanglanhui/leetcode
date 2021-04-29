#!/usr/bin/python3
from typing import List
import functools


# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/container-with-most-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 暴力解法
#
# 双指针遍历所有可能情况计算最大值

class Solution1:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        if len(height) == 2:
            return min(height[0], height[1])
        p1, p2, max_area = 0, len(height) - 1, -1
        while p1 < p2:
            if height[p1] > height[p2]:
                max_area = max(max_area, (p2 - p1) * height[p2])
                p2 -= 1
            else:
                max_area = max(max_area, (p2 - p1) * height[p1])
                p1 += 1
        return max_area


print(Solution1().maxArea([4, 3, 2, 1, 4]))
