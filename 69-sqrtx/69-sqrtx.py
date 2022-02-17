class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Cheating and using formula sqrt(x)=e^(0.5*log(x))
#         if x < 2:
#             return x
        
#         left = int(e**(0.5 * log(x)))
#         right = left + 1
#         return left if right * right > x else right
    
        # Newton's method
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r