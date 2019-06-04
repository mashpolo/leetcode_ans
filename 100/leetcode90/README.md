# 子集 II

> 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

```
说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```


## 解决办法：
1. 采用迭代器模块中的排列组合方法来解决，需要注意的是，事先需要将原数组排序，否则会出现元素位置不一样但是元素一样的数组，导致无法去重


### 其他解决办法：
1. 思路和上面一样,一次遍历将每个元素加到子集中， 而由于重复元素和其他的元素重组过程中会得到重复的子集，那么就需要考虑不保留重复的序列

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = [[]]
        for i in range(len(nums)-1, -1, -1):
            for subres in res[:]:
                res.append(subres+[nums[i]])
                if res.count(res[-1]) > 1:
                    res.pop()

        return res

```
