class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return None
        dummy=ListNode(0,head)
        odd=head
        even=dummy
        prevOdd=None
        while odd and odd.next:
            even.next=odd.next
            even=even.next
            odd.next=even.next
            prevOdd=odd
            odd=odd.next
        if not odd:
            odd=prevOdd
            
        else:
            even.next=None
        odd.next=dummy.next
        return head
