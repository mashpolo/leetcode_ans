# 验证回文字符串

> 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

```
示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

```

## 解决思路：
1. 使用双指针的思路，首尾同时往中间走，判断每次首尾的值是否相等