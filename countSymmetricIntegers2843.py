class Solution(object):
    def countSymmetricIntegers(self, low, high):
        res=0
        def isSymetric(num):
            if len(num)%2==1:
                return False
            left = num[:len(num)//2]
            right = num[len(num)//2:]
            leftSum,rightSum=0,0
            for l in left:
                leftSum += int(l)
            for r in right:
                rightSum += int(r)
            return leftSum == rightSum
        for i in range(low, high+1):
            if isSymetric(str(i)):
                res+=1
        return res
