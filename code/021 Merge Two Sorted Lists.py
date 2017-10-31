# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root=res=ListNode(0)
        while l1 and l2:
            if l1.val>=l2.val:
                res.next=ListNode(l2.val)
                l2=l2.next
            else:
                res.next=ListNode(l1.val)
                l1=l1.next
            res=res.next
        if l1:
            res.next=l1
        if l2:
            res.next=l2
        return root.next