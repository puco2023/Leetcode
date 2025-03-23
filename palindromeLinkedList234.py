class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        half=slow
        prev=half
        curr=half.next
        while curr:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        curr=head
        tail=prev
        while curr!=half:
            if curr.val!=tail.val:
                return False
            tail=tail.next
            curr=curr.next
        return True
        
