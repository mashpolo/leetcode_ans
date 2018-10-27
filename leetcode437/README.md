# 路径总和3

> 给定一个二叉树，它的每个结点都存放着一个整数值。

> 找出路径和等于给定数值的路径总数。

> 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

> 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

```
示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
```

## 解决思路：
1. 使用递归的方式,每条线来判断，使用defaultdict来存储一条线的数据


### 其他解决办法：
```python
from collections import defaultdict
class Solution(object):
    def inorder(self, root, target, summ, di):
        if not root:
            return 0
        summ += root.val
        numWays = di[summ-target]
        di[summ] += 1
        numWays += self.inorder(root.left, target, summ, di) + self.inorder(root.right, target, summ, di)
        di[summ] -= 1
        return numWays

    def pathSum(self, root, target):
        di = defaultdict(int)
        di[0] = 1
        return self.inorder(root, target, 0, di)
```
