# Excel表列名称
> 给定一个正整数，返回它在 Excel 表中相对应的列名称。

```
例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
```

```
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"
```


## 解决思路：
1. 将数字转化为26进制的数来算，例如'AAA'='26*26*1+26*1+26*0'='703'
2. 采用chr用法，可以将数字转化为unicode字符


### 递归解决方案：

```python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        return self.convertToTitle((n-1)/26) + chr((n-1)%26 + 65)
```