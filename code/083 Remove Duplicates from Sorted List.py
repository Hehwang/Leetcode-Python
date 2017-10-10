# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        root=res=ListNode(head.val)
        while head.next:
            if head.next.val!=head.val:
                res.next=ListNode(head.next.val)
                res=res.next
                head=head.next
            else:
                head=head.next
        return root