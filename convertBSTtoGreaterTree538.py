class Solution(object):
    def convertBST(self, root):
        self.currSum=0
        def dfs(root):
            if not root:
                return 
            dfs(root.right)
            self.currSum+=root.val
            root.val=self.currSum
            dfs(root.left)
        dfs(root)
        return root
            
