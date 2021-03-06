# 最小覆盖子串

>给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

```
示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
```




## 解决方法：
> 这个题hard 但是是一个典型的滑动窗口siliding window的题目
1. 使用哈希表 统计t中每个字母出现的个数 一会这个个数将会成为滑动窗口左右极限位置变化的标志
2. 因为限制了最大时间复杂度时O（n） 遍历s的过程中我们要完成很多事

> 遍历s字符串:
    - 每次遍历一个字母 将这个字母在hash表中的映射 - 1 如果映射小于0 表示这个字母在t中没有出现过 >=0代表出现过
    - 遍历的过程中，如果t中的字母已经全部出现，则开始对窗口的左端点进行移动:
        在移动的过程中 我们的目的是找到这部分窗口中的最小字符串
        从窗口左边第一个字母开始判断：如果窗口长度比之前的最小字符串长度小 更新minlen
        如果在hash表中对left位置字符映射+1之后 映射如果>0 整明这个字符是当前窗口中 唯一出现的一个t中的字符 cnt-- 即这个lef就是左极限位置
    - 别忘了 我们还在大循环里面 当找到这个窗口中的最小字符串后 窗口右端又将开始移动

