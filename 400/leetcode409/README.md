# 最长回文数

> 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

> 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

**注意:**
> 假设字符串的长度不会超过 1010。

```
示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
```


## 解决思路：
1. 直接构造一个字典来保存字符串各个字母存在的个数,偶数直接相加，存在奇数那就最后再加上一个1即可


### 其他思路：
1. 思路一样，写法更pythonic一些

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        res=0
        for i in s:
            d[i] = 1 if i not in d else d[i]+1
        for i in d:
            res+=d[i]-d[i]%2
        return res+1 if res<len(s) else res
```
