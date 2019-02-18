# 山脉数组的峰顶索引

> 我们把符合下列属性的数组 A 称作山脉：

> A.length >= 3
> 存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
> 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

```
示例 1：

输入：[0,1,0]
输出：1
示例 2：

输入：[0,2,1,0]
输出：1


提示：

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A 是如上定义的山脉
```

## 解决办法：
1. 这个题就是求数组中最大值的索引，因此利用内置方法来求取即可，但时间复杂度是O(n)
2. 使用二分查找，时间复杂度O(logn)

```python
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left = 0
        right = len(A) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid > 0 and A[mid] > A[mid - 1]:
                left = mid
            else:
                right = mid

        if A[left] > A[right]:
            return left

        return right
```
