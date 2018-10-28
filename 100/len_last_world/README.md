# 求最后一个单词的长度
> 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

> 说明：一个单词是指由字母组成，但不包含任何空格的字符串。

```
示例:

输入: "Hello World"
输出: 5
```

## 解决思路：
1. 利用replace，把多个空格替换成一个
2. 按照空格分隔成列表，当列表最后为空字符串，直接删掉，迭代开始

## 最优解法
- 使用rsrip去除掉右边的空格

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        for v in reversed(s):
            if v.isspace():
                if cnt:break
            else:cnt+=1
        return cnt
```
