class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans=0
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            if not node.left and not node.right:
                return 1
            if not node.left:
                if node.val==node.right.val:
                    self.ans=max(self.ans,right)
                    return right+1
                else:
                    return 1
            if not node.right:
                if node.val==node.left.val:
                    self.ans=max(self.ans,left)
                    return left+1
                else:
                    return 1
            if node.left and node.right:
                if node.val==node.left.val and node.val==node.right.val:
                    self.ans=max(self.ans,left+right)
                    return max(left,right)+1
                if node.val==node.left.val:
                    self.ans=max(self.ans,left)
                    return left+1
                if node.val==node.right.val:
                    self.ans=max(self.ans,right)
                    return right+1
                if node.val!=node.left.val and node.val!=node.right.val:
                    return 1
        dfs(root)
        return self.ans
