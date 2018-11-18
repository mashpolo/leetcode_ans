# 检测大写字母

> 给定一个单词，你需要判断单词的大写使用是否正确。

> 我们定义，在以下情况时，单词的大写用法是正确的：

- 全部字母都是大写，比如"USA"。
- 单词中所有字母都不是大写，比如"leetcode"。
- 如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
  否则，我们定义这个单词没有正确使用大写字母。

```
示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。
```

## 解决办法：
1. 按照说明一一判断，效率很低


### 其他办法：
1. 使用正则匹配

```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        import re
        pat = '([A-Z]*|[A-Z][a-z]*|[a-z]*)$'
        return True if re.compile(pat).match(word) else False
```


2. 使用逻辑判断
```python
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return  word.isupper() or word.istitle() or word.islower()
```
