# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        # recursion inorder+linear scan
#         def inorder(r):
#             return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
#         return min(inorder(root), key = lambda x: abs(target - x))

        #iterative
        r = root.val
        while root:
            if abs(root.val - target) < abs(r - target):
                r = root.val
            root = root.left if target < root.val else root.right
        return r