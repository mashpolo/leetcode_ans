# 寻找数组的中心索引

> 给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
> 我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

> 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

```
示例 1:

输入:
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释:
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
示例 2:

输入:
nums = [1, 2, 3]
输出: -1
解释:
数组中不存在满足此条件的中心索引。
```


- 说明:

- nums 的长度范围为 [0, 10000]。
- 任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。


## 解决办法：
1. 采用循环获取两边的值来判断即可，需要注意的是可能有负数，因此不能用左边大于右边来结束判断


### 其他办法：
1. 采用for循环

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if i != 0:
                left += nums[i - 1]
            right -= nums[i]
            if left == right:
                return i
        return -1
```

2. 减去当前数字的办法

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        N = len(nums)
        sums = [0] * (N + 1)
        for i in range(N):
            sums[i + 1] = sums[i] + nums[i]
        for i in range(N):
            if sums[i] == sums[-1] - sums[i + 1]:
                return i
        return -1
```
