#!/usr/bin/python3
from typing import List
import functools


# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前序数组的 左子树部分+根节点 是 1,2,4,5，中序数组的 左子树部分+根节点 是 4,2,5,1。这两者的数组长度是一样的。
# 我们可以根据中序数组的中间位置 1，来确定前序数组的左右部分，由于前序数组第一个是根节点，
# 所以其左边部分是：[1:mid_index]，右半部分是 [mid_index+1:]
# 这里的 mid_index 是中序数组的中间下标位置。
# 递归函数实现如下：
#
# 终止条件:前序和中序数组为空
# 根据前序数组第一个元素，拼出根节点，再将前序数组和中序数组分成两半，递归的处理前序数组左边和中序数组左边，递归的处理前序数组右边和中序数组右边。
class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder):
            return None
        # 根据前序数组的第一个元素，就可以确定根节点
        root = TreeNode(preorder[0])
        # 用preorder[0]去中序数组中查找对应的元素
        mid_idx = inorder.index(preorder[0])
        # 递归的处理前序数组的左边部分和中序数组的左边部分
        # 递归处理前序数组右边部分和中序数组右边部分
        root.left = self.buildTree(preorder[1:mid_idx + 1], inorder[:mid_idx])
        root.right = self.buildTree(preorder[mid_idx + 1:], inorder[mid_idx + 1:])
        return root




