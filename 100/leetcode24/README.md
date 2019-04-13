# 两两交换链表中的节点

> 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

> 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


```
示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
```

## 解决办法：
1. 采用递归的办法，只到只剩最后一个或者没有节点了为止，每次都是交换当前节点
2. 利用三个指针分别指向前一组最后一个，当前和当前的第二个，使用迭代的方式

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a;
            pre = a
        return self.next
```
