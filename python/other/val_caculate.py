# !/usr/bin/python3
from typing import List

# a = [1, 2, 3, [4, 5, 6]]
# b = a[:] # 与copy作用相同
# b[3].append(7)
# print("a:", a)
# print("b:", b)
# print("--------------------")
# b.append(8)
# print("a:", a)
# print("b:", b)


from collections import OrderedDict

# val_caculate.py
a = 10  # a是整数
print('10/3 = ', 10 / 3)
print('9/3 = ', 9 / 3)
print('10//3 = ', 10 // 3)
print('10%3 = ', 10 % 3)


# 说明：
# 1. 除法：/;
#    取整：//;
#    取余：%
# 2. Python的整数没有大小限制,而Java对32位整数的范围限制在-2147483648-2147483647；
#    Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        root_val = preorder[0]
        mid = inorder.index(root_val)
        return TreeNode(root_val, self.buildTree(preorder[1:mid + 1], inorder[:mid]),
                        self.buildTree(preorder[mid + 1:], inorder[mid + 1:]))
