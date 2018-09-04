# 求一个有序数列中是否存在两数之和等于指定值
> 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

> 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。


## 说明:
1. 返回的下标值（index1 和 index2）不是从零开始的。
2. 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

```
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```


## 解决思路：
1. 不考虑时间复杂度，循环中再次循环查询剩下的数，找出index
2. 可以将数组转化为字典，利用字典的查找O(1)的时间复杂度，迭代查询数组前面的数是否可以和当前数匹配
3. 可以使用双指针的思路，分别指向头尾，每次判断，头尾相加是否=target，小于的话，头指针+1；大于的话，尾指针+1

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
```