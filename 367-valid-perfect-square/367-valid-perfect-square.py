class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Binary search
#         if num < 2:
#             return True
        
#         left, right = 2, num // 2
        
#         while left <= right:
#             x = left + (right - left) // 2
#             guess_squared = x * x
#             if guess_squared == num:
#                 return True
#             if guess_squared > num:
#                 right = x - 1
#             else:
#                 left = x + 1
        
#         return False
    
        # Newton's method
        r = num
        while r*r > num:
            r = (r + num/r) / 2
        return r*r == num