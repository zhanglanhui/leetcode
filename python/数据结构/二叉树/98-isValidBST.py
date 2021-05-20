#!/usr/bin/python3
from typing import List
import functools


# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(rot, min_num, max_num, key, is_left):
            if not rot: return True
            if rot.val >= max_num or \
                    rot.val <= min_num or \
                    (is_left and rot.val >= key) or \
                    (not is_left and rot.val <= key):
                return False
            return valid(rot.left, min_num, min(max_num, rot.val), rot.val, True) and \
                   valid(rot.right, max(min_num, rot.val), max_num, rot.val, False)

        if not root: return True
        return valid(root, -float('inf'), float('inf'), float('inf'), True)
