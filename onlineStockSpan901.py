class StockSpanner(object):
    def __init__(self):
        self.stack=[]
    def next(self, price):
        i=len(self.stack)-1
        br=1
        while self.stack and price>=self.stack[-1][0]:
            br+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price,br])
        return br
