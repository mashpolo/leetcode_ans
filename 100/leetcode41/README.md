# 缺失的第一个正数

> 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

```
示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

```


```python
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        leng = len(nums)
        nums.append(nums[0])
        for i in nums:
            idx = i
            while idx is not None and 1 <= idx <= leng and nums[idx] is not None:
                t = nums[idx]
                nums[idx] = None
                idx = t

        for i in range(1, leng+1):
            if nums[i] is not None:
                return i
        return leng+1
```


## 解决办法：
1. 假设数组长度为 len，则缺的正数 x 一定满足 0 < x <= len+1，所以只考虑这个范围内的数，如果存在，将以其为下标的数组元素标记为None。
2. 注意点：1. 数组需要扩容一个元素。2. 标记需要递归进行直到目标数已经被标记，我代码里将递归转换成了循环。
