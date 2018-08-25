class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        less = sum - root.val
        left = root.left
        right = root.right
        if left is None and right is None:
            if less == 0:
                return True
            else:
                return False
        else:
            return self.hasPathSum(left, less) or self.hasPathSum(right, less)
