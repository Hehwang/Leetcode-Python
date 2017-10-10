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
        head2=head
        ###  creat a dict record the  frequency of values
        ### then we can know if we could drop this node in loop!
        freqDict={}
        while head2:
            if head2.val in freqDict:
                freqDict[head2.val]+=1
            else:
                freqDict[head2.val]=1
            head2=head2.next
            
        root=res=ListNode(head.val)
        while head:
            if freqDict[head.val]>1:
                head=head.next
            else:
                res.next=ListNode(head.val)
                res=res.next
                head=head.next
        return root.next