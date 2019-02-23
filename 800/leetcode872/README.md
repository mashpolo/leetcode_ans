# 叶子相似的树

> 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

```
举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。



提示：

给定的两颗树可能会有 1 到 100 个结点。
```


## 解决办法：
1. 暴力遍历，分别求出两个树的叶值，然后比较
2. 遍历还可以是用递归的方式

```python
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.getLeafs(root1)==self.getLeafs(root2)
    def getLeafs(self,nd):
        if nd is None:return []
        if not (nd.left or nd.right):
            return [nd.val]
        return self.getLeafs(nd.left)+self.getLeafs(nd.right)
```
