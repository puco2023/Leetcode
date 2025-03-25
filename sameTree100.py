class Solution(object):
    def isSameTree(self, p, q):
        self.b=True
        def dfs(p,q):
            if not p and not q:
                return
            if not p:
                self.b=False
                return
            if not q:
                self.b=False
                return
            if p.val!=q.val:
                self.b = False
            dfs(p.left,q.left)
            dfs(p.right,q.right)
        dfs(p,q)
        return self.b
        
