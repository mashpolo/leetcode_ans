# 扰乱字符串

> 我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

> 同样地，如果我们继续将其节点 "eat" 和 "at" 进行交换，将会产生另一个新的扰乱字符串 "rgtae" 。

```
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
```

> 我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

> 给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。


```
示例 1:

输入: s1 = "great", s2 = "rgeat"
输出: true
示例 2:

输入: s1 = "abcde", s2 = "caebd"
输出: false
```

## 解决办法：
1. 利用切割字符串的思路，要想是扰乱的，那么只有可能是不管哪一部分，字符的个数都是相等的，也就是说，只能是挨着的才是扰乱，否则中间漏掉一个都不行


### 其他办法：

- 如果s1 前k个 跟s2后k个，是扰乱字符串，那么只要看s1第k+1个到最后 与 s2第0个到len(s2)-k个是否是扰乱字符串

- 如果s1 前k个 跟s2前k个，是扰乱字符串， 那么只要看s1， s2的第k+1个到最后是否是扰乱字符串

- 注意长度小于等于3的情形可以单独处理，简化代码

- 用记忆化搜索防止重复搜索


```python
# 思路其实和判断切割掉的部分个数是同样的思路

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = dict()
        def dfs(s1, s2):
            if (s1,s2) in memo:
                return memo[(s1, s2)]
            l1, l2 = len(s1), len(s2)
            if l1 != l2:
                memo[(s1,s2)] = False
                return False
            if l1 < 4:
                memo[(s1, s2)] = sorted(s1) == sorted(s2)
                return memo[(s1, s2)]
            if s1==s2: #小范围单独处理的思想很重要
                memo[(s1, s2)] = True
                return True
            if sorted(s1) != sorted(s2):
                return False
            memo[(s1, s2)] = False
            for k in range(1, l1):
                a = s1[:k]
                b = s2[:k]
                c = s1[k:]
                d = s2[k:]
                e = s2[l1-k:]
                f = s2[:l1-k]
                if (dfs(a,b) and dfs(c, d)) or (dfs(a,e) and dfs(c, f)):
                    memo[(s1,s2)] = True
                    return memo[(s1,s2)]
            return memo[(s1, s2)]
        return dfs(s1, s2)
```
