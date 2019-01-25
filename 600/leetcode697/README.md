# 数组的度

> 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

> 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

```
示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释: 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
注意:

nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。
```

## 解决办法：
1. 使用计数器找到所有的元素，然后最大的一个来做列表截取的操作


### 最优解
```python
import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return 1
        num_dict = {num:nums.count(num) for num in nums_set}
        degree = max(num_dict.values())
        most_numbers = [num for num in nums_set if num_dict[num] == degree]
        scale = 100000000
        for most_number in most_numbers:
            appear = [i for i,num in enumerate(nums) if num == most_number]
            appear_scale = max(appear) - min(appear) + 1
            if appear_scale < scale:
                scale = appear_scale
        return scale
```