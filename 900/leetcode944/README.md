# 删列造序

> 比如，有 A = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 A 为["bef", "vyz"]， A 的列分别为["b","v"], ["e","y"], ["f","z"]。（形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。

> 假设，我们选择了一组删除索引 D，那么在执行删除操作之后，A 中所剩余的每一列都必须是 非降序 排列的，然后请你返回 D.length 的最小可能值。


```
示例 1：

输入：["cba", "daf", "ghi"]
输出：1
解释：
当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。
若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。
示例 2：

输入：["a", "b"]
输出：0
解释：D = {}
示例 3：

输入：["zyx", "wvu", "tsr"]
输出：3
解释：D = {0, 1, 2}
提示：

1 <= A.length <= 100
1 <= A[i].length <= 1000
```


## 解决办法：
1. 看成是一个矩阵，然后转置即可，然后判断每个元素是否是降序
2. 利用zip内置函数，代码可以更加简洁

```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        result=0
        for col in zip(*A):
            if sorted(col)!=list(col):
                result+=1
        return result
```
