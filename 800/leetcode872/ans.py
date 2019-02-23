#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-23

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leafs(node):
            if not node:
                return []
            res = []
            nodes = [node]
            while nodes:
                node = nodes.pop()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                if not node.left and not node.right:
                    res.append(node.val)
            return res
        return get_leafs(root1) == get_leafs(root2)




