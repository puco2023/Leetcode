class Solution:
    def permute(self, nums):
        used=[False]*len(nums)
        ans=[]
        def backtracking(curr,i):
            if len(curr)==len(nums):
                ans.append(curr[:])
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                curr.append(nums[i])
                backtracking(curr,i)
                curr.pop()
                used[i] = False
        backtracking([],0)
        return ans
