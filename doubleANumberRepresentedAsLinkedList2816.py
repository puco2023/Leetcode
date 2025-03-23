class Solution(object):
    def doubleIt(self, head):
        if not head:
            return None
        if head.val==0 and not head.next:
            return head
        curr=head
        number=""
        while curr:
            number+=str(curr.val)
            curr=curr.next
        number=int(number)
        number*=2
        arr=[]
        num=number
        while num>0:
            arr.append(num%10)
            num//=10
        arr.reverse()
        curr=head
        dummy=ListNode(0)
        curr2=dummy
        for i in arr:
            curr2.next=ListNode(i)
            curr2=curr2.next
        return dummy.next
