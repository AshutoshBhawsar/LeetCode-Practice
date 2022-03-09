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
        answer=ListNode(0)
        pointer=answer
        temp=head
        hmap=collections.OrderedDict()
        while(temp):
            if temp.val in hmap:
                hmap[temp.val]=False
            else:
                hmap[temp.val]=True
            temp=temp.next
        for ele in hmap.keys():
            if hmap[ele]:
                new=ListNode(ele)
                pointer.next=new
                pointer=pointer.next
        return answer.next