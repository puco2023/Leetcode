class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        nodes=[]
        for i in range(n):
            for j in range(n):
                if i==j or isConnected[i][j]==0:
                    continue
                nodes.append([i,j])
        parent=[i for i in range(n)]
        rank=[1 for i in range(n)]
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i,j):
            p1=find(i)
            p2=find(j)
            if p1==p2:
                return False
            if rank[p1]<rank[p2]:
                rank[p2]+=rank[p1]
                parent[p2]=p1
            else:
                rank[p1]+=rank[p2]
                parent[p1]=p2
            return True
        res=n
        for i,j in nodes:
            if union(i,j):
                res-=1
        return res
