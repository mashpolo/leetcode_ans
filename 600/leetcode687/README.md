# 最长同值路径

> 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

```
注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
```

## 解决办法：
1. 后序遍历的办法，使用递归的方式，判断左右子树中相同节点最远的值，再到后面必须要加一（后序遍历）中，最后一个是根节点
