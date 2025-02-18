class Solution:
    def countComponents(self, n, edges):
        ans = 0
        graph={i:[] for i in range(n)}
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        leftToPop=[]
        for i in range(n):
            leftToPop.append(i)
        visited=set()
        def dfs(i,prev):
            nonlocal visited, leftToPop
            if i in visited:
                return
            visited.add(i)
            leftToPop.remove(i)
            for node in graph[i]:
                if node == prev:
                    continue
                dfs(node,i)
        while len(leftToPop)>0:
            dfs(leftToPop[0],-1)
            ans+=1
            visited=set()
        return ans
