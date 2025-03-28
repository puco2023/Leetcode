class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth==1:
            newNode = TreeNode(val)
            newNode.left=root
            return newNode
        def dfs(node,currH):
            if not node:
                return
            if currH==depth-1:

                L=node.left
                R=node.right
                
                newNode=TreeNode(val)
                node.left=newNode
                newNode.left=L
                
                newNode=TreeNode(val)
                node.right=newNode
                newNode.right=R
                return
            dfs(node.left,currH+1)
            dfs(node.right,currH+1)
        dfs(root,1)
        return root
