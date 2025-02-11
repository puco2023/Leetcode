import heapq
import math
class Solution:
    def kClosest(self, points, k):
        ans=[]
        distances = []
        for i in range(len(points)):
            x = math.sqrt((points[i][0] ** 2) + (points[i][1] ** 2))
            distances.append((x, points[i]))
        heapq.heapify(distances)
        while k>0:
            ans.append(distances[0][1])
            heapq.heappop(distances)
            k-=1
        return ans
