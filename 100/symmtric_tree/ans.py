class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
   def isSymmetric(self, root):
        queue = [root]
        while queue:
            values = [i.val if i else None for i in queue]
            if values != values[::-1]: return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True
