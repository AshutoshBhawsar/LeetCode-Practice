# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return[]
        
        def collector(root,level):
            if not root:
                return
            if level==len(view):
                view.append(root.val)
            collector(root.right,level+1)
            collector(root.left,level+1)
        
        view=[]
        collector(root,0)
        return view