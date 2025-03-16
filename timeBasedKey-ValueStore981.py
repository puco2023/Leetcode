class TimeMap(object):

    def __init__(self):
        self.keyStore={}


    def set(self, key, value, timestamp):
        if key not in self.keyStore:
            self.keyStore[key]=[(value,timestamp)]
        else:
            self.keyStore[key].append((value,timestamp))
        

    def get(self, key, timestamp):
        l=0
        if key in self.keyStore:
            r=len(self.keyStore[key])-1
        else:
            return ""
        if r==-1:
            return ""
        if timestamp<self.keyStore[key][0][1]:
            return ""

        while l<=r:
            m=(l+r)//2
            if self.keyStore[key][m][1]>timestamp:
                r=m-1
            elif self.keyStore[key][m][1]<timestamp:
                l=m+1
            else:
                return self.keyStore[key][m][0]
        return self.keyStore[key][l-1][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
