# 两句话中的不常见单词

> 给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）

> 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

> 返回所有不常用单词的列表。

> 您可以按任何顺序返回列表。


```
示例 1：

输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
示例 2：

输入：A = "apple apple", B = "banana"
输出：["banana"]


提示：

0 <= A.length <= 200
0 <= B.length <= 200
A 和 B 都只包含空格和小写字母。
```

## 解决办法：
1. 采用内置的计数器，找出两个字符串中只出现一次的字符串
2. 基本就是利用一个散列表来存储两个字符串的次数

```python
class Solution(object):
    def uncommonFromSentences(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        #Alternatively:
        #count = collections.Counter(A.split())
        #count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]
```
