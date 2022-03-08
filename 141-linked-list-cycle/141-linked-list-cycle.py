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
        if head==None:
            return False
        fast_run,slow_run=head.next,head
        while(fast_run!=None):
            if(fast_run==slow_run):
                return True
            else:
                if(fast_run.next==None):
                    fast_run=fast_run.next
                else:
                    fast_run=fast_run.next.next
                slow_run=slow_run.next
        
        return False
    