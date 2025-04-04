import heapq
from collections import defaultdict
class Solution(object):
    def findRelativeRanks(self, score):
        heap = [(-s,i) for i,s in enumerate(score)]
        heapq.heapify(heap)
        res=[0]*len(score)
        br=0
        while heap:
            val, index = heapq.heappop(heap)
            if br==0:
                res[index]="Gold Medal"
            elif br==1:
                res[index] = "Silver Medal"
            elif br==2:
                res[index]="Bronze Medal"
            else:
                res[index]=str(br+1)
            br+=1
        return res
