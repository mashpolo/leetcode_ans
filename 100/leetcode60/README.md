# 第k个排列

> 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

```
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
```

## 解决办法：
1. 最简单的思路就是回溯，然后得出最后一个
2. 利用数学的思维，因为实际上是排了序的，所以直接可以判断每个位置上的数字和它在列表中的索引位置

```python
class Solution(object):
    def getPermutation(self, n: int, k: int) -> str:
        """
        :param n:
        :param k:
        :return:
        """
        import math
        ls = list(range(1, n + 1))
        res = ''
        k -= 1
        while ls:
            m = math.factorial(len(ls) - 1)
            i, k = k // m, k % m  # 索引
            res += str(ls[i])
            ls.pop(i)
        return res
```
