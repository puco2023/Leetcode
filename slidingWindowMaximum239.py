import heapq
from collections import defaultdict
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        window=defaultdict(int)
        heap=[]
        res=[]
        for i in range(len(nums)):
            if i<k:
                window[nums[i]]+=1
                heapq.heappush(heap,-nums[i])
                if i==k-1:
                    res.append(-heap[0])
                continue
            window[nums[i]]+=1
            heapq.heappush(heap,-nums[i])
            window[nums[i-k]]-=1
            while -heap[0] not in window or window[-heap[0]]==0:
                heapq.heappop(heap)
            res.append(-heap[0])
        return res
  #time: O(nlogn) space: O(n^2)
