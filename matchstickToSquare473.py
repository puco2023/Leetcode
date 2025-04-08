class Solution(object):
    def makesquare(self, matchsticks):
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        length = total // 4
        matchsticks.sort(reverse=True)  # Optimizacija
        used=[False] * len(matchsticks)
        def backtracking(i,sides,curr):
            if sides == 4:
                return True
            if curr==length:
                return backtracking(0, sides+1, 0)
            if curr>length:
                return False
            for j in range(i,len(matchsticks)):
                if used[j]:
                    continue
                used[j] = True
                if backtracking(j+1,sides,curr+matchsticks[j]):
                    return True
                used[j] = False
            return False
        return backtracking(0,0,0)
