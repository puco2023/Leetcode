class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for operation in operations:
            if operation=="C":
                stack.pop()
            elif operation=="D":
                stack.append(stack[-1]*2)
            elif operation=="+":
                a=stack[-1]+stack[-2]
                #stack.pop()
                #stack.pop()
                stack.append(a)
            else:
                stack.append(int(operation))
        return sum(stack)
