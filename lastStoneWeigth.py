class Solution:
    def lastStoneWeight(self, stones):
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones) != 0 and len(stones)!=1:
            x=-heapq.heappop(stones)
            y=-heapq.heappop(stones)
            if x!=y:
                m=abs(x-y)
                heapq.heappush(stones,-m)
        if stones:
            return -stones[0]
        else:
            return 0
