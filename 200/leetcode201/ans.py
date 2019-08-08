class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        if m==0:
            return 0
        if m==n:
            return m
        count = 0
        while True:
            if m!=n:
                m >>= 1
                n >>= 1
                count += 1
            else:
                break
        for j in range(count):
            m <<=1
        return m
