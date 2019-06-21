#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-21

"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        last = root #last始终表示每一层第一个有子树的节点
        while(last):
            while(last and not last.left and not last.right):last = last.next
            if not last:break #如果没有左右子树，自然不用更改什么
            cur = None
            i= last
            while(i):#相当于遍历每一层，利用next信息进行递推
                if i.left:
                    if cur:cur.next = i.left
                    cur = i.left
                if i.right:
                    if cur:cur.next = i.right
                    cur = i.right
                i = i.next#找兄弟给右节点
            last = last.left if last.left else last.right#由于开始的while循环已经确保last有子树
        return root
