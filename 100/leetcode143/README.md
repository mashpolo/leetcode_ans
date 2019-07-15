# 重排链表

> 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，

> 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

> 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


```
示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
```

## 解决办法：
1. 双链表合并法大体思路是这样的:首先找到整条链表的中点，以中点为界，将链表分为前后两条；依据题意，我们只需要把后一条链表翻转(这里用头插法)，然后交错合并两条链表的节点即可