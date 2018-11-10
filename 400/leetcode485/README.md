# 最大连续1的个数

> 给定一个二进制数组， 计算其中最大连续1的个数。

```
示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
```


## 解决思路：
1. 直接遍历，然后数个数即可，只是需要注意的是遍历到最后一个要把最后的n加进去


### 最优解
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max([len(i) for i in bytearray(nums).split(b'\x00')])
```
