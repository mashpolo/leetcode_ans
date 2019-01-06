# 數據流中的第K大元素

> 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

> 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

```
示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明:
你可以假设 nums 的长度≥ k-1 且k ≥ 1。
```

## 解決辦法：
1. 題有點複雜，題意沒有寫好，都有點懵逼
2. 根據提示，使用堆的方式來解決
3. Python的堆是小根堆，不需要对其进行转换，我们想一想，如果一个堆的大小是k的话，那么最小的数字就在其最前面（即为第k大的数字），只要维护当新来的数字和最前面的这个数字比较即可。
4. 所以我们的工作就是维护一个小根堆，这个小根堆保存的是从第K大的数字到最大的数字。堆的大小即为K。
