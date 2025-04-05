import heapq
from collections import Counter
from collections import deque
import math
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        heapq.heapify(products)
        returnWords=[]
        res=[]
        i=0
        s=""
        while i<len(searchWord):
            s+=searchWord[i]
            i+=1
            while products:
                w=heapq.heappop(products)
                n=len(s)
                if s==w[:n]:
                    returnWords.append(w)
                if len(returnWords)>2:
                    break
            res.append(returnWords[:])
            while returnWords:
                heapq.heappush(products, returnWords.pop())

        return res
