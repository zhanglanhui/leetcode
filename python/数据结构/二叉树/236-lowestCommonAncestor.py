# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
#  
#
# 示例 1：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return  # 1.
        if not left: return right  # 3.
        if not right: return left  # 4.
        return root  # 2. if left and right:


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        father = dict()
        other = dict()

        def pre_order(root):
            if not root: return
            pre_order(root.left)
            pre_order(root.right)
            if root.left: father[root.left.val] = root
            if root.right: father[root.right.val] = root
            return

        pre_order(root)
        ppp = p
        while ppp != root:
            other[ppp] = True
            ppp = father[ppp.val]
        other[root] = True
        qqq = q
        while qqq != root:
            if qqq in other:
                return qqq
            qqq = father[qqq.val]
        return root


# 递归法
class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def commonAncestor(r):
            if not r or r == p or r == q: return r
            left = commonAncestor(r.left)
            right = commonAncestor(r.right)
            if left and right:
                return r
            return left if left else right

        return commonAncestor(root)


# hash
class Solution4:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        father_hash = dict()
        while stack:
            stack_next = []
            for x in stack:
                if x.left:
                    stack_next.append(x.left)
                    father_hash[x.left]=x
                if x.right:
                    stack_next.append(x.right)
                    father_hash[x.right] = x
            stack=stack_next
        tmp_q=q
        qList=set()
        while tmp_q:
            qList.add(tmp_q)
            tmp_q=father_hash.get(tmp_q,None)
        tmp_p = p
        while tmp_p:
            if tmp_p in qList: return tmp_p
            tmp_p = father_hash.get(tmp_p,None)
        return None



