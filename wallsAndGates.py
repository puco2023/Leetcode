from collections import deque
class Solution:
    def islandsAndTreasure(self, grid):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        Rows, Cols = len(grid), len(grid[0])
        visited = set()
        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            distance = 1
            while queue:
                for _ in range(len(queue)):
                    y, x = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= ny < Rows and 0 <= nx < Cols and (ny, nx) not in visited:
                            if grid[ny][nx] != -1 and grid[ny][nx] != 0:
                                grid[ny][nx] = min(grid[ny][nx], distance)
                                visited.add((ny, nx))
                                queue.append((ny, nx))
                distance += 1
        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 0:
                    bfs(i, j)
                    visited=set()
