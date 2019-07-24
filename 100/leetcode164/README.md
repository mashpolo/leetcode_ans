# 最大间距

> 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

> 如果数组元素个数小于 2，则返回 0。

```
示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
```

## 解决办法：
1. 排序然后遍历


### 最优解法
1. 使用桶排序的办法

```python
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        # 如果数组最大值最小值相等，则最大间距为0
        if min_num == max_num:
            return 0

        # 初始化三个长度为len(nums)+1的空数组，依次代表N+1个桶的信息。
        # bool_bkt：代表桶中是否存在元素。
        # min_bkt：代表对应桶中的最小元素。
        # max_bkt：代表对应桶中的最大元素。
        bool_bkt = [0]*(length+1)
        min_bkt = [float('inf')]*(length+1)
        max_bkt = [-float('inf')]*(length+1)

        # 遍历数组，对于每个元素找到其对应的桶
        for i in range(length):
            bkt_idx = self.findBucket(nums[i], length, min_num, max_num)
            # 更新桶的标记位和对应的最大最小值
            if bool_bkt[bkt_idx] == 0:
                bool_bkt[bkt_idx] = 1
            if bool_bkt[bkt_idx] == 1:
                min_bkt[bkt_idx] = nums[i] if nums[i] < min_bkt[bkt_idx] else min_bkt[bkt_idx]
                max_bkt[bkt_idx] = nums[i] if nums[i] > max_bkt[bkt_idx] else max_bkt[bkt_idx]

        # 查找最大间距
        res = 0
        stack = []    # 依次存储包含元素的桶号
        if bool_bkt[0] == 1:
            stack.append(0)
        for i in range(1, length + 1):
            if bool_bkt[i] == 1:
                stack.append(i)
                if min_bkt[stack[-1]] - max_bkt[stack[-2]] > res:
                    res = min_bkt[stack[-1]] - max_bkt[stack[-2]]
            else:
                continue
        return res

    def findBucket(self, element, length, min_num, max_num):
        bkt_index = ((element - min_num) * length) // (max_num - min_num)
        return bkt_index
```
