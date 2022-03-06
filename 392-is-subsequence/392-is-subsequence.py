class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # basic 2 pointer
        # i,j=0,0
        # n,n2=len(t),len(s)
        # if not n2:
        #     return True
        # while(j<n and i<n2):
        #     if s[i]==t[j]:
        #         i+=1
        #     j+=1
        # return i>=n2
        
        # iter magic
        t = iter(t)
        return all(c in t for c in s)  