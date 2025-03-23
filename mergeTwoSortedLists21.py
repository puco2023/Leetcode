class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode(0)
        curr3=dummy
        while list1 and list2:
            if list1.val>list2.val:
                new=ListNode(list2.val)
                curr3.next=new
                list2=list2.next
            else:
                new=ListNode(list1.val)
                curr3.next=new
                list1=list1.next
            curr3=curr3.next
        if list1:
            curr3.next = list1
        if list2:
            curr3.next = list2
        return dummy.next
