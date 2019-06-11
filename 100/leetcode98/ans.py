#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-11

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def ValidBST(self, root, _min, _max):
        if root == None:
            return True
        if root.val <= _min or root.val >= _max:
            return False
        return self.ValidBST(root.left, _min, root.val) and self.ValidBST(root.right, root.val, _max)

    def isValidBST(self, root):
        return self.ValidBST(root, -2147483649, 2147483648)




