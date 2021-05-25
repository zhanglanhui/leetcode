# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # if not root: return 0
        # stack = [root]
        # ans = 1
        # while stack:
        #     tmp = []
        #     for x in stack:
        #         if not x:
        #             tmp.append(None)
        #             tmp.append(None)
        #             continue
        #         left, right = x.left, x.right
        #         tmp.append(left)
        #         tmp.append(right)
        #     p1, p2, change = 0, len(tmp) - 1, True
        #     while p1 <= p2 and change:
        #         change = False
        #         if not tmp[p1]:
        #             p1 += 1
        #             change = True
        #         if not tmp[p2]:
        #             p2 -= 1
        #             change = True
        #     if p1 > p2: break
        #     stack = tmp[p1: p2 + 1]
        #     ans = max(ans, len(stack))
        # return ans
        if not root: return 0
        stack = [(root, 0)]
        ans = 1
        while stack:
            tmp = []
            left_idx, right_idx = float('inf'), 0
            for x in stack:
                d, k = x[0], x[1]
                left, right = d.left, d.right
                if left:
                    tmp.append((left, 2 * k))
                    left_idx = min(left_idx, 2 * k)
                if right:
                    tmp.append((right, 2 * k + 1))
                    right_idx = max(right_idx, 2 * k + 1)
            ans = max(ans, right_idx - left_idx + 1)
            stack = tmp
        return ans
