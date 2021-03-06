# 226. 翻转二叉树
# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        if root.right is None and root.left is None:
            return root
        left, right = root.left, root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root
