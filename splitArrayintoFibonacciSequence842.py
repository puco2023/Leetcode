class Solution(object):
    def splitIntoFibonacci(self, num):
        res=[]
        fib=[]
        def backtrack(start,fib):
            if start==len(num):
                if len(fib)>2:
                    res.append(fib[:])
                    return True
                return False
            for i in range(start,len(num)):
                new=num[start:i+1]
                if new[0]=="0" and len(new)>1:
                    continue
                new=int(new)
                if new>2**31-1:
                    return False
                if (len(fib)<2 or fib[-1]+fib[-2]==new):
                    fib.append(new)
                    if backtrack(i+1,fib):
                        return True
                    fib.pop()

        backtrack(0,[])
        return res[0] if res else []
