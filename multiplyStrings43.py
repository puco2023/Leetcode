from collections import deque
class Solution(object):
    def multiply(self, num1, num2):
        ans = []
        help1 = deque()
        carry=0
        m=0
        for i1,v1 in enumerate(reversed(num1)):
            for i2,v2 in enumerate(reversed(num2)):
                help = (ord(v1)-ord("0")) * (ord(v2)-ord("0")) + carry
                carry = help // 10
                help %= 10
                help1.appendleft(help)
            if carry:
                help1.appendleft(carry)
                carry = 0
            partial = int("".join(map(str, help1)))*10**m
            help1.clear()
            m += 1
            ans.append(partial)
        
        ans = sum(ans)
        return str(ans)
            
