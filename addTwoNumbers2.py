class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prenos=0
        curr1=l1
        curr2=l2
        dummy=ListNode(0)
        curr3=dummy
        while curr1 or curr2:
            if curr1 and curr2:
                newVal=curr1.val+curr2.val+prenos
            if not curr1:
                newVal=curr2.val+prenos
            if not curr2:
                newVal=curr1.val+prenos
            if newVal>9:
                newVal%=10
                prenos=1
            else:
                prenos=0
            newNode=ListNode(newVal)
            curr3.next=newNode
            curr3=curr3.next
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        if prenos==1:
            curr3.next=ListNode(1)
        return dummy.next
        
