class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(0, n, 1):
            for j in range(i, n, 1):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        for i in range(0, n, 1):
            matrix[i].reverse()