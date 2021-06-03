# 给定一个二叉树，检查它是否是镜像对称的。
#
#  
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/symmetric-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1, root2):
            if (not root1 and not root2):
                return True
            if (not root1 and root2) or (not root2 and root1):
                return False
            if root1.val == root2.val and check(root1.left, root2.right) and check(root1.right, root2.left):
                return True
            return False

        return check(root, root)


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1, root2):
            tmp = [root1, root2]
            while tmp:
                l, r = tmp[0], tmp[1]
                tmp = tmp[2:]
                if not l and not r: continue
                if (not l and r) or (l and not r) or (l.val != r.val): return False
                tmp.extend([l.left, r.right, l.right, r.left])
            return True

        return check(root, root)
