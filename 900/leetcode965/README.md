# 单值二叉树

> 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

> 只有给定的树是单值二叉树时，才返回 true；否则返回 false。


```
示例 1：

输入：[1,1,1,1,1,null,1]
输出：true
示例 2：



输入：[2,2,2,5,2]
输出：false


提示：

给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99] 。
```


## 解决办法：
1. 遍历的思路，判断是否又重复的数截止
2. 利用生成器更能减少内存的占用

```python
class Solution(object):
    def isUnivalTree(self, root):
        root = iterable(root)
        return len(set(root)) == 1


def iterable(p):
    if p:
        yield p.val
        yield from iterable(p.left)
        yield from iterable(p.right)
```
