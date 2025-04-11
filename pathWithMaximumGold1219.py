class Solution(object):
    def getMaximumGold(self, grid):
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        rows, cols = len(grid), len(grid[0])
        self.ans = 0

        def dfs(i, j, curr, visited):
            self.ans = max(self.ans, curr)
            for dx, dy in direction:
                ni, nj = i + dx, j + dy
                if (0 <= ni < rows and 0 <= nj < cols and
                        (ni, nj) not in visited and grid[ni][nj] > 0):
                    visited.add((ni, nj))
                    dfs(ni, nj, curr + grid[ni][nj], visited)
                    visited.remove((ni, nj))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    visited = set()
                    visited.add((i, j))
                    dfs(i, j, grid[i][j], visited)
        return self.ans
