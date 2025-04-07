import heapq
class Solution(object):
    def matrixSum(self, nums):
        helper=[]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                helper.append(-nums[i][j])
            heapq.heapify(helper)
            nums[i]=helper
            helper=[]

        res=0
        sum=0
        while nums:
            for i in range(len(nums)):
                if len(nums[i])==0:
                    return res
                sum=max(sum,-heapq.heappop(nums[i]))

            sum=sum
            res+=sum
            sum=0
#time: O(m*n*logm)
