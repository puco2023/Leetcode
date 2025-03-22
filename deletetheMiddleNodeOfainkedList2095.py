class Solution(object):
    def deleteMiddle(self, head):
        if not head:
            return None
        if not head.next:
            return None
        if not head.next.next:
            head.next=None
            return head
        if not head.next.next.next:
            head.next=head.next.next
            return head
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        prev.next=slow.next
        return head
