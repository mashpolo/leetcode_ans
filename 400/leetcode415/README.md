# 字符串相加

> 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

```
注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
```

## 解决思路：
1. 通过取巧的方式，利用`ord`函数，把字符串转成数字再来相加，但是要考虑到位数

### 其他思路：
1. 使用列表的方式也可以

```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        l1 = len(num1)
        l2 = len(num2)
        lm = max(l1, l2)
        num1 = num1.zfill(lm)
        num2 = num2.zfill(lm)
        num1 = num1[::-1]
        num2 = num2[::-1]

        s = []
        c = 0
        for i in range(lm):
            sum1 = int(num1[i]) + int(num2[i]) + c
            c, sum1 =divmod(sum1, 10)
            s.append(str(sum1))
        l = s[::-1]
        s1 = ''.join(l)
        if c == 1:
            s1 = '1' + s1
        if  len(s1) == 1:
            return l[0]
        return s1
```
