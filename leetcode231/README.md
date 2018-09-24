# 2的幂

> 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

```
示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false
```


## 解决思路：
1. 暴力解决，直接迭代或者递归请求，一直除2求余数


### 最佳思路：
> 所有的和2相关的运算，都可以考虑位运算

1. 这道题直接可以转换位二进制数，2的幂次 x 表示成二进制一定是一个1后面若干个0，因此直接计算输入数的二进制表示是否只有一个1

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count('1') == 1
```

2. 和上面的思路一样，2的幂次 x 表示成二进制一定是一个1后面若干个0，那么 x-1 一定是一个0后面若干个1，所以 x & (x-1) = 0 ，非2的幂无法得到0

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)
```