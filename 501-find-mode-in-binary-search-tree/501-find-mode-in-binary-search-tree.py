# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        answer=[]
        temp=root
        #inorder_trav=[]
        default_dict=collections.defaultdict(lambda:0)
        max_count=0
        while len(stack)>0 or temp is not None:
            if temp is not None:
                stack.append(temp)
                temp=temp.left
            else:
                temp=stack.pop()
                #inorder_trav.append(temp.val)
                default_dict[temp.val]=default_dict[temp.val]+1
                if default_dict[temp.val]>max_count:
                    max_count=default_dict[temp.val]
                temp=temp.right
        #print(max_count)
        
        for key,value in default_dict.items():
            if value==max_count:
                answer.append(key)
        return answer