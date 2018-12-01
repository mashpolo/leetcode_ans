# 二叉树的坡度

> 给定一个二叉树，计算整个树的坡度。

> 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

> 整个树的坡度就是其所有节点的坡度之和。

```

示例:

输入:
         1
       /   \
      2     3
输出: 1
解释:
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
注意:

任何子树的结点的和不会超过32位整数的范围。
坡度的值不会超过32位整数的范围。

```

## 解决思路：
1. 采用递归的方式，求每一个节点的左右子树的差值，然后求和


### 更好的写法：

```python
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def subTreeSum(root):
            if root is None:
                return 0
            lsum = subTreeSum(root.left)
            rsum = subTreeSum(root.right)
            self.ans += abs(lsum - rsum)

            return root.val + lsum + rsum
        subTreeSum(root)
        return self.ans
```
