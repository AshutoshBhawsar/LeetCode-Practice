class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for _ in s.lower():
            if _.isalnum():
                string+=_
        #print(string)
        return string==string[::-1]