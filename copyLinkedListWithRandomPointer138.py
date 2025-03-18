"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        if not head:
            return 
        curr=head
        hashmap={}
        while curr:
            node=Node(curr.val,None,None)
            hashmap[curr]=node
            curr=curr.next
        curr=head
        while curr:
            if curr.next:
                hashmap[curr].next=hashmap[curr.next]
            if curr.random:
                hashmap[curr].random=hashmap[curr.random]
            curr=curr.next
        return hashmap[head]
