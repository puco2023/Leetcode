import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        counter=Counter(words)
        heap=[]
        for key,value in counter.items():
            heapq.heappush(heap,(-value,key))
        res=[]
        while len(res)<k:
            _, key = heapq.heappop(heap)
            res.append(key)
        return res
