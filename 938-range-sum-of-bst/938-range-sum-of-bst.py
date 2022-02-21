# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        return sum(x for x in self.inorder(root) if low<=x<=high)
        
    def inorder(self,root):
        return self.inorder(root.left)+[root.val]+self.inorder(root.right) if root else []