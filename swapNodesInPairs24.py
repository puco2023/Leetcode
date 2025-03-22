# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head:
            return None
        dummy=ListNode(0,head)
        prev2=dummy
        prev1=head
        curr=head.next
        if not curr:
            return head
        while curr:
            prev2.next=curr
            tmp=curr.next
            curr.next=prev1
            prev1.next=tmp
            
            prev2=prev1
            prev1=tmp
            if tmp==None:
                curr=None
            else:
                curr=tmp.next
        return dummy.next
