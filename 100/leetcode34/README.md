# 在排序数组中查找元素的第一个和最后一个位置

> 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

> 你的算法时间复杂度必须是 O(log n) 级别。

> 如果数组中不存在目标值，返回 [-1, -1]。

```
示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

```


## 解决办法：
1. 使用二分查找
2. 使用内置的列表获取索引的方式

```python
class Solution:
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]

        head = nums.index(target)
        tail = nums[::-1].index(target)
        return [head, len(nums) - tail]
```
