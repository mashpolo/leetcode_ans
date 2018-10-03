# 单词模式

> 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

> 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

```
示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
```

**说明:**
> 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。


## 解决思路：
1. 只需要建立两个字符串的一一映射就行了，这里的关键就在于需要判断是否是一一对应关系

### 最优解
1. 直接判断每个数组中的第一个元素存在的位置即可

```python
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split(' ')
        return list(map(s.index,s)) == list(map(pattern.find,pattern))

```