class Solution(object):
    def findTilt(self, root):
        
        def sumAllSubtree(node):
            if not node:
                return 0
            left = sumAllSubtree(node.left)
            right=sumAllSubtree(node.right)
            node.val+=left+right
            return node.val
            
        sumAllSubtree(root)
        
        def tiltSubtree(node):
            if not node:
                return
            if node.left and node.right:
                node.val=abs(node.left.val-node.right.val)
            elif node.left and not node.right:
                node.val=abs(node.left.val)
            elif node.right and not node.left:
                node.val=abs(node.right.val)
            else:
                node.val=0
            tiltSubtree(node.left)
            tiltSubtree(node.right)
        tiltSubtree(root)
        
        self.ans=0
        def suma(node):
            if not node:
                return 0
            self.ans+=node.val
            suma(node.left)
            suma(node.right)
        suma(root)
        return self.ans
