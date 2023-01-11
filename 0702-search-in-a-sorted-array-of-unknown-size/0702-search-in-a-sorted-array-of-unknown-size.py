# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # find boundaries in log (n) time
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            # Same as right*=2, we optimize using bitwise shift instead of mul
            right <<= 1
        
        # classic binary search
        while left <= right:
            pivot = left + (right - left)//2
            num = reader.get(pivot)
            
            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1
        
        return -1