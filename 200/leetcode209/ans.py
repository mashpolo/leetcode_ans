class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) == s:
            return len(nums)
        if sum(nums) < s:
            return 0
        sum_temp = left = 0
        min_len = len(nums)
        for right in range(len(nums)):
            sum_temp += nums[right]
            while sum_temp >= s:
                min_len = min(min_len, right-left+1)
                sum_temp -= nums[left]
                left += 1       
        return min_len

