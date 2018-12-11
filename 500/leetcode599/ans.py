#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-11

"""


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        min_index = 2000
        result = []
        for i in range(len(list1)):
            dict1[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in dict1 and dict1[list2[i]] + i < min_index:
                min_index = dict1[list2[i]] + i
                result = [list2[i]]
            elif list2[i] in dict1 and dict1[list2[i]] + i == min_index:
                result.append(list2[i])
        return result




if __name__ == '__main__':
    A = Solution()
    print(A.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                           ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
