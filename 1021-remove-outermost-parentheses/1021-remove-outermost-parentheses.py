class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        temp=""
        result=""
        for _ in s:
            if _=='(':
                count+=1
            else:
                count-=1
            temp+=_
            if count==0:
                result+=temp[1:-1]
                temp=""
        return result
        
                