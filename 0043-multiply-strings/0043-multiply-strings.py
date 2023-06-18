class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        first,second=0,0
        for i,ch in enumerate(reversed(num1)):
            if i<1:
                first+=int(ch)
                continue
            first+=int(ch)*(10**(i))
        for j,ch2 in enumerate(reversed(num2)):
            if j<1:
                second+=int(ch2)
                continue
            second+=int(ch2)*(10**(j))
        return str(first*second)