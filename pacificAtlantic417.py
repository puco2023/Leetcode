class Solution:
    def pacificAtlantic(self, grid):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans=[]
        Rows=len(grid)
        cols = len(grid[0])
        pacific=False
        atlantic=False
        y1=-1
        x1=-1
        def dfs(i,j,prev):
            nonlocal pacific, atlantic, y1,x1
            if i<0 or j<0:
                pacific=True
                return
            if i>=Rows or j>=cols:
                atlantic=True
                return
            if grid[i][j]>prev:
                return
            sos=grid[i][j]
            grid[i][j]=float("inf")
            for y,x in directions:
                dfs(i+y,j+x,sos)
                if pacific and atlantic:
                    break
            grid[i][j]=sos
        for i in range(Rows):
            for j in range(cols):
                dfs(i,j,float("inf"))
                if atlantic and pacific:
                    ans.append([i,j])
                atlantic=False
                pacific=False
        return ans
