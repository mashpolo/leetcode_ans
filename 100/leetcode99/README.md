# 恢复二叉搜索树

> 二叉搜索树中的两个节点被错误地交换。

> 请在不改变其结构的情况下，恢复这棵树。

```
示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

```

> 进阶:

- 使用 O(n) 空间复杂度的解法很容易实现。
- 你能想出一个只使用常数空间的解决方案吗？


## 解决办法：
1. 采用中序遍历，由于二叉搜索树中，左<根<右，因此中序得到的一定是一个升序排列，保存两个列表分别存储节点和节点值，然后互相交换即可


### 其他解决办法：
1. 要使用O(1)的空间复杂度的话，需要使用到指针的思路

```
假设现在有一个乱掉的二叉搜索树[1,2,5,4,3,6,7]
很明显3和5颠倒了。那么在中序遍历时：当碰到第一个逆序时：为5->4，那么将n1指向5，n2指向4，
注意，此时n1已经确定下来了。然后prev和root一直向后遍历，直到碰到第二个逆序时：4->3，此时将n2指向3，
那么n1和n2都已经确定，只需要交换节点的值即可。prev指针用来比较中序遍历中相邻两个值的大小关系
```

```python
class Solution(object):
    def FindTwoNodes(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root:
            self.FindTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if not self.n1:
                    self.n1 = self.prev
            self.prev = root
            self.FindTwoNodes(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
```
