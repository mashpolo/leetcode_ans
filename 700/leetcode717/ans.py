class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits.pop()
        res = 0
        while bits:
            node = bits.pop()
            if node == 1:
                res += 1
            else:
                break
        if res % 2 !=0:
            return False
        else:
            return True
