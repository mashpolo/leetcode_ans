# 第三大的数

> 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

```
示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:

输入: [2, 2, 3, 1]

输出: 1
```

**解释:**
- 注意，要求返回第三大的数，是指第三大且唯一出现的数。
- 存在两个值为2的数，它们都排第二。

## 解决办法：
1. 首先判断唯一的数组成的数组的个数，如果小于3，取最大值
2. 循环判断1和2，2和3的值是否相等，这里需要考虑数组是否为空


### 其他解决思路：
1. 直接抛弃掉所有的最大数，连续2次，后续的值即是要求的

```python
class Solution1(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)
```