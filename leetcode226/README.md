# 翻转二叉树

> 翻转一棵二叉树。

```
示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
```


## 解决思路：
1. 使用队列或是栈来保存当前节点的左右子树(不为空的)，然后交换左右子树，遍历队列
2. 采用递归的思路来做


```python
# 递归

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        tmp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmp)
        return root
```