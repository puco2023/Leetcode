class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.sum=0
        def dfs(root,leftOrRight):
            if not root:
                return 0
            left = dfs(root.left,True)
            right = dfs(root.right,False)
            if not root.left and not root.right and leftOrRight==True:
                self.sum+=root.val
            return root.val
        dfs(root,False)
        return self.sum
