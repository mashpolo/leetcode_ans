# 208. 实现 Trie (前缀树)

> 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

```
示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
```

> 说明:

> 你可以假设所有的输入都是由小写字母 a-z 构成的。
> 保证所有输入均为非空字符串。


## 解决办法：
1. 考虑到时间复杂度，必须要一个字典来存储数据，将每个存储的单词按照字母拆分，作为键，方便后面来查询
