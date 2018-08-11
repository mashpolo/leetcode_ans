# Write your code here :-)
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        s = s.replace(' ', ' ')
        s_list = s.split(' ')
        print(s_list)
        while len(s_list) > 0 and s_list[-1] == '':
            s_list.pop()
        print(s_list)
        if len(s_list) > 0:
            return len(s_list[-1])
        else:
            return 0
        
