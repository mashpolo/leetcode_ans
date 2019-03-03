# 递增顺序查找树

> 给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。


```
示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9


提示：

给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。
```

## 解决办法：
1. 利用栈来保存中序遍历的每个节点，再将原树重排

```python
    def increasingBST(self, root):
        s=[]
        dummy=TreeNode(0)
        p=dummy

        while s or root:
            if root:
                s.append(root)
                root=root.left
            else:
                cur=s.pop()
                root=cur.right
                cur.left=None
                p.right=cur
                p=p.right
        return dummy.right
```
