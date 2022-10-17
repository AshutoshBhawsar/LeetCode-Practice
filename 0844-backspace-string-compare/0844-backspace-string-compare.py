class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return True if self.simulateBackspace(s)==self.simulateBackspace(t) else False
        
    def simulateBackspace(self,string:str)->str:
        stack=[]
        for i in string:
            if i=='#' and stack:
                stack.pop()
            elif i!='#':
                stack.append(i)
        return ''.join(stack)