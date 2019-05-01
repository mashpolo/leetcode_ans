# 全排列

> 给定一个可包含重复数字的序列，返回所有不重复的全排列。

```
示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```


## 解决办法：
1. 和上一题类似，多了一个判断是否重复的步骤

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res =[]
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            arr = nums[:]
            arr = list(set(arr))
            for pre in arr:
                index = nums.index(pre)
                newNums = nums[:index] + nums[index+1:]
                for post in self.permuteUnique(newNums):
                    res.append([pre] + post)
            return res
```
