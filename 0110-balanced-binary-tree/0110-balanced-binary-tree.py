# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
       # Recursive approach
        if not root: return True
        if abs(self.helper(root.left,0)-self.helper(root.right,0))>1:
            return False
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        return True
        
    def helper(self,root,depth):
        if not root:
            return depth
        left = self.helper(root.left,depth+1)
        right = self.helper(root.right,depth+1)
        return max(left,right)
