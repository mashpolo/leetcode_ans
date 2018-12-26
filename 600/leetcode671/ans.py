#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-26

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        nodes = [root]
        res = [root.val]
        while nodes:
            node = nodes.pop()
            res.append(node.val)
            if node.left:
                nodes.append(node.left)
                nodes.append(node.right)

        res = list(set(res))
        res.sort()
        print(res)
        return -1 if len(res) == 1 else res[1]

