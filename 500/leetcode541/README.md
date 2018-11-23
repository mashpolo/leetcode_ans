# 反转字符串

> 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。


```
示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。
```

## 解决思路：
1. 直接判断字符串的长度和k的关系即可

### 更好的写法
```python
class Solution(object):
    def reverseStr(self, s, k):
        res = ''
        i = 0
        while i < len(s):
            res = res + s[i:i+k][::-1]
            res = res + s[i+k:i+(k*2)]
            i = i + (k * 2)
        return res
```

### 其他解决思路：

```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        round = int(math.ceil(len(s)/(2.0*k)))
        for i in range(round):
            res += s[2*i*k:(2*i+1)*k][::-1]
            res += s[(2*i + 1)*k:(2*i + 2)*k]
        return res
```
