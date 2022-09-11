class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # m,n=len(matrix),len(matrix[0])
        # transpose=[[0 for i in range(m)] for j in range(n)]
        # #print(transpose)
        # for i in range(m):
        #     for j in range(n):
        #         transpose[j][i]=matrix[i][j]
        # return transpose
    
    
        # Shortcut
        return zip(*matrix)