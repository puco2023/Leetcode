class Solution(object):
    def countCompleteComponents(self, n, edges):
        adj={}
        checked=set()
        
        for edge in edges:
            if edge[0] not in adj:
                adj[edge[0]]=[edge[1]]
            else:
                adj[edge[0]].append(edge[1])
            if edge[1] not in adj:
                adj[edge[1]]=[edge[0]]
            else:
                adj[edge[1]].append(edge[0])
        ans=n-len(adj)
        numOfEdges=0
        
        def dfs(node):
            if node in checked:
                return 0
            checked.add(node)
            edges=0
            for nei in adj[node]:
                edges+=1
                edges+=dfs(nei)
            return edges
                
        def valid(nodes,numberOfEdges):
            requiredNumberOfedges=0
            for i in range(nodes):
                requiredNumberOfedges+=i
            if requiredNumberOfedges==numberOfEdges:
                return 1
            else:
                return 0
        for node in adj:
            if node not in checked:
                before=len(checked)
                numOfEdges=dfs(node)
                after=len(checked)
                ans+=valid(after-before,numOfEdges/2)
                numOfEdges=0
        return ans
                
