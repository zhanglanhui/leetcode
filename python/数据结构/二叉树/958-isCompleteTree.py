#
# 给定一个二叉树，确定它是否是一个完全二叉树。
#
# 百度百科中对完全二叉树的定义如下：
#
# 若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）
#
#  
#
# 示例 1：
#
#
#
# 输入：[1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        stack = [(root, 1)]
        i = 0
        while i < len(stack):
            r, ind = stack[i]
            i += 1
            if r: stack.extend([(r.left, 2 * ind - 1), (r.right, 2 * ind)])
        return stack[-1][-1] == len(stack)
