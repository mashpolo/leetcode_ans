#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-21

"""


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nodes = [root]
        values = []
        while nodes:
            node = nodes.pop()
            if k - node.val in values:
                return True
            values.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return False
