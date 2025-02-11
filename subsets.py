class Solution:
    def subsets(self, nums):
        ans=[]
        def backtrack(i,curr):
            if len(curr)==len(nums) or i>=len(nums):
                ans.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(i+1,curr)
            curr.pop()
            backtrack(i+1,curr)
        backtrack(0,[])
        return ans
