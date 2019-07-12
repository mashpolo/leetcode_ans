#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-13

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans
        stack = []
        node = root
        while node or stack:
            while node:
                ans.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return ans


