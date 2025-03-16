class Solution(object):
    def Try(self,weights,days,tons):
        day=1
        diff=tons
        for w in weights:
            diff=diff-w
            if diff<0:
                day+=1
                diff=tons-w
            if day>days:
                return False
        return True
    def shipWithinDays(self, weights, days):
        l=max(weights)
        r=sum(weights)
        while l<=r:
            m=(l+r)//2
            if self.Try(weights,days,m):
                r=m-1
            else:
                l=m+1
        return l
