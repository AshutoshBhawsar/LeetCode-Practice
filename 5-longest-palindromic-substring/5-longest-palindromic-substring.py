class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        for i in range(len(s)):
            temp=self.helper(s,i,i)
            if len(temp)>len(result):
                result=temp
            temp=self.helper(s,i,i+1)
            if len(temp)>len(result):
                result=temp
        return result
    
    def helper(self,s:str,l:int,r:int)->str:
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        return s[l+1:r]