# 求 Excel表列序号

> 给定一个Excel表格中的列名称，返回其相应的列序号。

```
例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
```

```
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
```


## 解决思路：
1. 把26进制的运算转换成10进制就可以了


## 其他办法:

```python
# map & reduce
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x,y: x*26 + y, map(lambda x:ord(x)-64, s), 0)


# 系统自带的转换办法
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for c in s:
            sum = sum* 26 + int(c, 36) - 9
        return sum
```