# 找出所有数组中没有出现的数字
> 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

> 找到所有在 [1, n] 范围之间没有出现在数组中的数字。

> 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

```
示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
```

## 解决办法：
1. 遍历数组nums，记当前元素为n，令nums[abs(n) - 1] = -abs(nums[abs(n) - 1])。
   再次遍历nums，将正数对应的下标+1返回即为答案，因为正数对应的元素没有被上一步骤标记过


### 其他办法:
1. 使用去重的办法来做

```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = set(nums)
        new = set(range(1, len(nums) + 1))
        return list(new - n)
```
