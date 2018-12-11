# 两个列表的最小索引之和

> 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

> 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

```
示例 1:

输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。
示例 2:

输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
提示:

两个列表的长度范围都在 [1, 1000]内。
两个列表中的字符串的长度将在[1，30]的范围内。
下标从0开始，到列表的长度减1。
两个列表都没有重复的元素。
```


## 解决办法：
> 该题考验的应该是有优先级顺序的两个列表重合的重要度最高的一个值

1. 首先构造一个dict，将list1遍历到dict中，key为字符，value为list1中字符串对应的索引

2. 下一步看list2中的字符串是否在dict中，若在的话求索引之和

3. 接下来判断索引之和，预设索引之和为2000

4. 构造一个list存放最小索引字符串

5. 若小于最小索引之和的话，清空list，将新的最小索引之和对应的字符串放入list

6. 若等于最小索引之和，则将字符串append进list中
7. 最后返回list

