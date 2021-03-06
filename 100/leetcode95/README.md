# 不同的二叉搜索树 II

> 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

```
示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

```


## 解决办法：
- 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 
- 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 
- 它的左、右子树也分别为二叉排序树。
- 我们依旧使用递归
- 以不同的数作为root，
- 这就由i左边的数可以构成什么样的二叉搜索树，
- i右边的数可以构成什么样的二叉搜索树决定。
- 接着我们就会在i的左边去找一个左子树root，在i的右边去找一个右子树的root，这就是递归的过程。
