# 下一个最大的元素

> 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

> nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

```
示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
示例 2:

输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
```

**注意:**

- nums1和nums2中所有元素是唯一的。
- nums1和nums2 的数组大小都不超过1000。


## 解决思路：
1. 考虑栈的数据结构，栈stack维护nums的递减子集，记nums的当前元素为n，栈顶元素为top，
重复弹出栈顶，直到stack为空，或者top大于n为止，将所有被弹出元素的next greater element置为n
```python
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dmap = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dmap[stack.pop()] = n
            stack.append(n)
        return [dmap.get(n, -1) for n in findNums]
```

### 其他解决思路：
1. 朴素解法，O(n*m)

```python
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dmap = {v : k for k, v in enumerate(nums)}
        size = len(nums)
        ans = []
        for e, n in enumerate(findNums):
            for j in range(dmap[n] + 1, size):
                if nums[j] > n:
                    ans.append(nums[j])
                    break
            if len(ans) <= e: ans.append(-1)
        return ans
```
