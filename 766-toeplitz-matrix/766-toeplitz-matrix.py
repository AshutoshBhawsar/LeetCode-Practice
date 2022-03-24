class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        def helper(matrix,i,j,val):
            if i>=len(matrix) or j>=len(matrix[0]):
                return True
            if matrix[i][j]!=val:
                return False
            matrix[i][j]=-1
            a=helper(matrix,i+1,j+1,val)
            return a
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==-1:
                    continue
                a=helper(matrix,i,j,matrix[i][j])
                if not a:
                    return False
        return True
    
    