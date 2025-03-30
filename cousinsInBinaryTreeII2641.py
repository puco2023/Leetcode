class Solution(object):
    def replaceValueInTree(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return TreeNode(0)
        queue=deque([root])
        level=[]
        while queue:
            suma=0
            for _ in range(len(queue)):
                node=queue.popleft()
                suma+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level.append(suma)
        def dfs(node,depth):
            if not node:
                return
            elif not node.left and node.right:
                x=level[depth]-node.right.val
                node.right.val=x if x>0 else 0
            elif not node.right and node.left:
                x = level[depth]-node.left.val
                node.left.val=x if x>0 else 0
            elif node.left and node.right:
                x=level[depth]-node.left.val-node.right.val
                node.left.val=x if x>0 else 0
                node.right.val=x if x>0 else 0
                
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,1)
        root.val=0
        return root
