# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(None)
        dummy.next=head
        pre=dummy
        cur=dummy
        i=0
        while i<n:
            cur=cur.next
            i+=1
        
        while cur and cur.next:
            pre=pre.next
            cur=cur.next
        pre.next=pre.next.next
        return dummy.next
