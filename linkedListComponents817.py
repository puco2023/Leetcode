class Solution(object):
    def numComponents(self, head, nums):
        nums=set(nums)
        ans=0
        count=False
        while head:
            if head.val in nums and count==False:
                ans+=1
                count=True
            if head.val not in nums:
                count=False
            head=head.next
        return ans
                
