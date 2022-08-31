class Solution:
    def confusingNumber(self, n: int) -> bool:
        valid_dict={'0':'0','1':'1','6':'9','8':'8','9':'6'}
        invalid_dict={'2':'0','3':'0','4':'0','5':'0','7':'0'}
        new_num=""
        for i in str(n):
            if i in invalid_dict:
                return False
            new_num+=valid_dict[i]
        return True if int(new_num[::-1])!=n else False