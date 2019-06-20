#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-20

"""


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = [root]
        while(queue): #temp=[]使用temp不如当成队列节省空间
            node_pre = None
            for i in range(len(queue)):#保证每次都是读取一行的量
                node = queue.pop(0)
                if node_pre: node_pre.next = node
                node_pre = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


