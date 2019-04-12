# 合并K个排序链表

> 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

```
示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
```

## 解决办法：
1. 自己采用的是迭代的办法，构造一个小顶堆来存储当前所有链表的节点值，然后找出最小的，维护两个map来存储对应的链表索引，然后求被拿掉最小值的那个链表的下一个节点
2. 也可以采用分治的办法

```python
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        new_lists = []           # 存储不为空的元素
        for i in range(len(lists)):
            if lists[i]:         # 元素不为空
                new_lists.append(lists[i])
        if len(new_lists)==0:
            return None
        elif len(new_lists)==1:
            return new_lists[0]
        re = []                  # 临时存放完成一次循环的结果
        while len(new_lists)>1:    # 合并之后只剩最终合并的链表，长度为1
            for i in range(0, len(new_lists), 2):    # 每次去两个合并
                tem_head = ListNode(0)          # 建立临时头结点
                tem_ptr = tem_head             # 建立临时指针
                left = new_lists[i:i+1]        # 参与合并的第一个列表
                right = new_lists[i+1:i+1*2]    # 参与合并的第二个列表
                if right:   #如果第二列表不为空
                    ptr_left = left[0]        # 第一个链表的指针
                    ptr_right = right[0]      # 第一个链表的指针
                    # 合并两个列表
                    while ptr_left and ptr_right:
                        if ptr_left.val < ptr_right.val:
                            tem_ptr.next = ListNode(ptr_left.val)
                            ptr_left = ptr_left.next
                        else:
                            tem_ptr.next = ListNode(ptr_right.val)
                            ptr_right = ptr_right.next
                        tem_ptr = tem_ptr.next
                    while ptr_left:
                        tem_ptr.next = ListNode(ptr_left.val)
                        ptr_left = ptr_left.next
                        tem_ptr = tem_ptr.next
                    while ptr_right:
                        tem_ptr.next = ListNode(ptr_right.val)
                        ptr_right = ptr_right.next
                        tem_ptr = tem_ptr.next
                    re.append(tem_head.next)     # 追加合并的列表
                else:
                    re.extend(left)   #否则直接添加第一个列表
            new_lists = re[:]   # 循环完一次的结果赋值给原始列表
            re = []     # 将临时列表置空
        return new_lists[0]
```
