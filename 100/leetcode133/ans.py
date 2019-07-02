#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-03

"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.dic = {} # store all the copy nodes: dic[node] = copy
        return self.dfs(node)

    def dfs(self, node):
        if node not in self.dic:
            self.dic[node] = Node(node.val, []) # get copy of the node 'node' and add it into the dictionary.
            for nei in node.neighbors:   # recursive: get the nei***ors of the node 'copy'.
                self.dic[node].neighbors.append(self.dfs(nei))
        return self.dic[node] # return the node 'copy'.
