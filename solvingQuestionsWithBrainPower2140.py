class Solution(object):
    def mostPoints(self, questions):
        helper=[0]*(len(questions)+1)
        helper[-1]=questions[-1][0]
        for i in range(len(questions)-1,-1,-1):
            x=0
            if i+questions[i][1]+1<len(questions):
                x=max(helper[i+questions[i][1]+1]+questions[i][0],helper[i+1])
            else:
                x=max(helper[i+1],questions[i][0])
            helper[i]=x
        return helper[0]
