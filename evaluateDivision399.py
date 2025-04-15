from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for e, v in zip(equations, values):
            graph[e[0]].append((e[1], v))
            graph[e[1]].append((e[0], 1.0 / v))

        def dfs(val, node):
            if node == searched:
                return val
            for nei in graph[node]:
                if nei[0] not in visited:
                    visited.add(nei[0])
                    res = dfs(val * nei[1], nei[0])
                    if res != -1:
                        return res
                    visited.remove(nei[0])
            return -1

        ans = []
        for query in queries:
            if query[0] in graph and query[1] in graph:
                searched = query[1]
                visited = set()
                visited.add(query[0])
                x = dfs(1, query[0])
                ans.append(x)
            else:
                ans.append(-1.0)
        return ans
