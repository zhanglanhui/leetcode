# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_root(r: TreeNode):
            if not r: return 0
            return r.val + rob_not_root(r.left) + rob_not_root(r.right)

        def rob_not_root(r: TreeNode):
            if not r: return 0
            return max(rob_not_root(r.left), rob_root(r.left)) + max(rob_not_root(r.right), rob_root(r.right))

        if not root: return 0
        return max(rob_root(root), rob_not_root(root))
