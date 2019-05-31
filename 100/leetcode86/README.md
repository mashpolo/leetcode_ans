# 分隔链表

> 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

```
你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
```


## 解决办法：
1. 采用双指针的办法，分别维护一个大的和小的链表，然后在组装在一起。需要注意的是大的链表最终的节点的下一个必须是None，不然会造成死循环


### 其他解决办法：
1. 将所有值拿出来，然后开始重新组装成新链表

```python
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        result=ListNode(0)
        res=result

        result_=ListNode(0)
        res_=result_

        while head:
            if head.val >= x:
                result_.next= ListNode(head.val)
                result_=result_.next
            else:
                result.next= ListNode(head.val)
                result=result.next
            head=head.next
        result.next=res_.next
        return res.next
```
