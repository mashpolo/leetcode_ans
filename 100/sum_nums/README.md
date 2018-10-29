# 选择两个数
> 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

> 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

```shell
示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```















# 思路：
> 暴力搜索，实际上需要从列表中先查找到减法取到的值，然后再从列表中获取该值的索引，这两个动作都是o(n)的时间复杂度，所以整个脚本就收o(n*n)
> 优化思路，使用hashmap，通过key去查找value是o(1)的时间复杂度，我们应该先将列表遍历，然后存入字典{列表的值：索引}，找到值以后直接查找value就可以了