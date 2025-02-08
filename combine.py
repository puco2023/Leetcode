class Solution(object):
    def combine(self, n, k):
        ans=[]
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        curr=[]
        def dfs(j):
            if len(curr) == k:
                ans.append(curr[:])
                return
            if j>=len(nums):
                return
            curr.append(nums[j])
            dfs(j+1)
            curr.pop()
            dfs(j+1)
        dfs(0)
        return ans
