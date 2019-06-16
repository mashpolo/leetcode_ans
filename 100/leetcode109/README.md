# 有序链表转换二叉搜索树

> 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

> 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

```
示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

```


## 解决办法：
1. 使用快慢指针查找每个树的跟节点，然后分别递归

### 其他思路：
1. 可以将链表转化位数组，然后二分法来解决

```python
class Solution(object):
    # 本题还可先将链表转化为数组，再用108题方法
     def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        # 调用和第108题一样的动态规划方法
        def buildBST(nums):
            if len(nums)==0:
                return
            # 取nums列表的中间下标值
            mid_index = len(nums)//2
            pNode = TreeNode(nums[mid_index])
            pNode.left = buildBST(nums[:mid_index])
            pNode.right = buildBST(nums[mid_index+1:])
            return pNode
        return buildBST(head_list)
```
