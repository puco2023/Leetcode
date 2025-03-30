class Solution(object):
    def isCousins(self, root, x, y):
        if not root:
            return False
        def bfs(x):
            queue=deque([(root,0,None)])
            while queue:
                node,depth,par=queue.popleft()
                if node.val==x:
                    return (depth,par)
                if node.left:
                    queue.append((node.left,depth+1,node))
                if node.right:
                    queue.append((node.right,depth+1,node))
        first=bfs(x)
        second=bfs(y)
        return first[0]==second[0] and first[1]!=second[1]
