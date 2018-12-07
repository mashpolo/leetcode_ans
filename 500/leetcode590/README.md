# N叉树的后序遍历

> 给定一个 N 叉树，返回其节点值的后序遍历。

```
例如，给定一个 3叉树 :







返回其后序遍历: [5,6,3,2,4,1].



说明: 递归法很简单，你可以使用迭代法完成此题吗?
```


## 解决思路：
1. 采用递归和迭代都可以

### 递归的思路：


```
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res
```
