# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
#         color=0
#         hmap={}
#         result=[]
#         def colorTree(root,color):
#             if root:
#                 if color in hmap:
#                     hmap[color].append(root.val)
#                 else:
#                     hmap[color]=[root.val]
                
#                 colorTree(root.left,color-1)
#                 colorTree(root.right,color+1)
                
#                 return
        
#         colorTree(root,color)
#         for i in sorted(hmap.keys()):
#             result.append(hmap[i])
#         return result

        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]