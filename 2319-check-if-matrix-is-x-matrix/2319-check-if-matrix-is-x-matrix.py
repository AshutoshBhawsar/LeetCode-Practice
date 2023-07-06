class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0 and (i != j and j != n - i - 1):
                    return False
                elif grid[i][j] == 0 and (i == j or j == n - i - 1):
                    return False
        return True