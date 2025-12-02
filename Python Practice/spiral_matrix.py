# Given an m x n matrix, return all elements of the matrix in spiral order.

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t,l = 0, 0
        b = len(matrix) -1
        r = len(matrix[0])-1
        result = []
        if not matrix or not matrix[0]:
            return []
        while t <= b and l <= r:

            for i in range(l, r+1):
                result.append(matrix[l][i])
            t+=1
            for i in range(t, b+1):
                result.append(matrix[i][r])
            r-=1

            if t <= b:
                for i in range(r, l-1,-1):
                    result.append(matrix[b][i])
                b-=1
            if l <= r:
                for i in range(b, t-1,-1):
                    result.append(matrix[i][l])
                l+=1
        return result 
    

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))