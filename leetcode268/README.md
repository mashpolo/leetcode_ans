# 缺失数字

> 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

```
示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
```

**说明:**
> 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?


## 解决思路：
1. 暴力破解，直接对数组排序，然后判断索引和当前数是否相等，不相等就返回索引；如果只有1个数，返回当前数组的个数即可


### 最优思路：
1. 采用数学的办法。由于是0-n个数字，我们可以轻易的用等差数列求和公式求出和，
那么减去给定数组的和，得到的结果就是缺失的数字。

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum = len(nums)*(len(nums)+1)/2
        t_sum = sum(nums)
        return temp_sum - t_sum
```

2. 利用位运算中的异或运算，最初设置返回值res是nums的长度，目标值i^现有值nums\[i]，那么如果i和nums\[i]是相同的，
异或的结果就是0，再让res^该结果，那么res仍等于res，这样说明i这个数是存在的，
也就是说所有相同的数都被变成了0，剩下的就是缺失的数

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res ^= (i ^ nums[i])
        return res
```