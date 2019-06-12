#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-12

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        """
        python,先中序遍历得到两个列表，然后排序赋值，至于为什么中序遍历？因为二叉搜索树的左<根<右，所以按照中序遍历后的值组可以按照升序排序付给二叉树。
        """
        point=[]
        val=[]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            point.append(root)
            val.append(root.val)
            inorder(root.right)
            return
        inorder(root)
        val=sorted(val)
        for i in range(len(point)):
            point[i].val=val[i]
