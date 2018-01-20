# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        root1=res1=ListNode(None)
        root2=res2=ListNode(None)
        while head:
            if head.val<x:
                res1.next=ListNode(head.val)
                res1=res1.next
            else:
                res2.next=ListNode(head.val)
                res2=res2.next
            head=head.next
        res1.next=root2.next
        return root1.next