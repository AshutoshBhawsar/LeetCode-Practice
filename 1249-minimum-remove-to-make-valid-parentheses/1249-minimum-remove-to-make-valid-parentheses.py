class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        list1={}
        ans=''
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if not stack:
                    list1[i]=i
                    continue
                else:
                    stack.pop()
        if stack:
            for i in stack:
                list1[i]=i
        for i in range(len(s)):
            if i not in list1:
                ans+=s[i]
        return ans
            