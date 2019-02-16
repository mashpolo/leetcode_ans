class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        res_s = []
        for x in S:
            if x == '#' and len(res_s) > 0:
                res_s.pop()
            elif x == '#' and not res_s:
                continue
            else:
                res_s.append(x)
        res_t = []
        for y in T:
            if y == '#' and len(res_t) > 0:
                res_t.pop()
            elif y == '#' and not res_t:
                continue
            else:
                res_t.append(y)
        print(res_t, res_s)
        return res_s == res_t
