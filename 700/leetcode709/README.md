# 转换小写字母

> 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。


```
示例 1：

输入: "Hello"
输出: "hello"
示例 2：

输入: "here"
输出: "here"
示例 3：

输入: "LOVELY"
输出: "lovely"

```

## 解决办法：
1. 直接使用字典来匹配显然比较耗费存储
2. 使用asci字符来判断

```python
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for s in str:
            if ord(s) >= ord('A') and ord(s) <= ord('Z'):
                res += chr(ord(s) - ord('A') + ord('a'))
            else:
                res += s
        return res
```
