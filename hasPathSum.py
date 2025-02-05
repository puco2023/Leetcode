class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(root, cs):
            if not root:
                return False
            if not root.left and not root.right:
                return cs == targetSum - root.val
            return dfs(root.left, cs + root.val) or dfs(root.right, cs + root.val)
        return dfs(root, 0)
