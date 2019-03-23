#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-23

"""


class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        evensum = sum(i for i in A if i&1==0)
        outputs = []
        for i in range(len(queries)):
            if A[queries[i][1]]&1 == 0:
                if queries[i][0]&1 == 0:
                    # 如果原始数据为偶数且新增数据为偶数，新的偶数和为上一个和加新增数据
                    evensum += queries[i][0]
                else:
                    # 如果原始数据为偶数但新增数据为奇数，新的偶数和为上一个和减原始数据
                    evensum -= A[queries[i][1]]
            else:
                if queries[i][0]&1 == 0:
                    # 如果原始数据为奇数但新增数据为偶数，新的偶数和与上一个和相同
                    pass
                else:
                    # 如果原始数据为奇数且新增数据为奇数，新的偶数和为上一个和加（原始数据+新增数据）
                    evensum += A[queries[i][1]] + queries[i][0]
            A[queries[i][1]] += queries[i][0]
            outputs.append(evensum)
        return outputs


if __name__ == '__main__':
    A = Solution()
    print(A.sumEvenAfterQueries(A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]))
