# 二叉树的中序遍历

> 给定一个二叉树，返回它的中序 遍历。

```
示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
```

## 解决办法：
1. 如果是迭代的方式，那么就利用一个栈来存储节点，先优先找到每个节点最左边的节点