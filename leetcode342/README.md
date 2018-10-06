# 4的幂

> 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

```
示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
```

**进阶：**
> 你能不使用循环或者递归来完成本题吗？


## 解决思路：
1. 和求3的幂一样，由于是有大小限制的，直接把所有4的幂找出来，判断当前数是否在这里面就行了


### 最优解
1. 4的幂次表现在二进制上，为首位为1，后面有偶数个0。所以先将输入的数转换成2进制，再判断2进制中0和1的个数即可。
注意：Python里将数转成二进制后的表示为“0bxxxx”，最前面有个0，在计算0的个数时要考虑到。


```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and bin(num).count('1') == 1 and bin(num).count('0') % 2 == 1
```

2. 由于4是2的倍数，那么可以考虑二进制计算的方式，转化成二进制后，判断1是在奇位，后面是偶数个0即可
```python
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num&(num-1) == 0 and (num & 0x55555555) != 0
```