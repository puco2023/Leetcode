import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        heap=[]
        hashMap=Counter(nums)
        for num in hashMap:
            heapq.heappush(heap,(-hashMap[num],num))
        res=[]
        for _ in range(k):
            freq,num = heapq.heappop(heap)
            res.append(num)
        return res
