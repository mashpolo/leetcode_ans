#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-28

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        def dfs(node):
            if not node.left and not node.right:
                return [str(node.val)]
            left, right = [], []

            if node.left:
                left = [str(node.val) + str(x) for x in dfs(node.left)]
            if node.right:
                right = [str(node.val) + str(x) for x in dfs(node.right)]
            return left + right

        res = [int(x) for x in dfs(root)]
        return sum(res)
