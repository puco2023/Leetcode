class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks)
        task_counts=[-i for i in task_counts.values()]
        heap = []
        for i in task_counts:
            heapq.heappush(heap, i)
        ans=0
        stack=[]
        time=0
        t=0
        while heap or stack:
            time+=1
            if heap:
                c=heapq.heappop(heap)
                c+=1
                if c<0:
                    stack.append((c,time+n))
            if stack and stack[0][1]==time:
                c,x=stack.pop(0)
                heapq.heappush(heap,c)
        return time
