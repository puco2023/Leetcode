class Solution:
    def combinationSum2(self, nums,target):
        ans=[]
        def dfs(curr,i):
            if sum(curr)==target:
                p=curr.copy()
                p.sort()
                if p not in ans:
                    ans.append(p)
                return
            if sum(curr)>target or i>len(nums)-1:
                return
            curr.append(nums[i])
            dfs(curr,i+1)
            curr.pop()
            dfs(curr,i+1)
        dfs([],0)
        return ans
