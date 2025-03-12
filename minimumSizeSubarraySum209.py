class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        r=0
        ans=len(nums)+1
        suma=nums[0]
        while l<len(nums):
            if suma>=target:
                ans=min(ans,r-l+1)
                suma-=nums[l]
                l+=1
            elif r<len(nums)-1:
                r+=1
                suma+=nums[r]
            else:
                suma-=nums[l]
                l+=1
        if ans==len(nums)+1:
            return 0
        else:
            return ans
