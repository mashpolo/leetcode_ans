#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-29

"""
# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        depth = 0
        que = collections.deque()
        que.append(root)
        while que:
            size = len(que)
            for i in range(size):
                node = que.popleft()
                for child in node.children:
                    que.append(child)
            depth += 1
        return depth




if __name__ == '__main__':
    a = Node(1, [Node(2, [Node(3, [])])])
    A = Solution()
    print(A.maxDepth(a))
