class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        l = len(nums)
        x = 0
        y = 1
        Flag = 1
        while Flag <= l - 1:
            if nums[x] == nums[y]:
                nums.pop(y)
            else:
                x += 1
                y += 1

            Flag += 1
            
        return len(nums)
