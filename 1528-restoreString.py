#!/usr/bin/python3
from typing import List
import functools


# 给你一个字符串 s 和一个 长度相同 的整数数组 indices 。
#
# 请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。
#
# 返回重新排列后的字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shuffle-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution1:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join(map(str,[indices[ind] for ind,x in enumerate(s)]))

print(Solution1().restoreString("codeleet",[4,5,6,7,0,2,1,3]))