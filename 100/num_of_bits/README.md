# 求二进制数中1的个数

> 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

```
示例 :

输入: 11
输出: 3
解释: 整数 11 的二进制表示为 00000000000000000000000000001011


示例 2:

输入: 128
输出: 1
解释: 整数 128 的二进制表示为 00000000000000000000000010000000
```


## 解决思路：
1. 32位的数字实际上就在在不足32位的二进制数前补0，因此，直接使用bin函数返回二进制数，然后判断里面1的个数
2. 利用collections模块中的Counter方法可以，使用replace也可以


```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len(bin(n)[2:].replace('0', ''))
```

3. 通过位运算，每次右移一位，在使用&运算来加一
```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n&1
            n >>= 1
        return count
```