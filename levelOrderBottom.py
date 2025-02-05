from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
       self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        ans=[]
        l=[]
        o=0
        if not root:
            return []
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                l.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(l)
            l=[]
        return ans[::-1]
