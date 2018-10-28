#!/usr/bin/env python
# coding=utf-8
"""
@desc:   二叉树的所有路径
@author: Luo.lu
@date:   2018-9-28

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = {root: str(root.val)}
        nodes = [root]
        leaf_node = []
        while nodes:
            node = nodes.pop()
            if node.left:
                nodes.append(node.left)
                result[node.left] = result[node] + '->' + str(node.left.val)
            if node.right:
                nodes.append(node.right)
                result[node.right] = result[node] + '->' + str(node.right.val)
            if not node.left and not node.right:
                leaf_node.append(node)
        all = []
        for x in leaf_node:
            all.append(result[x])
        return all
