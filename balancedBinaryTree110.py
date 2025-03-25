class Solution(object):
    def isBalanced(self, root):
        self.b=True
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            if abs(right-left)>1:
                self.b=False
            return max(left,right)+1
        dfs(root)
        return self.b
