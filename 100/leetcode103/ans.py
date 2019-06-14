#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-14

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        level_nodes = [root]
        flag = 0
        res = []
        while level_nodes:
            flag += 1
            level_ans = []
            nodes = []
            for node in level_nodes:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                level_ans.append(node.val)
            if flag % 2 > 0:
                res.append(level_ans)
            else:
                res.append(level_ans[::-1])
            level_nodes = nodes

        return res
