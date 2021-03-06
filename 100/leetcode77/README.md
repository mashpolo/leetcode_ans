# 组合

> 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

```
示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

```


## 解决办法：
1. itertools的combinations函数可以直接解决掉这个问题，使用回溯的办法来解决
2. 直接采用递归的方法来解决组合问题，C(m,n)=C(m-1,n)+C(m-1,n-1)

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k>n or k==0:
            return []
        if k==1:
            return [[i] for i in range(1,n+1)]
        if k==n:
            return [[i for i in range(1,n+1)]]

        answer=self.combine(n-1,k)
        for item in self.combine(n-1,k-1):
            item.append(n)
            answer.append(item)

        return answer
```
