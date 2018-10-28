# 两个数组的交集2

> 给定两个数组，编写一个函数来计算它们的交集。

```
示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
```

**说明：**

- 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
- 我们可以不考虑输出结果的顺序。

**进阶:**

- 如果给定的数组已经排好序呢？你将如何优化你的算法？
- 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
- 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？


## 解决思路：
1. 找出小的那个数组来进行遍历，判断是否存在大数组中，需要注意的是需要确定大数组中的索引不和上一次的重复


### 最优解答：
1. 用字典统计第一个列表都出现了哪些数及出现的次数，
然后顺序遍历第二个列表，发现同时出现的数则加入到结果列表中，同时将第一个列表中相应的出现次数减一

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] -= 1

        return res
```

2. 考虑到进阶，不能一次加载数组到内存中，借用counter计数器，不过是将两个数组都统计成dict，再计算交集

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
```