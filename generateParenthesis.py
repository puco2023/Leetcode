class Solution:
    def generateParenthesis(self, n):
        stack=[]
        ans=[]
        def dfs(open,close):
            if open==close==n:
                ans.append("".join(stack))
                return
            if open<n:
                stack.append("(")
                dfs(open+1,close)
                stack.pop()
            if close<open and close<n:
                stack.append(")")
                dfs(open,close+1)
                stack.pop()
        dfs(0,0)
        return ans
