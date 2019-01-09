# 设计哈希映射

> 不使用任何内建的哈希表库设计一个哈希映射

> 具体地说，你的设计应该包含以下的功能

- put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
- get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
- remove(key)：如果映射中存在这个键，删除这个数值对。

```
示例：

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // 返回 1
hashMap.get(3);            // 返回 -1 (未找到)
hashMap.put(2, 1);         // 更新已有的值
hashMap.get(2);            // 返回 1
hashMap.remove(2);         // 删除键为2的数据
hashMap.get(2);            // 返回 -1 (未找到)

注意：

所有的值都在 [1, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希库。
```

## 解决办法：
1. 最简单的办法就是利用两个数组来一一对应，不仅可以存储数字，还包括其他的类型，范性函数
2. 如果只存储数字，可以利用上一题的一些思路

```python
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBuckect = 1001
        self.hashmap = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if not self.hashmap[hashkey]:
            self.hashmap[hashkey] = [None] * self.itemsPerBuckect
        self.hashmap[hashkey][self.pos(key)] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey = self.hash(key)
        if (not self.hashmap[hashkey]) or self.hashmap[hashkey][self.pos(key)] == None:
            return -1
        else:
            return self.hashmap[hashkey][self.pos(key)]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][self.pos(key)] = None
```
