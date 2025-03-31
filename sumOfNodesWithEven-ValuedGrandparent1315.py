class Solution(object):
    def sumEvenGrandparent(self, root):
        def dfs(node):
            if not node:
                return 0
            x=0
            if node.val%2==0:
                if node.left:
                    x+=node.left.left.val if node.left.left else 0
                    x+=node.left.right.val if node.left.right else 0
                if node.right:
                    x+=node.right.left.val if node.right.left else 0
                    x+=node.right.right.val if node.right.right else 0
            return dfs(node.left)+dfs(node.right)+x
        return dfs(root)
