class Solution(object):

    def asteroidCollision(self, asteroids):
        stack=[]
        for i in range(len(asteroids)):
            stack.append(asteroids[i])
            if len(stack)>=2 and stack[-1]*stack[-2]<0:
                if stack[-1]<0:
                    n=stack[-1]
                    p=stack[-2]
                else:
                    n=stack[-2]
                    p=stack[-1]
            while len(stack)>=2 and stack[-1]*stack[-2]<0 and len(stack)-stack[::-1].index(n)-1>len(stack)-stack[::-1].index(p)-1:
                if abs(stack[-1])<abs(stack[-2]):
                    stack.pop()
                elif abs(stack[-1])>abs(stack[-2]):
                    stack.pop(-2)
                else:
                    stack.pop()
                    stack.pop()
                if len(stack)>=2 and stack[-1]*stack[-2]<0:
                    if stack[-1]<0:
                        n=stack[-1]
                        p=stack[-2]
                    else:
                        n=stack[-2]
                        p=stack[-1]
        return stack
