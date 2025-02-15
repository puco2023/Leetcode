#from collections import deque
class Solution:

    def orangesRotting(self, grid):
        def correct(y,x):
            if x>=0 and x<len(grid[0]) and y>=0 and y<len(grid) and grid[y][x]==1:
                return True
        res=0
        Rows=len(grid)
        Cols=len(grid[0])
        def bfs():
            time=-1
            queue = deque()
            for i in range(Rows):
                for j in range(Cols):
                    if grid[i][j]==2:
                            queue.append((i, j))
            while queue:
                for _ in range(len(queue)):
                    y,x=queue.popleft()
                    if correct(y+1,x):
                        queue.append((y+1,x))
                        grid[y+1][x]=2
                    if correct(y-1,x):
                        queue.append((y-1,x))
                        grid[y-1][x]=2
                    if correct(y,x+1):
                        queue.append((y,x+1))
                        grid[y][x+1]=2
                    if correct(y,x-1):
                        queue.append((y,x-1))
                        grid[y][x-1]=2
                time+=1
            for i in range(Rows):
                for j in range(Cols):
                    if grid[i][j] == 1 or grid[i][j]==0:
                        time = -1
            return time

        return bfs()
