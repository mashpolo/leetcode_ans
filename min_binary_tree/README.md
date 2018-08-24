# 求二叉树的最小深度
> 给定一个二叉树，找出其最小深度。

> 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

> 说明: 叶子节点是指没有子节点的节点。

```
示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
```

## 解决思路:
1. 存储一个数据结构，每次判断当前层次中每个节点是否没有左右子树了，如果有一个节点没有左右子树就跳出循环
2. 按照层级来迭代

## 递归的思路:
1. 分别递归左右子树，直到该节点没有左右子树

```python
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if root.left is None or root.right is None:
            return max(leftDepth, rightDepth) + 1
        return min(leftDepth, rightDepth) + 1
```