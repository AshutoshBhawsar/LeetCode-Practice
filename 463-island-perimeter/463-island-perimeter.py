class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s, m = len(grid), len(grid[0])
        ans = 0
        for x in xrange(s):
            for y in xrange(m):
                if grid[x][y] == 1:
                    ans += 4
                    if x < s - 1 and grid[x+1][y] == 1:
                        ans -= 2
                    if y < m - 1 and grid[x][y+1] == 1:
                        ans -= 2

        return ans