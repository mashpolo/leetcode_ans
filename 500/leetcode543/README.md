# 二叉树的直径

> 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

```

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

```

## 解决办法：
1. 左子树高度 + 右子树高度 + 1


### 其他办法：
1. 递归的思路

```python
class Solution(object):
    def traverse(self,root):
        if root is None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.ans = max(self.ans, left + right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.traverse(root)
        return self.ans
```
