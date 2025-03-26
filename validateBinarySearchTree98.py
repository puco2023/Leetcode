class Solution(object):
    def isValidBST(self, root):
         
        def dfs(left,right,node):
            if not node:
                return True
            if not left<node.val<right:
                return False
            return dfs(left,node.val,node.left) and dfs(node.val,right,node.right)
        return dfs(float("-inf"),float("inf"),root)
