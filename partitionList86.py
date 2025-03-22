class Solution(object):
    def partition(self, head, x):
        if not head:
            return None
        dummyL=ListNode(0)
        curr1=dummyL
        curr=head
        while curr:
            if curr.val<x:
                curr1.next=ListNode(curr.val)
                curr1=curr1.next
            curr=curr.next
        dummyR=ListNode(0)
        curr=head
        curr2=dummyR
        while curr:
            if curr.val>=x:
                curr2.next=ListNode(curr.val)
                curr2=curr2.next
            curr=curr.next
        curr1.next=dummyR.next
        return dummyL.next
