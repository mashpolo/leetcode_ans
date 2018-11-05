# 重复的字符串

> 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

```
示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
```

## 解决思路：
1. 使用KMP算法求解，时间复杂度O(n)



### 最优方法
1. 直接打破字符串，然后拼接在一起，判断原字符串是否存在其中就可以了
```
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type str: str
        :rtype: bool
        """
        return s in s[1:] + s[:-1]
```
