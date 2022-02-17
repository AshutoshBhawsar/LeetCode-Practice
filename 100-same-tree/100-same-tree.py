# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Traditional method recursion ##############
        # if not q and not p:
        #     return True
        # if not p or not q or p.val!=q.val:
        #     return False
        # flag1=self.isSameTree(p.left,q.left)
        # flag2=self.isSameTree(p.right,q.right)
        # return flag1 and flag2
        
        # Consolidated version ###########
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q