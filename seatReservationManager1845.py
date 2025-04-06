import heapq
class SeatManager(object):

    def __init__(self, n):
        self.n = n
        self.heap=[i for i in range(n)]
        heapq.heapify(self.heap)

    def reserve(self):
        return heapq.heappop(self.heap)+1

    def unreserve(self, seatNumber):
        heapq.heappush(self.heap, seatNumber-1)
