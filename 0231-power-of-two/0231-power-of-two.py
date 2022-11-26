class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #print(math.ceil(math.log(n)/math.log(2)), int(math.log(n)/math.log(2)))
        #return True if math.ceil(math.log(n)/math.log(2)) == int(math.log(n)/math.log(2)) else False
        return n > 0 and not (n & n-1)