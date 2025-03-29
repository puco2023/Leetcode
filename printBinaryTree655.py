class Solution(object):
    def printTree(self, root):
        if not root:
            return None
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left),depth(node.right))+1
        ROWS=depth(root)
        COLS=2**(ROWS)-1
        self.tree=[["" for _ in range(COLS)] for i in range(ROWS)] 
        def dfs(node,r,c):
            if not node:
                return 
            self.tree[r][c]=str(node.val)
            dfs(node.left,r+1,c-2**(ROWS-r-2))
            dfs(node.right,r+1,c+2**(ROWS-r-2))
        dfs(root,0,COLS//2)
        return self.tree
            
