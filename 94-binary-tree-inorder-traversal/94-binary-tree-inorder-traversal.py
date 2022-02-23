# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        temp=root
        answer=[]
        while len(stack)>0 or temp is not None:
            if temp is not None:
                stack.append(temp)
                temp=temp.left
            else:
                temp=stack.pop()
                answer.append(temp.val)
                temp=temp.right
        return answer
                
                