class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1,num2,c1,c2=0,0,0,0
        while l1:
            num1+=l1.val*(10**c1)
            c1+=1
            l1=l1.next
        while l2:
            num2+=l2.val*(10**c2)
            c2+=1
            l2=l2.next
        num=num1+num2
        num_str=list(str(num))
        num_str.reverse()
        root=res=ListNode(0)
        for i in num_str:
            res.next=ListNode(i)
            res=res.next
        return root.next