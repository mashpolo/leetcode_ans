# 求最大和的子序列
> 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

```
示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

## 进阶:

> 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。



## 解决思路：
1. 利用迭代的思路，从第一个数相加，到最后
2. 如果前面相加都是负数，那么都抛弃掉，从新计算


## 利用分治法来解决
1. 对于任何一个array来说，有三种可能：
- 它的maximum subarray 落在它的左边；
- maximum subarray 落在它的右边；
- maximum subarray 落在它的中间。

2. 对于第一，二种情况，利用二分法就很容易得到，base case 是如果只有一个数字了，那么就返回。

3. 对于第三种情况，如果落在中间，那么我们要从左右两边返回的两个 mss 中，挑出一个大的，再从 （左右中大的值） 和 （左+右）中挑出一个大的

```python
class Solution(object):
    def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return -2147483647
        m = (l+r) / 2

        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):  # 从中间向左遍历
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)

        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):  # 从中间向右遍历
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)

        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)

        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))

    def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
```