#solution 1
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
#solution 2
class Solution(object):
    def combine(self, n, k):
        ans=[]
        curr=[]
        def dfs(j):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            if j>=n:
                return
            for i in range(j,n):
                curr.append(i)
                dfs(j+1)
                curr.pop()
        dfs(1)
        return ans
