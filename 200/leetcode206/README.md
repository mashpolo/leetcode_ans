# 反转链表

> 反转一个单链表。

```
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
```

## 解决思路：
1. 优先考虑栈的数据结构
```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        newList = []
        while p:
            newList.insert(0, p.val)
            p = p.next

        p = head
        for v in newList:
            p.val = v
            p = p.next
        return head
```

2. 3个指针分别指向前一个，当前和后一个，依次往后推

3. 考虑递归，要考虑中止
```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        p = head.next
        n = self.reverseList(p)

        head.next = None
        p.next = head
        return n
```