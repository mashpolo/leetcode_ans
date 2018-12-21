# 两数之和

> 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

```
案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True


案例 2:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
```

## 解决办法：
1. 最简单的办法就是遍历整个二叉树，存入列表；每次判断新的数字是否存在列表中，直接最后直接False


### 其他解决办法：
1. 使用递归的方式来解决
2. 由于该题指明了是二叉搜索树，不可能出现重复元素

```python
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.dset = set()
        self.traverse(root)
        for n in self.dset:
            if k - n != n and k - n in self.dset:
                return True
        return False
    def traverse(self, root):
        if not root: return
        self.dset.add(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
```
