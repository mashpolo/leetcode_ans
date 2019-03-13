# 有效的山脉数组

> 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

> 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

- A.length >= 3
- 在 0 < i < A.length - 1 条件下，存在 i 使得：
- A[0] < A[1] < ... A[i-1] < A[i]
- A[i] > A[i+1] > ... > A[B.length - 1]

```
示例 1：

输入：[2,1]
输出：false
示例 2：

输入：[3,5,5]
输出：false
示例 3：

输入：[0,3,2,1]
输出：true


提示：

0 <= A.length <= 10000
0 <= A[i] <= 10000
```


## 解决办法：
1. 先找出中间点，然后对中点后面的数组排序，并去重，和原数组后面的数组比较即可
2. 直接遍历整个数组，利用两个指针指向前一个和当前的数字来判断是否达到阈值

```python
class Solution:
    def validMountainArray(self, A: 'List[int]') -> 'bool':
        if len(A) < 3:
            return False
        ind = A.index(max(A))
        if ind in [0, len(A)-1]:
            return False
        for i in range(1, ind):
            if A[i] <= A[i-1]:
                return False
        for i in range(ind+1, len(A)):
            if A[i] >= A[i-1]:
                return False
        return True
```
