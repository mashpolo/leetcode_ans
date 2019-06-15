#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-15

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not len(postorder):
            return None
        if len(inorder) == 1:
            # 这里要返回结点，而不是返回具体的数
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return root
