# 搜索插入位置

> 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素

```
示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
```


## 解决思路：
1. 一般直接使用迭代，由于是有序无重复的数组，直接每次拿到数组的数和target比较就行了
2. 上面的思路，时间复杂度O(n)，可以使用二分法来优化时间复杂度O(logn)，每次都是切半，中间数来和target比较

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums) - 1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return right
```