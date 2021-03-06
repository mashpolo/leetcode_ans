# 报数

> 报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
```
1.     1
2.     11
3.     21
4.     1211
5.     111221
```
- 1 被读作  "one 1"  ("一个一") , 即 11。
- 11 被读作 "two 1s" ("两个一"）, 即 21。
- 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

> 给定一个正整数 n ，输出报数序列的第 n 项。
> 注意：整数顺序将表示为一个字符串。

```
示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"
```


## 解决思路：
1. 迭代的方式，从2开始，依次往上类加，直到和n相等
2. while循环每次保存上一次的报数结果
3. for循环读取上次的报数结果，返回下一次的报数值


## 最优解
> itertools的group_by方法可以返回一个字符串中每次重复的有多少个

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res
```