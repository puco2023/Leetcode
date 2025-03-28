class Solution(object):
    def tree2str(self, root):
        def dfs(node):
            if not node:
                return ""
            if node.left and node.right:
                return str(node.val) + "("+ dfs(node.left)+")" + "("+dfs(node.right)+")"
            if node.left:
                return str(node.val)+ "(" +dfs(node.left) + ")"
            if node.right:
                return str(node.val)+"()"+"("+dfs(node.right)+")"
            if not node.left and not node.right:
                return str(node.val)
        return dfs(root)
