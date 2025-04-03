import heapq

class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Uklanja najmanji element
        
        return min_heap[0]  # Prvi element u min-heapu je k-ti najveći
