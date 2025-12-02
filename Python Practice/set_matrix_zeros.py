# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        r_track = [0 for _ in range(r)]
        c_track = [0 for _ in range(c)]
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    r_track[i] = -1
                    c_track[j] = -1
        for i in range(0, r):
            for j in range(0, c):
                if r_track[i] == -1 or c_track[j] == -1:
                    matrix[i][j] = 0
        return matrix


sol = Solution()
print(sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))