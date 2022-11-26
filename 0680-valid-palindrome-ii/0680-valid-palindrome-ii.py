class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s,i,j):
            string=s[i:j+1]
            return string==string[::-1]
        
        n=len(s)
        l,r=0,n-1
        while(l<r):
            if s[l]!=s[r]:
                return checkPalindrome(s,l,r-1) or checkPalindrome(s,l+1,r)
            l+=1
            r-=1
            
        return True