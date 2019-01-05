#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-05

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if node.val == val:
                return node
            if node.val < val and node.right:
                nodes.append(node.right)
            if node.val > val and node.left:
                nodes.append(node.left)
        return
