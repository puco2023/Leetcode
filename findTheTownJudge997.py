class Solution(object):
    def findJudge(self, n, trust):
        counter={i:0 for i in range(1,n+1)}
        maybeans=-1
        for t in trust:
            counter[t[1]] += 1
        maxv=max(counter.values())
        if maxv<n-1:
            return -1
        for i in counter:
            if counter[i]==maxv:
                counter[i]=-1
                maybeans=i
        maxv2=max(counter.values())
        if maxv2==maxv:
            return -1
        for t in trust:
            if t[0]==maybeans:
                return -1
        return maybeans
