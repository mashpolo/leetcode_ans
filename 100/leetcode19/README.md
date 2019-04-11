# 删除链表的倒数第N个节点

> 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

```
示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
```


## 解决办法：
1. 使用快慢指针的办法，快指针先走n步，然后两个指针一起走，当快指针没有节点后，慢指针跳过下一个节点即可