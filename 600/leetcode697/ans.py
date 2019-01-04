from collections import Counter


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        max_num = count.most_common()[0][1]
        res = len(nums)
        for x in count:
            if count[x] == max_num:
                start = nums.index(x)
                end = len(nums) - nums[::-1].index(x)
                print(x, start, end)
                if len(nums[start: end]) < res:
                    res = len(nums[start: end])

        return res


if __name__ == "__main__":
    A = Solution()
    print(A.findShortestSubArray([1,2,2,3,1]))
