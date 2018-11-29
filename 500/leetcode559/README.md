# N叉树的最大深度

> 给定一个 N 叉树，找到其最大深度。

> 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

```
例如，给定一个 3叉树 :







我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。
```

## 解决办法：
1.深度遍历，求层级即可，主要是考虑到循环遍历节点的问题


### 其他解决办法：
1. DFS的方法

```python

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        depth = 1 + max(self.maxDepth(child) for child in root.children)
        return depth
```
