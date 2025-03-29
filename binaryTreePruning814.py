class Solution(object):
    def pruneTree(self, root):
        
        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            dfs(node.right)
            if node.left:
                if not node.left.left and not node.left.right and node.left.val==0:
                    node.left=None
            if node.right:
                if not node.right.left and not node.right.right and node.right.val==0:
                    node.right=None
        dfs(root)
        if not root.left and not root.right and root.val==0:
            return None
        return root
