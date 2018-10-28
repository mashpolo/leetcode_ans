class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for x in digits:
            num += str(x)
        num = int(num) + 1
        num_list = list(str(num))
        rest = map(lambda x: int(x), num_list)
        return list(rest)
