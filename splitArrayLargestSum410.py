class Solution(object):
    def Try(self,nums,k,tr):
        diff=tr
        res=-1
        a=0
        for num in nums:
            diff=diff-num
            if diff<0:
                res=max(res,a)
                a=0
                diff=tr-num
                a=a+num
                k-=1
                res=max(res,a)
            else:
                a+=num
            if k<=0:
                return -1
        res=max(res,a)
        return res
            
    def splitArray(self, nums, k):
        l=max(nums)
        r=sum(nums)
        ans=float("inf")
        while l<=r:
            m=(l+r)//2
            maybe=self.Try(nums,k,m)
            if maybe<0:
                l=m+1
            else:
                ans=min(ans,maybe)
                r=m-1
        return ans
