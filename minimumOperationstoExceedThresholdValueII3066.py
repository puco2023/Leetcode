import heapq
class Solution(object):
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        res=0
        while nums[0]<k:
            min=heapq.heappop(nums)
            secondMin=heapq.heappop(nums)
            add=min*2+secondMin
            heapq.heappush(nums,add)
            res+=1
        return res
