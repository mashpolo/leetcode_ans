# 按奇偶排序数组 II

> 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

> 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

> 你可以返回任何满足上述条件的数组作为答案。


```
示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。


提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
```

## 解决办法：
1. 分别统计出不符合条件的偶数和奇数的列表，然后再交换位置

```python
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ou = [i for i in A if i % 2]
        ji = [i for i in A if not i % 2]
        return [i for n in zip(ji, ou) for i in n]
```
