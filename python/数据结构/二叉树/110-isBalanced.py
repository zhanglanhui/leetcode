# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
#
#  
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/balanced-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def ssss(rrr):
            if not rrr: return 0, True
            left, bbb1 = ssss(rrr.left)
            right, bbb2 = ssss(rrr.right)
            if not bbb1 or not bbb2 or abs(left - right) > 1:
                return 0, False
            return max(left, right) + 1, True

        _, f = ssss(rrr=root)
        return f
