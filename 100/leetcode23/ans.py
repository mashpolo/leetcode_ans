#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-12

"""
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        heap = []
        res = None
        node_map = {}
        val_map = {}
        for (index, node) in enumerate(lists):
            if not node:
                continue
            node_map[index] = node
            if node.val in val_map:
                val_map[node.val].append(index)
            else:
                val_map[node.val] = [index]
            heapq.heappush(heap, node.val)

        while heap:
            if res is None:
                small = heapq.heappop(heap)
                node_index = val_map[small].pop()
                res = node_map[node_index]
                now = res
                new = node_map[node_index].next
                node_map[node_index] = new
                if new:
                    if new.val in val_map:
                        val_map[new.val].append(node_index)
                    else:
                        val_map[new.val] = [node_index]
                    heapq.heappush(heap, new.val)
            else:
                small = heapq.heappop(heap)
                node_index = val_map[small].pop()

                now.next = node_map[node_index]
                now = now.next

                new = node_map[node_index].next

                if new:
                    node_map[node_index] = new
                    if new.val in val_map:
                        val_map[new.val].append(node_index)
                    else:
                        val_map[new.val] = [node_index]
                    heapq.heappush(heap, new.val)
        return res

