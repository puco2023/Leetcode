class Solution:
    def combinationSum(self, nums,target):
        ans=[]
        def dfs(cur,i):
            if sum(cur)>target or i>len(nums)-1:
                return
            if sum(cur)==target:
                ans.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(cur,i)
            cur.pop()
            dfs(cur,i+1)
        dfs([],0)
        return ans
