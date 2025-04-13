class Solution(object):
    def getHappyString(self, n, k):
        letters=["a","b","c"]
        res=[]
        def backtracking(curr):
            if len(curr)==n:
                res.append("".join(curr))
                return len(res)==k
            for i in range(3):
                if (curr and curr[-1]==letters[i]):
                    continue
                curr.append(letters[i])
                if backtracking(curr):
                    return True

                curr.pop()
        backtracking([])
        return res[-1] if len(res)>=k else ""
