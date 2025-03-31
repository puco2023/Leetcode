class Solution(object):
    def maxProduct(self, root):
        if not root:
            return 0
        def dfs1(node):
            if not node:
                return 0
            return node.val+dfs1(node.left)+dfs1(node.right)
        self.suma=dfs1(root)
        self.max=float("-inf")
        def dfs(node):
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            x=l+r+node.val
            self.max=max(self.max,(self.suma-x)*x)
            return x
        dfs(root)
        return self.max % (10**9 + 7) 
