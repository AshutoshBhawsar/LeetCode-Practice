class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Traditional int to bin, add, bin to int
        #return '{0:b}'.format(int(a,2)+int(b,2))
    
        # Bit manipulation XOR
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]