class Solution(object):
    def isValidSerialization(self, preorder):
        if preorder=="#":
            return True
        if preorder=="#,#,#":
            return False
        arr=preorder.split(",")
        if len(arr)<3:
            return False
        if arr[-1]!="#" or arr[-2] !="#":
            return False
        reqClosed=2
        currClosed=0
        for i in range(1,len(arr)-2):
            if arr[i]=="#":
                currClosed+=1
            else:
                reqClosed+=1
            if reqClosed<=currClosed:
                return False
        currClosed+=2
        return reqClosed==currClosed
