# 多叉树的遍历

> 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

```
例如，给定一个 3叉树 :







返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]

```

**说明:**

- 树的深度不会超过 1000。
- 树的节点总数不会超过 5000。


## 解决思路：
1. 使用循环遍历就可以了，需要注意一点的是顺序，结果和节点分别存入队列或是栈(需要注意保存的顺序)


### 其他解决办法：
1. 直接保存的时候，记录层数


```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = [[]]
        while queue:
            node, level = queue.pop(0)
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level + 1))
        return res
```
