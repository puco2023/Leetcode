class ListNode():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyCircularQueue(object):

    def __init__(self, k):
        self.head=ListNode()
        self.last=self.head
        self.len=0
        self.k=k
    def enQueue(self, value):
        if self.len==self.k:
            return False
        if self.len==0:
            self.last=ListNode(value)
            self.head=self.last
            self.last.next=self.head
        else:
            new=ListNode(value)
            self.last.next=new
            new.next=self.head
            self.last=self.last.next
        self.len+=1
        return True
    def deQueue(self):
        if self.len==0:
            return False
        if self.len==1:
            self.head=self.last=None
        else:
            self.head=self.head.next
            self.last.next=self.head
        self.len-=1
        return True
    def Front(self):
        if self.isEmpty():
            return -1
        return self.head.val
        
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.last.val
        

    def isEmpty(self):
        return self.len==0

    def isFull(self):
        return self.k==self.len


