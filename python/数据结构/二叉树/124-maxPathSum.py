# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#  
#
# 示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 示例 2：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def post_path(head):
            if not head: return 0
            left = max(0, post_path(head.left))
            right = max(0, post_path(head.right))
            self.ans = max(self.ans, head.val + left + right)
            return head.val + max(left, right)

        if not root:  return 0
        self.ans = -1000000
        post_path(root)
        return self.ans


class Solution2:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float('inf')

        def dfs(r: TreeNode):
            if not r: return 0
            left = max(dfs(r.left), 0)
            right = max(dfs(r.right), 0)
            self.ans = max(self.ans, left + right + r.val)
            return r.val + max(left, right)

        dfs(root)
        return int(self.ans)
