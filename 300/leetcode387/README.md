# 字符串中的第一个唯一字符

> 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

```
案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
```

## 解决办法：
1. 使用两个字典来保存每个字符出现的次数，然后取最小的那个数即可


### 其他解决办法：
1. 使用字典来保存，然后取第一个数值是1的字符
```python
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for c in s:
            letters[c] = letters[c] + 1 if c in letters else 1
        for i in range(len(s)):
            if letters[s[i]] == 1:
                return i
        return -1
```
