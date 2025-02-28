class Solution:
    def uniquePaths(self, m, n):
        board=[]
        sos=[]
        for i in range(m):
            sos=[]
            for i in range(n):
                sos.append(-1)

            board.append(sos)
        for i in range(m):
            board[i][0]=1
        for i in range(n):
            board[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                board[i][j] = board[i][j-1] + board[i-1][j]
        return board[m-1][n-1]
