#!/usr/bin/python3
from typing import List
import functools

# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
#
#  
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 示例 2：
#
# 输入：root = []
# 输出：[]
# 示例 3：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        if not root:
            return []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res