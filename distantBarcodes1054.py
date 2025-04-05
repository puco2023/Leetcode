import heapq
from collections import Counter
from collections import deque
import math


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        counter = Counter(barcodes)
        heap=[]
        for key,value in counter.items():
            heapq.heappush(heap,(-value,key))
        res=[]
        prev=None
        while len(res)<len(barcodes):
            cnt,code = heapq.heappop(heap)
            cnt+=1
            if prev:
                heapq.heappush(heap,(prev[0],prev[1]))
                prev=None
            if cnt<0:
                prev=(cnt,code)
            res.append(code)
        return res
