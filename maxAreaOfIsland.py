class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans=0
        area=0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            nonlocal area
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return
            grid[r][c]=0
            area=area+1
            for x,y in directions:
                dfs(r+y, c+x)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    ans=max(ans, area)
                    area=0
        return ans
