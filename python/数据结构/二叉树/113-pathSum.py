#!/usr/bin/python3
from typing import List
import functools


# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#
#  
#
# 示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
# 示例 2：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(rrr: TreeNode, tmp):
            if not rrr:
                return
            if (not rrr.right and not rrr.left):
                if sum(tmp) + rrr.val == targetSum:
                    tmp.append(rrr.val)
                    ans.append(tmp[:])
                return
            tmp.append(rrr.val)
            dfs(rrr.left, tmp[:])
            dfs(rrr.right, tmp[:])
            return

        dfs(root, [])
        return ans
