class Solution:
    def solve(self, board):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        Rows,Cols = len(board),len(board[0])
        shouldBeo=set()
        def dfs(i,j):
            nonlocal shouldBeo
            if i<0 or i>=Rows or j<0 or j>=Cols or board[i][j]=="X":
                return
            shouldBeo.add((i, j))
            board[i][j] = "X"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        for i in range(Rows):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][Cols-1]=="O":
                dfs(i,Cols-1)
        for i in range(Cols):
            if board[0][i]=="O":
                dfs(0,i)
            if board[Rows-1][i]=="O":
                dfs(Rows-1,i)
        for i in range(Rows):
            for j in range(Cols):
                if (i,j) in shouldBeo:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
