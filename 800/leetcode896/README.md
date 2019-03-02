# 单调数列

> 如果数组是单调递增或单调递减的，那么它是单调的。

> 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

> 当给定的数组 A 是单调数组时返回 true，否则返回 false。

```
示例 1：

输入：[1,2,2,3]
输出：true
示例 2：

输入：[6,5,4,4]
输出：true
示例 3：

输入：[1,3,2]
输出：false
示例 4：

输入：[1,2,4,5]
输出：true
示例 5：

输入：[1,1,1]
输出：true


提示：

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
```


## 解决办法：
1. 采用排序的方法，倒序和正序都需要排列一次，近似需要两次遍历
2. 也可以只采用一次遍历，但需要定位A到底第一次是倒序还是正序

```python
class Solution:
    def isMonotonic(self, A):
        flag = None
        for x in range(len(A) - 1):
            if flag is None:
                if A[x] > A[x+1]:
                    flag = 0
                elif A[x] < A[x+1]:
                    flag = 1
                else:
                    flag = None
                continue
            if x + 1 == len(A):
                return A[x] <= A[x+1] if flag == 0 else A[x] >= A[x+1]
            if A[x] > A[x+1] and flag > 0:
                return False
            elif A[x] < A[x+1] and not flag:
                return False

        return True
```
