class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node):
        visited=set()
        graph={}
        def dfs(node):
            if node in visited:
                return graph[node]
            visited.add(node)
            graph[node]=Node(node.val)
            for neighbor in node.neighbors:
                graph[node].neighbors.append(dfs(neighbor))
            return graph[node]
        return dfs(node) if node else None
      
