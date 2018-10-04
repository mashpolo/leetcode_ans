# 区域和检索 - 数组不可变
> 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

```
示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

**说明:**

- 你可以假设数组不可变。
- 会多次调用 sumRange 方法。


## 解决思路：
1. 因为要多次调用求和的方法，因此不能每次都重新计算
2. 简单的思路就是将数组索引前面的数求和，保存到一个新数组里面，然后求和的时候，只需要大索引的和减去小的即可

### 其他方法：
1. 可以当成二叉树来求解，不过，实际上题目说了数组不会变化，
所以BIT的优势并没有完全发挥，BIT的更新和计算部分和的时间复杂度都是O(logn)。

```python
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.length = len(nums)
        self.BIT = [0] * (self.length + 1)
        for i in range(len(nums)):
            self.updateBIT(i, nums[i])

    def updateBIT(self, i, val):
        i += 1
        while i <= self.length:
            self.BIT[i] += val
            i += i & (-i)

    def getBITsum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.BIT[i]
            i -= i & (-i)
        return res

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getBITsum(j) - self.getBITsum(i-1)
```