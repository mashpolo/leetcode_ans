# 插入区间

> 给出一个无重叠的 ，按照区间起始端点排序的区间列表。

> 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。


```
示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
```


## 解决办法：
1. 根据题意，来判断当前插入的区间最小值和最大值，然后合并，再和下一个区间进行比较
2. 二分法插入

```python
class Solution:
    def insert(self, intervals, newInterval):
        start, end = newInterval[0], newInterval[-1]
        res = []
        flag = False
        if not intervals or not newInterval:
            return [intervals + newInterval]

        for index, interval in enumerate(intervals):
            if interval[1] < start:
                res.append(interval)
                if index < len(intervals) - 1 and intervals[index + 1][0] > end:
                    res.append(newInterval)
            elif interval[0] > end:
                if flag:
                    res.append([start, end])
                    flag = False
                res.append(interval)
            else:
                start = min(interval[0], start)
                end = max(interval[1], end)
                flag = True
        if flag:
            res.append([start, end])
        else:
            if intervals[0][0] > end:
                res.insert(0, newInterval)
            elif intervals[-1][1] < start:
                res.append(newInterval)
        return res
```
