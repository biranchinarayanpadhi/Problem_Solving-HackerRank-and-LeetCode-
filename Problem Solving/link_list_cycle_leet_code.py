# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
        
        p=head
        q=head.next
        while p!=q:
            if q==None or q.next==None:
                return False
            p=p.next
            q=q.next.next
        return True