class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves_flag = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}
        root = [0, 0]
        for i in moves:
            root = [root[0]+moves_flag[i][0], root[1]+moves_flag[i][1]]
            
        if root == [0, 0]:
            return True
        else:
            return False
