class Solution(object):
    def uniquePathsIII(self, grid):
        self.req = 0
        starti, startj = -1, -1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != -1:
                    self.req += 1
                if grid[i][j] == 1:
                    starti = i
                    startj = j

        visited = set()
        visited.add((starti, startj))
        self.ans = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i, j):
            if grid[i][j] == 2:
                if len(visited) == self.req:
                    self.ans += 1
                return
            for d in directions:
                newI, newJ = i + d[0], j + d[1]
                if 0 <= newI < ROWS and 0 <= newJ < COLS and (newI, newJ) not in visited and grid[newI][newJ] != -1:
                    visited.add((newI, newJ))
                    dfs(newI, newJ)
                    visited.remove((newI, newJ))
        dfs(starti, startj)
        return self.ans
