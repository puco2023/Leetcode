class Solution(object):
    def pathSum(self, root, targetSum):
        ans=[]
        def dfs(root, cs,l):
            #nonlocal ans
            if not root:
                return False
            if not root.left and not root.right:
                if targetSum==root.val+cs:
                    l.append(root.val)
                    ans.append(l)
            dfs(root.left,cs+root.val,l+[root.val])
            dfs(root.right,cs+root.val,l+[root.val])
        dfs(root,0,[])
        return ans
