import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        heap=[]
        i=0
        for row in mat:
            br=row.count(1)
            heapq.heappush(heap,(-br,-i))
            i+=1
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        while heap:
            res.append(-heapq.heappop(heap)[1])
        res.reverse()
        return res
