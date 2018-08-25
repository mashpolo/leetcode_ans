# 求二叉树的路径总和
> 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

> 说明: 叶子节点是指没有子节点的节点。

```
示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
```

## 解决思路：
1. 主要是利用递归，分别判断左右节点能不能得到总和减去当前节点的值的数字，求并集即可
2. 直到当前节点没有左右子树，看less是等于0还是不等于0

## 更pythonic的写法：

```python
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if sum == root.val and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```
