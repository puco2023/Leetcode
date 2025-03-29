class Solution(object):
    def findTarget(self, root, k):
        def find(node, val, exclude):
            if not node:
                return False
            if node.val > val:
                return find(node.left, val, exclude)
            elif node.val < val:
                return find(node.right, val, exclude)
            else:
                return node != exclude  

        self.ans = False

        def dfs(node):
            if not node or self.ans:
                return
            if find(root, k - node.val, node):
                self.ans = True
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans
