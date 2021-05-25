# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(r: TreeNode, tmp):
            def sumsss(tmp):
                res = 0
                for i, x in enumerate(tmp[::-1]):
                    res += (10 ** i) * x
                return res

            if not r.left and not r.right:
                tmp.append(r.val)
                self.ans += sumsss(tmp)
                return
            tmp1 = tmp[:]
            tmp2 = tmp[:]
            tmp1.append(r.val)
            tmp2.append(r.val)
            if r.left: dfs(r.left, tmp1)
            if r.right: dfs(r.right, tmp2)
            tmp1.pop()
            tmp2.pop()
            return

        dfs(root, [])
        return self.ans
