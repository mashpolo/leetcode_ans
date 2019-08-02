# 二叉树的右视图

> 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

```
示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

## 解决办法：
1. 采用层序遍历



### 其他办法：
1. 利用递归的方式求解

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        d={}
        def f(root,i):
            if root:
                d[i]=root.val
                f(root.left,i+1)
                f(root.right,i+1)
        f(root,0)
        return list(d.values())
```

