class Solution:
    def numIslands(self, grid):
        numberOfIslands = 0
        Rows,Cols = len(grid),len(grid[0])

        def dfs(i,j):
            if i>=Rows or i<0 or j>=Cols or j<0 or grid[i][j]=="0":
                return
            grid[i][j] = "0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    numberOfIslands+=1
        return numberOfIslands
