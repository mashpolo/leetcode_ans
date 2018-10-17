# 左叶子之和

> 计算给定二叉树的所有左叶子之和。

```
示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
```

## 解决办法：
1. 遍历所有节点，判断当前节点的时候，如果该节点的左节点已经是叶子节点，保存该值到数组中，最后数组求和即可


