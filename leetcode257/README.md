# 二叉树的所有路径

> 给定一个二叉树，返回所有从根节点到叶子节点的路径。

> 说明: 叶子节点是指没有子节点的节点。

```
示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]
```

**解释:**
> 所有根节点到叶子节点的路径为: 1->2->5, 1->3


## 解决思路:
1. 使用队列遍历每个节点，将每个节点的路径存入一个字典中，并使用另外一个数组来保存叶子节点，最后遍历叶子节点的数组，将对应的路径从
字典中获取到，并返回


### 其他解决思路：
1. 考虑递归的方式，分别判断左右子节点，直到碰到叶子节点；每一层递归的输入是什么呢？结合题意，就是上层递归的输入加上上层结点的值了；而对于根结点，其输入就是空字符串

```python
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def paths(root, path, result):
            if root.left is None and root.right is None:
                result.append(path + str(root.val))
            if root.left is not None:
                paths(root.left, path + str(root.val) + '->', result)
            if root.right is not None:
                paths(root.right, path + str(root.val) + '->', result)

        result = []
        if root is not None:
            paths(root, '', result)
        return result
```