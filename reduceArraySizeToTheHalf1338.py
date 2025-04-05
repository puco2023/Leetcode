import heapq
from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        counter = Counter(arr)
        heap=[]
        for value in counter.values():
            heapq.heappush(heap,-value)
        curr=0
        res=0
        while curr<len(arr)/2:
            curr+=-heapq.heappop(heap)
            res+=1
        return res
