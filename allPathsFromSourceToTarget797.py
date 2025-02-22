class Solution(object):
    def allPathsSourceTarget(self, graph):
        visited=[False]*len(graph)
        destination=len(graph)-1
        ans=[]
        def dfs(i, path,visited):
            if visited[i]==True:
                return
            path.append(i)
            visited[i]=True
            if i==destination:
                ans.append(path[:])
                visited[i]=False
                path.remove(i)
                return
            for nei in graph[i]:
                dfs(nei, path, visited)
            visited[i]=False
            path.remove(i)
        dfs(0, [], visited)
        return ans
