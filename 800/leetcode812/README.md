# 最大三角形的面积

> 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

```
示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释:
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。

```

> 注意:

- 3 <= points.length <= 50.
- 不存在重复的点。
- -50 <= points[i][j] <= 50.
- 结果误差值在 10^-6 以内都认为是正确答案


## 解决办法：
1. 只有采用迭代的方法来求值，需要动用数学的求面积公式（S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)）

```python
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        N = len(points)
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(i + 2, N):
                    (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                    res = max(res, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return res
```
