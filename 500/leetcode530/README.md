# 二叉搜索树的最小绝对差

> 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。

```
示例 :

输入:

   1
    \
     3
    /
   2

输出:
1

解释:
最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
注意: 树中至少有2个节点。
```

## 解决办法：
1. 遍历二叉树，然后排序，求每两个值的绝对值，然后求该数组中最小的数


### 最优解：
1. 直接采用递归的方式，求当前节点和左节点的值

```python
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.last = -0x80000000
        self.ans = 0x7FFFFFFF
        def inOrderTraverse(root):
            if not root: return
            inOrderTraverse(root.left)
            self.ans = min(self.ans, root.val - self.last)
            self.last = root.val
            inOrderTraverse(root.right)
        inOrderTraverse(root)
        return self.ans

