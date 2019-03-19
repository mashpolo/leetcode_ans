#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-19

"""


class Solution:
    def isUnivalTree(self, root):
        mark = root.val
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if node.val != mark:
                return False
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return True

