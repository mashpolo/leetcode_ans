#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-13

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        nodes = [root]
        res = []
        while nodes:
            level_nodes, nodes = nodes, []
            level_ans = []
            for node in level_nodes:
                level_ans.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            res.append(level_ans)

        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node1.left = TreeNode(2)
    node1.right = TreeNode(3)
    node1.left.left = TreeNode(4)
    node1.right.right = TreeNode(5)
    A = Solution()
    print(A.levelOrder(node1))
