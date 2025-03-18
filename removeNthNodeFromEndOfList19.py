# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        br=1
        curr=head
        while curr.next:
            curr=curr.next
            br+=1
        k=br-n
        if k==0:
            return head.next
        br=1
        curr=head
        dummy=head
        while curr:
            if br==k:
                curr.next=curr.next.next
                br+=1
            else:
                curr=curr.next
                br+=1
        return dummy
