#!/usr/bin/env python
# coding=utf-8
"""
@desc:   
@author: Luo.lu
@date:   2018-9-22

"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        nums_dict = {}
        for (index, x) in enumerate(nums):
            if x in nums_dict:
                if int(index - nums_dict[x]) <= k:
                    return True
                else:
                    nums_dict[x] = index
            else:
                nums_dict[x] = index

        return False


if __name__ == "__main__":
    A = Solution()
    print(A.containsNearbyDuplicate([1,2,1,3], 3))
