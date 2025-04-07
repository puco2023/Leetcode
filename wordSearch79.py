class Solution(object):
    def exist(self, board, word):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(currIndex,i,j,visited):
            if currIndex==len(word):
                return True
            for d in directions:
                if 0<=i+d[0]<len(board) and 0<=j+d[1]<len(board[i]) and board[i+d[0]][j+d[1]]==word[currIndex] and (i+d[0],j+d[1]) not in visited:
                    visited.add((i+d[0],j+d[1]))
                    if dfs(currIndex+1,i+d[0],j+d[1],visited):
                        return True
                    visited.remove((i+d[0],j+d[1]))

            return False
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if dfs(1,i,j,visited):
                        return True
                    visited=set()
        return False
