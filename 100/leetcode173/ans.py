#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-27

"""


class BSTIterator(object):
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
    
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if not self.root:
            return None
        if not self.root.left:
            temp = self.root.val
            if self.root.right:
                self.root = self.root.right
            else:
                self.root = None
            return temp
        else:
            la = self.root
            pa = self.root
            while pa.left:
                la = pa
                pa = pa.left
            if not pa.right:
                temp = pa.val
                la.left = None
                return temp
            else:
                temp = pa.val
                la.left = pa.right
                return temp
    
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.root

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
