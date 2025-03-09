class Solution(object):
    def sortColors(self, nums):
        numshelper=[1]*len(nums)
        l=0
        d=len(nums)-1
        for num in nums:
            if num==0:
                numshelper[l]=0
                l+=1
            if num==2:
                numshelper[d]=2
                d-=1
        nums[:]=numshelper[:]
        return nums
        
