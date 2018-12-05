# 最短无序连续子数组

> 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

> 你找到的子数组应是最短的，请输出它的长度。

```
示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
```



## 解决办法：
> 对数组nums排序，记排序后的数组为snums，数组长度为n
> 令s = e = -1

> 从0到n-1枚举i，记满足nums[i] != snums[i]的最小i值为s，最大i值为e

> 则当s != e时，所求最短连续子数组为nums[s .. e]

> 否则，所求子数组为空

```python
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        s = e = -1
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                if s == -1: s = i
                e = i
        return e - s + 1 if e != s else 0
```
