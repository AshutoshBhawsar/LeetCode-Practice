class Solution:
    def findComplement(self, num: int) -> int:
        res="0b"
        for i in bin(num)[2:]:
            if i == '1':
                res+='0'
            else:
                res+='1'
        return int(res,2)