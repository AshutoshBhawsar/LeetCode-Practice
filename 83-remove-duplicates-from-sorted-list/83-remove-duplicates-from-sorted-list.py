# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        hmap=collections.OrderedDict()
        
        temp=head
        while(temp):
            if temp.val not in hmap:
                hmap[temp.val]=temp.val
            temp=temp.next
        dummy=ListNode(0)
        temp=dummy
        for item in hmap.values():
            new=ListNode(item)
            temp.next=new
            temp=new
        return dummy.next