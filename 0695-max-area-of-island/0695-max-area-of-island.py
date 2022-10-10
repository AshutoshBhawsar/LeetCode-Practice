class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    max_area=max(max_area,self.helper_area(grid,i,j))
        return max_area
    
    def helper_area(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
            return 0
        grid[i][j]='$'
        return 1+\
            self.helper_area(grid,i+1,j)+\
            self.helper_area(grid,i,j+1)+\
            self.helper_area(grid,i-1,j)+\
            self.helper_area(grid,i,j-1)