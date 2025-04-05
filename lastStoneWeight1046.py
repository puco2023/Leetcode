import heapq
from collections import Counter
from collections import deque
import math
#Time:O(nlogn)

class Solution(object):
    def lastStoneWeight(self, stones):
        stones=[-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) != 1 and len(stones) != 0:
            bigest=-heapq.heappop(stones)
            secodnBigest=-heapq.heappop(stones)
            diff=bigest-secodnBigest
            if diff>0:
                heapq.heappush(stones, -diff)
        return -stones[0] if len(stones)==1 else 0
