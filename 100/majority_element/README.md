# 求众数
> 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

>你可以假设数组是非空的，并且给定的数组总是存在众数。

```
示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
```




## 解决思路：
1. 遍历数组，将每个数字的存在次数都记录到一个字典中，当循环这次的数的次数超过了n/2，那么跳出循环


### 其他解决办法：
1. 先对数组进行排序，因为多数元素一定存在，且个数超过总个数的一半，那么排序后最中间的那个元素一定是多数元素
```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]
```

2. 随机抽一个元素，检查是否是多数元素，由于多数元素个数占大半，期望查找次数<2。
```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import random
        while True:
            r = random.choice(nums)
            if nums.count(r) > len(nums)/2:
                return r
```