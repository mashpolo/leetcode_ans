class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = 0 #记录数组中出现一次和两次的异或，出现三次会在出现一次中消去
        for n in nums:
            one = ~two & (one^n)
            two = ~one & (two^n)
        return one
