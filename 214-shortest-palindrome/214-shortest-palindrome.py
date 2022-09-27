class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n=len(s)
        i=0
        result=0
        while(i<=n):
            if self.helperIsPalindrome(s[:n-i]):
                break
            else:
                result+=1
            i+=1
        prefix=reversed(s[n-result:])
        return ''.join(prefix)+s
    
    def helperIsPalindrome(self,s:str)->bool:
        return s==s[::-1]