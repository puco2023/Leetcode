# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        def dfs(node):
            if not node.left and node.val>val:
                new=TreeNode(val)
                node.left=new
                return
            if not node.right and node.val<val:
                new=TreeNode(val)
                node.right=new
                return
            if node.val>val:
                dfs(node.left)
            else:
                dfs(node.right)
        dfs(root)
        return root
