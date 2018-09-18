# 删除链表中的节点

> 删除链表中等于给定值 val 的所有节点。

```
示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
```

## 解决思路：
1. 使用两个指针，一个指向当前节点，一个指向前一个节点，判断当前节点值是否符合，符合的话前指针指向当前节点的下一个节点


### 更pythonic的写法:
> 直接为当前链表创建一个空的头结点，返回原节点的下位即可

```python
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
```