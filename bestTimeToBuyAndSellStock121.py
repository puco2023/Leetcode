class Solution:
    def maxProfit(self, prices):
        memo={}
        def dfs(i,have):
            if (i,have) in memo:
                return memo[(i,have)]
            if i>=len(prices):
                return 0
            if have:
                memo[(i,have)]= max(dfs(i+1,have),prices[i]+dfs(i+2,False))
                return memo[(i,have)]
            else:
                memo[(i,have)] = max(dfs(i+1,have),-prices[i]+dfs(i+1,True))
                return memo[(i,have)]
        return dfs(0,False)
