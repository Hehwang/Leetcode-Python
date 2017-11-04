# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists)==0:
            return None
        import sys
        root=res=ListNode(0)
        currentVal=[None]*len(lists)
        ### initial the currentVal
        for i in range(len(lists)):
            if lists[i]:
                currentVal[i]=lists[i].val
            else:
                currentVal[i]=sys.maxint
        while min(currentVal)!=sys.maxint:
            tmpmin=min(currentVal)
            tmpindex=currentVal.index(tmpmin)
            res.next=ListNode(tmpmin)
            res=res.next
            if lists[tmpindex].next:
                lists[tmpindex]=lists[tmpindex].next
                currentVal[tmpindex]=lists[tmpindex].val
            else:
                currentVal[tmpindex]=sys.maxint
        return root.next