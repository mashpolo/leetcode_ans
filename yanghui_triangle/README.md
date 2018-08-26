# 杨辉三角

> 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

> 在杨辉三角中，每个数是它左上方和右上方的数的和。

```
示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

## 解决办法：
1. 使用迭代和递归均可
2. 例子中使用了迭代的方法


### 最优解
- 使用了map和lambda的方法，利用矩阵的数据结构来加和成当前层
- 在利用map计算相邻两个数的和，再拼接成列表

```python
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        for i in range(1,numRows):
            print(res[-1]+[0],[0]+res[-1])
            res.append(list(map(lambda x, y : x + y, res[-1]+[0], [0]+res[-1])))
        return res[:numRows]
```
