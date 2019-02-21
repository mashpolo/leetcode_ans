# 转置矩阵

> 给定一个矩阵 A， 返回 A 的转置矩阵。

> 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。


```
示例 1：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]


提示：

1 <= A.length <= 1000
1 <= A[0].length <= 1000
```

## 解决办法：
1. 可以直接使用zip高阶函数来转置即可
2. 思路和下面的类似

```python
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rown=len(A)
        if rown==0:
            return A
        coln=len(A[0])
        result=[]
        for j in range(coln):
            newrow=[]
            for i in range(rown):
                newrow.append(A[i][j])
            result.append(newrow)
        return result
```
