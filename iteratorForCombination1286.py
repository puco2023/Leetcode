class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        self.combinations=[]
        def backtrack(start,curr):
            if len(curr)==combinationLength:
                self.combinations.append("".join(curr))
                return
            for i in range(start,len(characters)):
                backtrack(i+1,curr+[characters[i]])
        backtrack(0,[])
        self.index=0
    def next(self):
        self.index+=1
        return self.combinations[self.index-1]
    def hasNext(self):
        return self.index<len(self.combinations)

