class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        counter=0
        while(s!=goal):
            s=self.rotate(s)
            if counter>len(s):
                break
            counter+=1
        return True if counter<len(s) else False
        
    def rotate(self, s:str)->str:
        return s[1:]+s[0]