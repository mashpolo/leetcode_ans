# 判断一个树是否是对称的
> 给定一个二叉树，检查它是否是镜像对称的。

```
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
```

## 解决办法：
1. 使用迭代的方法，把每个子节点做成一个栈的数据结构，和右节点来比较，效率是最高的
2. 采用递归的方式也可以

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(L,R):
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        return isSym(root, root)
```
