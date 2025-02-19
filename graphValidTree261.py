class Solution:
    def validTree(self, n, edges):
        visited=set()
        graph={i:[] for i in range(n)}
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for i in graph[node]:
                if prev==i:
                    continue
                if dfs(i,node)==False:
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(visited)==n
