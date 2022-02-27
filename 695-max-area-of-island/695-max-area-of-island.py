class Solution(object):
    count=0
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxcount=0
        if not grid:
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.helper(grid,i,j)
                    maxcount=max(self.count,maxcount)
                    self.count=0
        return maxcount
    
    def helper(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
            return
        self.count+=1
        grid[i][j]='$'
        self.helper(grid,i+1,j)
        self.helper(grid,i-1,j)
        self.helper(grid,i,j+1)
        self.helper(grid,i,j-1)