# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count_good_nodes(node,current_max):
            count=0
            if node is not None:
                if node.val>=current_max:
                    current_max=node.val
                    count+=1
                count+=count_good_nodes(node.left,current_max)
                count+=count_good_nodes(node.right,current_max)
            return count
        
        return count_good_nodes(root,root.val)