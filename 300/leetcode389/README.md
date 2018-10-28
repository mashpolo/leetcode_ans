# 找不同

> 给定两个字符串 s 和 t，它们只包含小写字母。

> 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

> 请找出在 t 中被添加的字母。


```
示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。
```


## 解决办法：
1. 采用异或运算，两个字符串相加后来进行依次异或，最后的结果则是多的那一个

### 其他思路：
1. 分别统计s和t中每个字母出现的次数，不一样的即为所求。为了减少计算量，可以先遍历s，用数组统计26个字母出现的次数；再遍历t，在刚才的数组基础上对出现的字母次数减一，次数出现负数的字母即为所求

```python
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = [0] * 26
        for c in s:
            letters[ord(c) - 97] += 1
        for c in t:
            letters[ord(c) - 97] -= 1
            if letters[ord(c) - 97] < 0:
                return c
```