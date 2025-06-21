class Solution(object):
    def canPlaceFlowers(self, flowerbe, n):
        flowerbed = flowerbe[:]
        jump = False
        #edge case
        if flowerbed==[0] and n==1:
            return True
        if n==0:
            return True
        for i,flower in enumerate(flowerbed[:-1]):
            if jump:
                jump = False
                continue
            if flower == 0 and flowerbed[i+1]==0:
                n-=1
                jump = True
                flowerbed[i]=1
            if n==0:
                return True
            if flower==1:
                jump = True
        # fill the last if possible
        if len(flowerbed)>=2 and n==1 and flowerbed[-1]==0 and flowerbed[-2]==0:
            return True
        return False
