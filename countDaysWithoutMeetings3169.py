class Solution(object):
    def countDays(self, days, meetings):
        sortedM=sorted(meetings, key=lambda x: x[0])
        stack=[]
        deleted=True
        for meeting in sortedM:
            stack.append(meeting)
            deleted=True
            while len(stack)>=2 and deleted:
                deleted=False
                while len(stack)>=2 and stack[-2][1]>=stack[-1][1]:
                    stack.pop()
                    deleted=True
                while len(stack)>=2 and stack[-2][1]<stack[-1][1] and stack[-2][1]>=stack[-1][0]-1:
                    a,b = stack.pop()
                    c,d = stack.pop()
                    stack.append([c,b])
                    deleted=True
        ans=0
        for i in range(len(stack)):
            if i==0:
                ans+=stack[i][0]-1
            if i>0:
                k=stack[i][0]-stack[i-1][1]-1
                if k>0:
                    ans+=k
        k=days-stack[-1][1]
        if k>0:
            ans+=k
        return ans
