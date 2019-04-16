# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
            :type head: ListNode
            :rtype: ListNode
            """
        res = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = res
            res = curr
            curr = temp
        return res


