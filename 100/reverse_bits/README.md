# 颠倒二进制位
> 颠倒给定的 32 位无符号整数的二进制位。

```
示例:

输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
```

> 进阶:
- 如果多次调用这个函数，你将如何优化你的算法？


## 解决思路：
1. 将数字转化为二进制数再反转，判断位数，如果小于32位，在后面补0(32位数即是在原二进制前面补0)


### 优化思路：
1. 按位处理，将输入n的二进制表示从低位到高位的值依次取出，逆序排列得到翻转后的值

```python
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            res <<= 1
            res |= ((n >> i) & 1)
        return res
```

2. 类似二分的思想，每次处理一半的位交换

```python
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n
```