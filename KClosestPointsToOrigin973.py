import heapq
from collections import Counter
from collections import deque
import math
class Solution(object):
    def kClosest(self, points, k):
        res=[]
        heap=[]
        for point in points:
            x=point[0]
            y=point[1]
            distance=math.sqrt((x**2)+(y**2))
            heapq.heappush(heap,(-distance, [x,y]))
            if len(heap)>k:
                heapq.heappop(heap)
        while heap:
            _,coordinates=heapq.heappop(heap)
            res.append(coordinates)
        return res
