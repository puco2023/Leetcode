class Solution:
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        memo=[-1]*len(nums)
        def dfs2(i):
            if i>len(nums)-1:
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i] = max(nums[i] + dfs2(i+2), dfs2(i+1))
            return memo[i]
        def dfs1(i):
            if i>len(nums)-2:
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i] = max(nums[i] + dfs1(i+2), dfs1(i+1))
            return memo[i]
        f=dfs1(1)
        memo=[-1]*len(nums)
        s=dfs2(0)
        return max(f,s)
