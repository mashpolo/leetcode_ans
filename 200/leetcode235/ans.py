#!/usr/bin/env python
# coding=utf-8
"""
@desc:   二叉搜索树的最近公共祖先
@author: Luo.lu
@date:   2018-9-26

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathp = self.findPath(root, p)
        pathq = self.findPath(root, q)
        res = root
        for i in range(1, min(len(pathp), len(pathq))):
            if pathp[i] == pathq[i]:
                res = pathp[i]
        return res

    def findPath(self, root, p):
        path = []
        while root.val != p.val:
            path.append(root)
            if p.val > root.val:
                root = root.right
            elif p.val < root.val:
                root = root.left
        path.append(p)
        return path


if __name__ == "__main__":
    a = TreeNode(6)
    a.left = TreeNode(2)
    a.right = TreeNode(8)
    a.left.left = TreeNode(0)
    a.left.right = TreeNode(4)
    a.left.right.left = TreeNode(3)
    a.left.right.right = TreeNode(5)
    a.right.left = TreeNode(7)
    a.right.right = TreeNode(9)

    A = Solution()
    print(A.lowestCommonAncestor(a, TreeNode(4), TreeNode(5)))
