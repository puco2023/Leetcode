import heapq
from collections import Counter
from collections import deque
class Solution(object):
    def leastInterval(self, tasks, n):
        mapOfFrequency = Counter(tasks)
        heap=[(-value,key) for key,value in mapOfFrequency.items()]
        heapq.heapify(heap)
        paused=deque()
        time=0
        while len(heap)>0 or len(paused)> 0:
            if len(heap)>0:
                value, task = heapq.heappop(heap)
                value+=1
                if value<0:
                    paused.append((value,time+n,task))
            if len(paused)>=1 and paused[0][1]<=time:
                value,_,task=paused.popleft()
                heapq.heappush(heap,(value,task))
            time+=1
        return time
