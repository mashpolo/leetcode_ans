# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxL = 0
        
        def getMaxL(node, val):
            nonlocal maxL
            if node == None:
                return 0
            leftMaxL = getMaxL(node.left, node.val)
            rightMaxL = getMaxL(node.right, node.val)

            maxL = max(maxL, leftMaxL+rightMaxL)

            if(node.val == val):
                return max(leftMaxL, rightMaxL) + 1
            else:
                return 0
            
        if root != None:
            getMaxL(root, root.val)
        return maxL
