# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val==val:
            return root
        root1=self.searchBST(root.left,val)
        root2=self.searchBST(root.right,val)
        if root1: return root1
        elif root2: return root2
        else: return None