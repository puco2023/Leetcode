class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue=deque()
        queue.append(root)
        level=1
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
