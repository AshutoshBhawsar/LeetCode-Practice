class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_hmap,col_hmap={},{}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i not in row_hmap:
                        row_hmap[i]=1
                    if j not in col_hmap:
                        col_hmap[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row_hmap or j in col_hmap:
                    matrix[i][j]=0