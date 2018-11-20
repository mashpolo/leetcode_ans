#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-20

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]
        res = []
        while nodes:
            node = nodes.pop()
            res.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        res.sort()
        ans = []
        for x in range(len(res)):
            if x == len(res) - 1:
                break
            ans.append(res[x+1] - res[x])
        return min(ans)
