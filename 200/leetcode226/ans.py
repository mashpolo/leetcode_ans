#!/usr/bin/env python
# coding=utf-8
"""
@desc:   翻转二叉树
@author: Luo.lu
@date:   2018-9-23

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        node_list = [root]
        for x in node_list:
            x.left, x.right = x.right, x.left
            if x.left:
                node_list.append(x.left)
            if x.right:
                node_list.append(x.right)

        return root


if __name__ == "__main__":
    r = TreeNode(4)
    r.left = TreeNode(3)
    r.right = TreeNode(2)

    A = Solution()
    print(A.invertTree(r))


