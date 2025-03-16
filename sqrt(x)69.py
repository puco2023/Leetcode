class Solution(object):
    def mySqrt(self, x):
        l=1
        r=x
        while l<=r:
            m=(l+r)//2
            if m*m>x:
                r=m-1
            elif m*m<x:
                l+=1
            elif m*m==x:
                return m
        return l-1
